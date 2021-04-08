import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class searchProductData:

    @staticmethod
    def searchProduct():
        ProductCode=config.get('Parameters', 'ProductCode')
        return ProductCode
