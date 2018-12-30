from source.config_reader import ConfigReader
import flask

import telebot



config = ConfigReader()

print(config.config_get("db_connect", 'db_file_path'))



