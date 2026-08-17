class SerialHardware:
    """Hardware adapter that sends newline-delimited commands to a controller."""

    def __init__(self, port, baudrate=115200, timeout=2, serial_connection=None):
        if serial_connection is not None:
            self.serial = serial_connection
            return

        try:
            import serial
        except ImportError as error:
            raise RuntimeError("Install pyserial before using serial hardware: pip3 install pyserial") from error

        self.serial = serial.Serial(port, baudrate=baudrate, timeout=timeout)

    def move_to(self, destination: str):
        self._send_command(f"MOVE_TO {self._require_value('destination', destination)}")
        return f"[Robot] Moving to {destination}"

    def speak(self, text: str):
        self._send_command(f"SPEAK {self._require_value('text', text)}")
        return f"[Robot] Speaking: {text}"

    def pick_up(self, object_name: str):
        self._send_command(f"PICK_UP {self._require_value('object name', object_name)}")
        return f"[Robot] Picking up {object_name}"

    def stop(self):
        self._send_command("STOP")
        return "[Robot] Stopped"

    def close(self):
        self.serial.close()

    def _send_command(self, command: str):
        self.serial.write(f"{command}\n".encode("utf-8"))
        self.serial.flush()

        response = self.serial.readline().decode("utf-8").strip()
        if not response.startswith("OK"):
            raise RuntimeError(f"Robot controller rejected '{command}': {response or 'no response'}")

    @staticmethod
    def _require_value(name: str, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name.capitalize()} is required.")

        if "\n" in value or "\r" in value:
            raise ValueError(f"{name.capitalize()} must be a single line.")

        return value.strip()
