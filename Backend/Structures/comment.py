class comment:
    def __init__(self, id_user, id_game, text, name, date_event):
        self.__id_user = id_user
        self.__id_game = id_game
        self.__text = text
        self.__name = name
        self.__date_event = date_event

    # Getters
    def get_id_user(self):
        return self.__id_user

    def get_id_game(self):
        return self.__id_game

    def get_text(self):
        return self.__text

    def get_name(self):
        return self.__name

    def get_date_event(self):
        return self.__date_event

    # Setters
    def set_id_user(self, _id_user):
        self.__id_user = _id_user

    def set_id_game(self, _id_game):
        self.__id_game = _id_game

    def set_text(self, _text):
        self.__text = _text

    def set_name(self, _name):
        self.__name = _name

    def set_date_event(self, _date_event):
        self.__date_event = _date_event
