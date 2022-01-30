#  Copyright (C) 2022 Sam Steele
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import json
from m5stack import lcd, axp, M5Led
from m5ui import setScreenColor
from uiflow import wait
from m5mqtt import M5mqtt
from easyIO import map_value

import wifiCfg
import unit

## How low can the water level get before the tank is considered empty
MAX_DISTANCE = 50

## MQTT configuration
MQTT_CLIENT = 'AeroGarden'
MQTT_HOST = 'pi.local'
MQTT_PORT = 1883
MQTT_USER = ''
MQTT_PASS = ''

env3 = unit.get(unit.ENV3, unit.PORTA)
ncir = unit.get(unit.NCIR, unit.PORTA)
ultrasonic = unit.get(unit.ULTRASONIC, unit.PORTA)

def center(y, text, color):
    lcd.print(text, int(lcd.screensize()[0] / 2 - lcd.textWidth(text) / 2) - 1, y, color)

def stat_screen(title, value):
    lcd.clear()
    lcd.rect(0, 0, lcd.screensize()[0] - 1, 46, 0xFFFFFF, 0xFF0000)
    lcd.font(lcd.FONT_DejaVu24)
    center(12, title, 0xFFFFFF)
    lcd.font(lcd.FONT_DejaVu56)
    center(68, value, 0xFFFFFF)

def Fahrenheit(temperature):
    return temperature * 1.8 + 32

def publish_configuration(entity, name, device_class, unit_of_measurement):
    if device_class is not None:
        m5mqtt.publish("homeassistant/sensor/" + entity + "/config", json.dumps({"unique_id": MQTT_CLIENT + "_" + entity, "name": name, "unit_of_measurement": unit_of_measurement, "device_class": device_class, "state_topic": "homeassistant/sensor/" + entity + "/state"}).encode('utf-8'))
    else:
        m5mqtt.publish("homeassistant/sensor/" + entity + "/config", json.dumps({"unique_id": MQTT_CLIENT + "_" + entity, "name": name, "unit_of_measurement": unit_of_measurement, "state_topic": "homeassistant/sensor/" + entity + "/state"}).encode('utf-8'))

def publish_state(entity, state):
    m5mqtt.publish("homeassistant/sensor/" + entity + "/state", str(state))

def publish_states():
    publish_configuration("aerogarden_temperature", "AeroGarden Temperature", "temperature", chr(186) + "F")
    publish_configuration("aerogarden_humidity", "AeroGarden Humidity", "humidity", "%")
    publish_configuration("aerogarden_pressure", "AeroGarden Air Pressure", "pressure", "hPa")
    publish_configuration("aerogarden_water_temperature", "AeroGarden Water Temperature", "temperature", chr(186) + "F")
    publish_configuration("aerogarden_water_distance", "AeroGarden Water Distance", None, "mm")
    publish_configuration("aerogarden_water_level", "AeroGarden Water Level", None, "%")
    publish_configuration("aerogarden_battery_level", "AeroGarden Battery Level", "battery", "%")
    t = int(round(Fahrenheit(env3.temperature),0))
    if t < 1000:
        publish_state("aerogarden_temperature", t)
    publish_state("aerogarden_humidity", int(round(env3.humidity,0)))
    publish_state("aerogarden_pressure", int(round(env3.pressure / 100,0)))
    t = int(round(Fahrenheit(ncir.temperature),0))
    if t < 1000:
        publish_state("aerogarden_water_temperature", t)
    publish_state("aerogarden_battery_level", map_value(axp.getBatVoltage(), 3.7, 4.1, 0, 100))
    publish_state("aerogarden_water_distance", distance)
    publish_state("aerogarden_water_level", 100 - int(map_value(distance, 18, MAX_DISTANCE, 0, 100)))

def set_brightness(level):
    axp.setLcdBrightness(int(level))

def set_led(state):
    if state == "on":
        M5Led.on()
    else:
        M5Led.off()

wifiCfg.autoConnect(lcdShow=True)
m5mqtt = M5mqtt(MQTT_CLIENT, MQTT_HOST, MQTT_PORT, MQTT_USER, MQTT_PASS, 300)
m5mqtt.subscribe('aerogarden/brightness', set_brightness)
m5mqtt.subscribe('aerogarden/led', set_led)
m5mqtt.start()
setScreenColor(0x000000)
lcd.setRotation(1)

while True:
    stat_screen("Temperature", str(int(round(Fahrenheit(env3.temperature), 0))) + " F")
    wait(20)
    stat_screen("Humidity", str(int(round(env3.humidity, 0))) + " %")
    wait(20)
    distance = int(round(ultrasonic.distance,0))
    stat_screen("Water Level", str(100 - int(map_value(distance, 18, MAX_DISTANCE, 0, 100))) + " %")
    wait(20)
    publish_states()
