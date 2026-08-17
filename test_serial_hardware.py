from brain.implementations.serial_hardware import SerialHardware


class FakeSerial:
    def __init__(self):
        self.commands = []
        self.responses = [b"OK\n", b"OK\n", b"OK\n", b"OK\n"]

    def write(self, command):
        self.commands.append(command.decode("utf-8"))

    def flush(self):
        pass

    def readline(self):
        return self.responses.pop(0)

    def close(self):
        pass


fake_serial = FakeSerial()
robot = SerialHardware(port="fake", serial_connection=fake_serial)

assert robot.move_to("kitchen") == "[Robot] Moving to kitchen"
assert robot.speak("Hello") == "[Robot] Speaking: Hello"
assert robot.pick_up("cup") == "[Robot] Picking up cup"
assert robot.stop() == "[Robot] Stopped"
assert fake_serial.commands == [
    "MOVE_TO kitchen\n",
    "SPEAK Hello\n",
    "PICK_UP cup\n",
    "STOP\n",
]

print("Serial hardware adapter test passed.")
