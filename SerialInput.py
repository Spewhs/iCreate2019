import json
import serial
from Travel import Travel


class SerialInput:
    def __init__(self, tty_name, player, threshold=50) -> None:
        super().__init__()
        self.ttyName = tty_name
        self.player = player
        try:
            self.arduinoSerialPort = serial.Serial(tty_name, 9600)
        except serial.serialutil.SerialException:
            print("Can't connect to tty")
        self.threshold = threshold
        self.travels = []

    def start(self) -> None:
        """
        Start the sketch
        """
        self._read_config_file()
        while True:
            self.process_input(self.arduinoSerialPort.readline())

    def _read_config_file(self) -> None:
        try:
            with open('configTravel.json') as travelConfigFile:
                travel_values = json.loads(travelConfigFile.read())
                for travel_value in travel_values:
                    start = travel_values[travel_value]['start']
                    end = travel_values[travel_value]['end']

                    travel = Travel((start['x'], start['y'], start['z']),
                                    (end['x'], end['y'], end['z']),
                                    travel_values[travel_value]['path'],
                                    travel_value
                                    )
                    self.travels.append(travel)

        except IOError:
            print("Can't read configTravel.json")

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
        for travel in self.travels:
            if travel.travel_name == activated_piezo:
                self.player.start(travel)
                return

