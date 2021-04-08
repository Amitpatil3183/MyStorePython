import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url=config.get('Parameters', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('Parameters', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('Parameters', 'password')
        return password
