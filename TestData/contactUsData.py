import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class contactUsData:

    @staticmethod
    def setSubjectHeading():
        Heading=config.get('Parameters', 'SubjectHeading')
        return Heading

    @staticmethod
    def setOrderReference():
        OrderReference = config.get('Parameters', 'Orderreference')
        return OrderReference

    @staticmethod
    def setProduct():
        Product = config.get('Parameters', 'Product')
        return Product

    @staticmethod
    def setMessage():
        message = config.get('Parameters', 'message')
        return message