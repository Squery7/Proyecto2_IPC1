from Structures.game import game


class products:
    def __init__(self):
        self.__products = []

    def create(self, _values):
        new_game = game(_values["_id"], _values["_name"],  _values["_year"], _values["_price"],
                        _values["_categories"], _values["_photo"], _values["_banner"], _values["_description"])
        game = self.exists(new_game.get_id())
        if game is not None:
            return {
                "status": "error",
                "msg": "The id is already exists.",
                "game": None
            }
        self.__products.append(new_game)
        return {
            "status": "success",
            "msg": "The product was created successfully.",
            "game": new_game
        }

    def read(self, _id):
        game = self.exists(_id)
        if game is None:
            return {
                "status": "error",
                "msg": "The game does not exist.",
                "game": None
            }
        return {
            "status": "success",
            "msg": "This is the game.",
            "game": game
        }

    def update(self, _id, _values):
        game = self.exists(_id)
        if game is not None:
            for i, product in enumerate(self.__products):
                if _id == product.get_id():
                    self.__products[i].set_name(_values["_name"])
                    self.__products[i].set_year(_values["_year"])
                    self.__products[i].set_price(_values["_price"])
                    self.__products[i].set_price(_values["_categories"])
                    self.__products[i].set_photo(_values["_photo"])
                    self.__products[i].set_banner(_values["_banner"])
                    self.__products[i].set_description(_values["_description"])
                    return {
                        "status": "success",
                        "msg": "The changes were updated successfully.",
                        "game": self.__products[i]
                    }
        else:
            return {
                "status": "error",
                "msg": "The game does not exist.",
                "game": None
            }

    def delete(self, _id):
        user = self.exists(_id)
        if user is not None:
            for i, product in enumerate(self.__products):
                if product.get_id() == _id:
                    return {
                        "status": "error",
                        "msg": "The user does not exist.",
                        "user": self.__products.pop(i)
                    }
        else:
            return {
                "status": "error",
                "msg": "The user does not exist.",
                "user": None
            }

    def exists(self, _id):
        for product in self.__products:
            if product.get_id() == _id:
                return product
        return None
