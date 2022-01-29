"""
Module: 'm5stack' on uiflow_stickc_plus v1.9.1
"""
# MCU: {'ver': 'v1.12', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.12.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.12.0', 'machine': 'M5StickC-Plus with ESP32', 'build': 'dirty', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any

def const(*args, **kwargs) -> Any:
    ...

node_id = '308398e2c5fc' # type: str
btnA : Any ## <class 'BtnChild'> = <BtnChild object at 3ffc41d0>
btnB : Any ## <class 'BtnChild'> = <BtnChild object at 3ffc4c20>
lcd : Any ## <class 'TFT'> = TFT   (Color mode: 24-bit, Clk=40000000 Hz)
Pins  (miso=19, mosi=23, clk=18, cs=14, dc=27, reset=33)
rtc : Any ## <class 'Bm8563'> = <Bm8563 object at 3ffc6510>
btn : Any ## <class 'Btn'> = <Btn object at 3ffc41c0>
timEx : Any ## <class 'TimerEx'> = <TimerEx object at 3ffc5040>
timerSch : Any ## <class 'timeSch'> = <timeSch object at 3ffc4de0>
def clear_imu_irq(*args, **kwargs) -> Any:
    ...


class Speaker():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def checkInit(self, *args, **kwargs) -> Any:
        ...

    def tone(self, *args, **kwargs) -> Any:
        ...

    def sing(self, *args, **kwargs) -> Any:
        ...

    def setBeat(self, *args, **kwargs) -> Any:
        ...

    def setVolume(self, *args, **kwargs) -> Any:
        ...

speaker : Any ## <class 'Speaker'> = <Speaker object at 3ffc5ea0>

class Axp192():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def deinit(self, *args, **kwargs) -> Any:
        ...

    def powerAll(self, *args, **kwargs) -> Any:
        ...

    def setLDO2State(self, *args, **kwargs) -> Any:
        ...

    def clearAllIRQ(self, *args, **kwargs) -> Any:
        ...

    CURRENT_100MA = 0 # type: int
    CURRENT_190MA = 1 # type: int
    CURRENT_280MA = 2 # type: int
    CURRENT_360MA = 3 # type: int
    CURRENT_450MA = 4 # type: int
    CURRENT_550MA = 5 # type: int
    CURRENT_630MA = 6 # type: int
    CURRENT_700MA = 7 # type: int
    def getChargeState(self, *args, **kwargs) -> Any:
        ...

    def setChargeState(self, *args, **kwargs) -> Any:
        ...

    def getBatVoltage(self, *args, **kwargs) -> Any:
        ...

    def getBatCurrent(self, *args, **kwargs) -> Any:
        ...

    def getVinVoltage(self, *args, **kwargs) -> Any:
        ...

    def getVinCurrent(self, *args, **kwargs) -> Any:
        ...

    def getVBusVoltage(self, *args, **kwargs) -> Any:
        ...

    def getVBusCurrent(self, *args, **kwargs) -> Any:
        ...

    def getTempInAXP192(self, *args, **kwargs) -> Any:
        ...

    def powerOff(self, *args, **kwargs) -> Any:
        ...

    def setLDO2Volt(self, *args, **kwargs) -> Any:
        ...

    def setLDO3Volt(self, *args, **kwargs) -> Any:
        ...

    def setLDO3State(self, *args, **kwargs) -> Any:
        ...

    def setLcdBrightness(self, *args, **kwargs) -> Any:
        ...

    def setChargeCurrent(self, *args, **kwargs) -> Any:
        ...

    def disableAllIRQ(self, *args, **kwargs) -> Any:
        ...

    def enableBtnIRQ(self, *args, **kwargs) -> Any:
        ...

    def btnState(self, *args, **kwargs) -> Any:
        ...

axp : Any ## <class 'Axp192'> = <Axp192 object at 3ffc4bb0>

class Bm8563():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def deinit(self, *args, **kwargs) -> Any:
        ...

    def setTime(self, *args, **kwargs) -> Any:
        ...

    def now(self, *args, **kwargs) -> Any:
        ...

M5Led : Any ## <class 'M5Led'> = <M5Led object at 3ffc6440>

class IR():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def deinit(self, *args, **kwargs) -> Any:
        ...

    def tx(self, *args, **kwargs) -> Any:
        ...

ir : Any ## <class 'IR'> = <IR object at 3ffc6120>
def remoteInit(*args, **kwargs) -> Any:
    ...

