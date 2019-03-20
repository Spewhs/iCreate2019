import json
import serial


class SerialInput:
    def __init__(self, tty_name, player, threshold=50) -> None:
        super().__init__()
        self.ttyName = tty_name
        self.player = player
        self.arduinoSerialPort = serial.Serial(tty_name, 9600)
        self.threshold = threshold

    def start(self) -> None:
        """
        Start the sketch
        """
        #TODO Instanciate Travel
        while True:
            self.process_input(self.arduinoSerialPort.readline())

    def process_input(self, json_input) -> None:
        """
        Process the input of the arduino serial port select the highest value
        If the sensor is enough triggered
        :param json_input: key = tringered piezo, value = input of the piezo
        """
        input_data = json.loads(json_input)
        max_input_name = ""
        max_input_value = -1
        for piezo, value in input_data.items():
            if value > max_input_name:
                max_input_name = piezo
                max_input_value = value
        if max_input_value >= self.threshold and max_input_name > 0:
            self.select_instance(max_input_name)

    def select_instance(self, activated_piezo) -> None:
        """
        Try to trigger sequence
        :param activated_piezo:
        :return:
        """
        print(activated_piezo)
        # self.player.star()

