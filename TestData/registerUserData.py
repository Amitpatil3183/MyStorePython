import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class registerUserData:

    @staticmethod
    def setCustFname():
        CustFname=config.get('Parameters', 'CustFname')
        return CustFname

    @staticmethod
    def setCustLname():
        CustLname = config.get('Parameters', 'CustLname')
        return CustLname

    @staticmethod
    def setCustPwd():
        CustPwd = config.get('Parameters', 'CustPwd')
        return CustPwd

    @staticmethod
    def setAddressFname():
        AddressFname = config.get('Parameters', 'AddressFname')
        return AddressFname

    @staticmethod
    def setAddressLname():
        AddressLname = config.get('Parameters', 'AddressLname')
        return AddressLname

    @staticmethod
    def setAddress1():
        Address1 = config.get('Parameters', 'Address1')
        return Address1

    @staticmethod
    def setCity():
        City = config.get('Parameters', 'City')
        return City

    @staticmethod
    def selectState():
        State = config.get('Parameters', 'State')
        return State

    @staticmethod
    def setZip():
        Zip = config.get('Parameters', 'Zip')
        return Zip

    @staticmethod
    def setHomePhone():
        HomePhone = config.get('Parameters', 'HomePhone')
        return HomePhone

    @staticmethod
    def setAliasAdd():
        AliasAdd = config.get('Parameters', 'AliasAdd')
        return AliasAdd







