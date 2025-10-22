from abc import ABC, abstractmethod

from orders import Order


class User(ABC):
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @abstractmethod
    def get_password(self):
        return self.password

    @abstractmethod
    def change_password(self, value):
        self.password = value
        print("Password changed successfully.")


class Customer(User):
    def __init__(self, name, email, password, deposit) -> None:
        super().__init__(name, email, password)
        self.__deposit = deposit
        self.cart = Order()

    @property
    def deposit(self):
        return self.__deposit

    @deposit.setter
    def deposit(self, value):
        self.__deposit -= value

    @deposit.setter
    def add_deposit(self, value):
        if value > 0:
            self.__deposit += value
            print("New deposit added successfully.")
        else:
            print("Invalid amount.")

    def get_password(self):
        return super().get_password()

    def change_password(self, value):
        super().change_password(value)


class Seller(User):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
        self.__revenue = 0

    @property
    def revenue(self):
        return self.__revenue

    @revenue.setter
    def revenue(self, value):
        self.__revenue += value

    def add_new_product(self, store, product):
        store.list.add_product(product)

    def view_all_products(self, store):
        store.list.view_products()

    def delete_product(self, store, product):
        store.list.remove_product(product)

    def get_password(self):
        return super().get_password()

    def change_password(self, value):
        super().change_password(value)
