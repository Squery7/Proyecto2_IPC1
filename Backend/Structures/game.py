class game:
    def __init__(self, _id, _name, _year, _price, _categories, _photo, _banner, _description):
        self.__id = _id  # Game id
        self.__name = _name  # Name of the game
        self.__year = _year
        self.__price = _price  # Game price
        self.__categories = self.set_list_minus(_categories)  # List of categories => []
        self.__photo = _photo  # Game image
        self.__banner = _banner  # Game banner
        self.__description = _description  # Game description

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_price(self):
        return self.__price

    def get_categories(self):
        return self.__categories

    def get_photo(self):
        return self.__photo

    def get_banner(self):
        return self.__banner

    def get_description(self):
        return self.__description

    # Setters
    def set_id(self, _id):
        self.__id = _id

    def set_name(self, _name):
        self.__name = _name

    def set_year(self, _year):
        self.__year = _year

    def set_price(self, _price):
        self.__price = _price

    def set_categories(self, _categories):
        self.__categories = _categories

    def set_photo(self, _photo):
        self.__photo = _photo

    def set_banner(self, _banner):
        self.__banner = _banner

    def set_description(self, _description):
        self.__description = _description

    # Set categories
    def change_category(self, _category, _new_value):
        aux = self.set_list_minus([_category, _new_value])
        _category = aux[0]
        _new_value = aux[1]

        index = 0
        for temp in self.__categories:
            if temp == _category:
                self.__categories[index] = _new_value
                return True
            index += 1
        return False

    def add_category(self, _category):
        _category = self.set_list_minus([_category])[0]
        if _category not in self.__categories:
            self.__categories.append(_category)
            return True
        else:
            return False

    def add_categories(self, _categories):
        _categories = self.set_list_minus(_categories)
        non_repeat_gategories = []
        for temp in _categories:
            if temp not in self.__categories:
                non_repeat_gategories.append(temp)

        self.__categories.extend(non_repeat_gategories)

    def delete_category(self, _category):
        _category = self.set_list_minus([_category])[0]
        index = 0
        for temp in self.__categories:
            if temp == _category:
                self.__categories.pop(index)
                return True
            index += 1
        return False

    def delete_categories(self, _categories):
        _categories = self.set_list_minus(_categories)
        state_eliminations = []
        for category_delete in _categories:
            index = 0
            exists = False
            for category_exist in self.__categories:
                if category_delete == category_exist:
                    self.__categories.pop(index)
                    exists = True
                    break
                index += 1
            state_eliminations.append(exists)
        return state_eliminations

    def delete_all_categories(self):
        self.__categories.clear()

    def set_list_minus(self, _categories):
        for x, category in enumerate(_categories):
            _categories[x] = category.lower()
        return _categories
