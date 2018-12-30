from source.config_reader import ConfigReader

config = ConfigReader()

print(config.config_get("db_connect", 'db_file_path'))


