import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        base_url = config.get('common info', 'base_url')
        return base_url
    @staticmethod
    def getusername():
        username = config.get('common info', 'username')
        return username
    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password
