# Real Hardware Setup

NOUS uses `DummyHardware` by default. It only connects to a real controller when
both environment variables below are set:

```bash
pip3 install pyserial
NOUS_HARDWARE=serial NOUS_SERIAL_PORT=/dev/ttyUSB0 python3 -m brain.main
```

Replace `/dev/ttyUSB0` with the serial device for your ESP32. On macOS it often
looks like `/dev/cu.usbserial-*` or `/dev/cu.SLAB_USBtoUART`.

The ESP32 must reply with a line beginning with `OK` for each command:

```text
MOVE_TO kitchen
SPEAK hello
PICK_UP cup
STOP
```

`STOP` must disable the motor driver in ESP32 firmware. Test with wheels raised
off the ground first, and use a physical emergency-stop switch that cuts motor
power. `MOVE_TO` and `PICK_UP` need additional navigation and arm firmware
before they can move real hardware safely.
