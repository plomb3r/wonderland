import configparser
import os


class ConfigReader:
    config = None
    this_dir = os.path.dirname(__file__)
    filename = os.path.realpath("{0}/../resource/config.ini".format(this_dir))

    def __init__(self):
        self.read_config_to_mem()

    def config_get(self, key, value):
        data = self.config.get(key, value)
        return data

    def config_set(self, key, value, element):
        data = self.config.set(key, value, element)
        with open(self.filename, "w") as config_file:
            self.config.write(config_file)

    def read_config_to_mem(self):
        config = configparser.RawConfigParser()
        config.read(filenames=self.filename)
        self.config = config
