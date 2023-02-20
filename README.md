# M5StickC-Plus AeroGarden

Monitor the status of an [AeroGarden](https://www.aerogarden.com/) in [Home Assistant](http://home-assistant.io/) using a [M5StickC-Plus microcontroller](https://docs.m5stack.com/en/core/m5stickc_plus) and [ESPHome](https://esphome.io).

![AeroGarden](github/aerogarden.jpg)
![M5StickC-Plus](github/m5stickcplus.jpg)

## Hardware

* AeroGarden Sprout LED
* [M5StickC-Plus microcontroller](https://docs.m5stack.com/en/core/m5stickc_plus)
* [M5Stack ENV III](https://docs.m5stack.com/en/unit/envIII) environmental sensor ([SHT30](https://esphome.io/components/sensor/sht3xd.html), [QMP6988](https://esphome.io/components/sensor/qmp6988.html))
* [M5Stack NCIR](https://docs.m5stack.com/en/unit/ncir) IR temperature sensor ([MLX90614](https://github.com/3gyptian/esphome-mlx90614-i2c_IR_temp_sensor))
* [M5Stack TVOC](https://docs.m5stack.com/en/unit/tvoc) TVOC/eCO2 sensor ([SGP30](https://esphome.io/components/sensor/SGP30.html))
* [Adafruit VL6180X](https://www.adafruit.com/product/3316) Time of flight distance sensor ([VL6180X](https://github.com/exxamalte/esphome-customisations/tree/master/vl6180x))

Sensors are mounted under the grow platform, facing down towards the water.

## Software

Install the required git submodules:

```sh
git submodule init
git submodule update
```

Build and deploy the firmware using the ESPHome dashboard or from the command line:

```sh
esphome run aerogarden.yaml
```

## Home Assistant

Home Assistant automatically discovers the sensors when the device connects to the network.  I created a helper entity to control the LCD backlight.  Home Assistant automations can be used to turn the LCD off during the night or adjust the level based on ambient room lighting. Pressing the button on the front of the device resets the plant food timestamp.

![HomeAssistant](github/homeassistant.png)

## Previous Version

The previous version of this project has been moved to the [UIFlow](https://github.com/c99koder/m5stickc-aerogarden/tree/UIFlow) branch.

## License

Copyright (C) 2023 Sam Steele. Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
