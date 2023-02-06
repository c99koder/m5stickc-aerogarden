# M5StickC-Plus AeroGarden

Monitor the status of an [AeroGarden](https://www.aerogarden.com/) in [Home Assistant](http://home-assistant.io/) using a [M5StickC-Plus microcontroller](https://docs.m5stack.com/en/core/m5stickc_plus) and [ESPHome](https://esphome.io).

![AeroGarden](github/aerogarden.jpg)
![M5StickC-Plus](github/m5stickcplus.jpg)

## Hardware

* AeroGarden Sprout LED
* [M5StickC-Plus microcontroller](https://docs.m5stack.com/en/core/m5stickc_plus)
* [M5Stack ENV III](https://docs.m5stack.com/en/unit/envIII) environmental sensor
* [M5Stack NCIR](https://docs.m5stack.com/en/unit/ncir) IR temperature sensor

Sensors are mounted under the grow platform, facing down towards the water.

## Software

Build and deploy the firmware using the ESPHome dashboard or from the command line:

```sh
esphome run aerogarden.yaml
```

## Home Assistant

Home Assistant automatically discovers the sensors using [MQTT Discovery](https://www.home-assistant.io/docs/mqtt/discovery/).  I created 2 helper entities to control the LCD backlight and LED.  The helper entity states are published to MQTT topics using [Node-RED](https://nodered.org/).  Home Assistant automations can be used to turn the LCD off during the night, or turn the LED on when the water level is low.

![HomeAssistant](github/homeassistant.png)

## Previous Version

The previous version of this project has been moved to the [UIFlow](/c99koder/m5stickc-aerogarden/tree/UIFlow) branch.

## License

Copyright (C) 2023 Sam Steele. Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
