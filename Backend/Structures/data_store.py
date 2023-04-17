from Structures.users import users
from Structures.products import products


class data_store:
    __instance = None

    def __init__(self):
        if data_store.__instance != None:
            raise Exception(
                "The class data_store only allows for one instance.")
        else:
            data_store.__instance = self
            self.__users = users()
            self.__products = products()

    @staticmethod
    def get_instance():
        if data_store.__instance == None:
            data_store()
        return data_store.__instance

    def get_products(self):
        return self.__products

    def get_users(self):
        return self.__users
