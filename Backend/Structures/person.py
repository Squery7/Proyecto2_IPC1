class person:
    def __init__(self, _id, _name, _last_name, _user, _password, _type):
        self.__id = _id
        self.__name = _name
        self.__last_name = _last_name
        self.__user = _user
        self.__password = _password
        self.__type = _type

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name

    def get_user(self):
        return self.__user

    def get_password(self):
        return self.__password

    def get_type(self):
        return self.__type

    # Setter
    def set_id(self, _id):  # Recommended not to change.
        if not isinstance(_id, int):
            print("Ingrese solo numeros por favor.")
            return
        self.__id = _id

    def set_name(self, _name):
        if _name != "":
            self.__name = _name

    def set_last_name(self, _last_name):
        if _last_name != "":
            self.__last_name = _last_name

    def set_user(self, _user):
        if _user != "":
            self.__user = _user

    def set_password(self, _password):
        if _password != "":
            self.__password = _password

    def set_type(self, _type):
        if _type != "":
            self.__type = _type
