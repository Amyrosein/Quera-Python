from models import Product, User
from datetime import datetime


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        if self.products[product] < amount:
            raise Exception("Not Enough Products")
        else:
            self.products[product] = self.products[product] - amount
        if self.products[product] == 0:
            del self.products[product]

    def add_user(self, username):
        for user in self.users:
            if user.username == username:
                return None
        new_user = User(username)
        self.users.append(new_user)
        return str(new_user.username)

    def get_total_asset(self):
        s = 0
        for (key, value) in self.products.items():
            s += key.price * value
        return s

    def get_total_profit(self):
        s = 0
        for user in self.users:
            for item in user.bought_products:
                for it in self.products.keys():
                    if item == it.name:
                        s += it.price
        return s

    def get_comments_by_user(self, user):
        comments = []
        for key in self.products.keys():
            for cmt in key.comments:
                if cmt.user.username == user:
                    comments.append(cmt.text)
        return comments

    def get_inflation_affected_product_names(self):
        inflation_affected_products = []
        item_names = []
        for product in self.products.keys():
            item_names.append(product.name)
        item_set = set(item_names)
        for item in item_set:
            if item_names.count(item) > 1:
                inflation_affected_products.append(item)
        return inflation_affected_products

    def clean_old_comments(self, date):
        for key in self.products.keys():
            cmts = []
            for cmt in key.comments:
                if cmt.date_added >= date:
                    cmts.append(cmt)
            key.comments = cmts
            del cmts

    def get_comments_by_bought_users(self, product):
        cmts = []
        for user in self.users:
            for item in user.bought_products:
                if item == product:
                    for key in self.products.keys():
                        if key.name == product:
                            for cmt in key.comments:
                                if cmt.user.username == user.username:
                                    cmts.append(cmt.text)
        return cmts
