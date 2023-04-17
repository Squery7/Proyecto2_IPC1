from Structures.person import person


class users:
    def __init__(self):
        self.__users = [
            person(0, "admin", "admin", "admin", "@dm!n1234", "administrator")]

    def create(self, _values): # _values={"_id": "", "_name": "", "_last_name": "", "_user": "", "_password": "", "_type": ""}
        new_person = person(_values["_id"], _values["_name"], _values["_last_name"], _values["_user"], _values["_password"], _values["_type"])
        if self.exist(new_person.get_id()):
            return {
                "status": "error",
                "msg": "The user already exists.",
                "user": None
            }
        else:
            self.__users.append(new_person)
            return {
                "status": "success",
                "msg": "The user was created successfully.",
                "user": new_person
            }

    def read(self, _id):
        user = self.exist(_id)
        if user is not None:
            return {
                "status": "success",
                "msg": "This is the user",
                "user": user
            }
        else:
            return {
                "status": "error",
                "msg": "The user does not exist.",
                "user": user
            }

    def update(self, _id, _values):
        user = self.exist(_id)
        if user is not None:
            for i, user in enumerate(self.__users):
                if _id == user.get_id():
                    self.__users[i].set_name(_values["_name"])
                    self.__users[i].set_last_name(_values["_last_name"])
                    self.__users[i].set_user(_values["_user"])
                    self.__users[i].set_password(_values["_password"])
                    self.__users[i].set_type(_values["_type"])
                    return {
                        "status": "success",
                        "msg": "The changes were updated successfully.",
                        "user": self.__users[i]
                    }
        else:
            return {
                "status": "error",
                "msg": "The user does not exist.",
                "user": user
            }

    def delete(self, _id):
        for i, user in enumerate(self.__users):
            if _id == user.get_id():
                return {
                    "status": "success",
                    "msg": "The user was eliminated successfully.",
                    "user": self.__users.pop(i)
                }
        return {
            "status": "error",
            "msg": "The user does not exist.",
            "user": None
        }
    
    def login(self, _user, _password):
        for user in self.__users:
            if user.get_user() == _user:
                if user.get_password() == _password:
                    return {
                        "status":"success",
                        "msg":"Welcome " + _user,
                        "user": user
                    }
                else:
                    return {
                        "status":"error",
                        "msg":"Incorrect password.",
                        "user": None
                    }
        return {
            "status":"error",
            "msg":"The user does not exist.",
            "user": None
        }

    def register(self, _values):
        return self.create(_values)

    def exist(self, _id):
        for user in self.__users:
            if _id == user.get_id():
                return user
        return None
