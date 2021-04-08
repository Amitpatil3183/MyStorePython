import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class createOrderData:

    @staticmethod
    def setDressSize():
        DressSize=config.get('Parameters', 'DressSize')
        return DressSize

    @staticmethod
    def setAddressComment():
        AddComment = config.get('Parameters', 'AddressComment')
        return AddComment