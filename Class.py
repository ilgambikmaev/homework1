class Product:
    def __init__(self, product_id, name, price, rating, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.rating = rating
        self.stock_quantity = stock_quantity

    def add_stock(self, quantity):
        self.stock_quantity += quantity

    def remove_stock(self, quantity):
        if quantity <= self.stock_quantity:
            self.stock_quantity -= quantity
        else:
            print("Not enough stock available.")

    def update_rating(self, new_rating):
        self.rating = new_rating

    def update_price(self, new_price):
        self.price = new_price


class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_item(self, product):
        self.products.append(product)

    def remove_item(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            print("Product not found in the category.")

    def get_item(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        print("Product not found in the category.")
        return None


class Basket:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)
        else:
            print("Product not found in the basket.")

    def get_item(self, product_id):
        for product in self.items:
            if product.product_id == product_id:
                return product
        print("Product not found in the basket.")
        return None

    def make_purchase(self):
        if not self.items:
            print("Basket is empty.")
            return

        print("Purchased items:")
        for product in self.items:
            print(product.name)
        self.items = []


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.basket = Basket()


# Пример использования:

# Создаем несколько товаров
product1 = Product(1, "Laptop", 1000, 4.5, 10)
product2 = Product(2, "Smartphone", 500, 4.0, 20)

# Создаем категории и добавляем товары в категории
category1 = Category("Electronics")
category1.add_item(product1)
category1.add_item(product2)

# Создаем пользователя и добавляем товары в корзину
user1 = User("user1", "password1")
user1.basket.add_item(product1)
user1.basket.add_item(product2)

# Покупаем товары из корзины
user1.basket.make_purchase()

# Обновляем рейтинг товара
product1.update_rating(4.8)

# Выводим информацию о товаре в категории
item = category1.get_item(1)
if item:
    print(f"Продукт {item.name} в категории {category1.name}: Цена - {item.price}, Рейтинг - {item.rating}")






