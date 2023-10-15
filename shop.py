# Словарь с информацией о товарах
shop_menu = {
    "Товар 1": {"цена": 10, "осталось": 10},
    "Товар 2": {"цена": 20, "осталось": 0},
    "Товар 3": {"цена": 30, "осталось": 1}
}

# Словарь для корзины
cart = {}


# Функция для отображения меню магазина
def show_menu(menu):
    print("Меню магазина:")
    for item, info in menu.items():
        print(f"{item} - Цена: ${info['цена']}, осталось: {info['осталось']}")


# Функция для выбора товара пользователем
def get_user_choice(menu):
    choice = input("Выберите товар (введите название): ")
    return choice


# Функция для расчета общей стоимости товара
def calculate_total_price(item, quantity):
    price = shop_menu[item]["цена"]
    stock = shop_menu[item]["осталось"]

    if stock >= quantity:
        return price * quantity
    else:
        print("Извините, товара не хватает.")
        return 0


# Функция для размещения заказа
def place_order():
    item = get_user_choice(shop_menu)
    if item in shop_menu:
        quantity = int(input("Введите количество единиц товара: "))
        total_price = calculate_total_price(item, quantity)

        if total_price > 0:
            print("Ваш заказ размещен!")
            print(f"Общая стоимость заказа: ${total_price}")

            # Обновляем количество товара на складе
            shop_menu[item]["осталось"] -= quantity

            # Добавляем товар в корзину
            if item in cart:
                 cart[item] += quantity
            else:
                cart[item] = quantity
    else:
        print("Такого товара нет в меню.")


# Функция для проверки наличия товара на складе
def check_stock(item, quantity):
    stock = shop_menu.get(item, {}).get("осталось", 0)
    return stock >= quantity


# Функция для обновления количества товара на складе
def update_stock(item, quantity):
    shop_menu[item]["осталось"] -= quantity


# Функция для поиска товара по названию
def search_item(query):
    found_items = []
    for item in shop_menu:
        if query.lower() in item.lower():
            found_items.append(item)
    return found_items


# Функция для добавления товара в корзину
def add_to_cart():
    query = input("Введите название товара для добавления в корзину: ")
    found_items = search_item(query)

    if found_items:
        if len(found_items) == 1:
            item = found_items[0]
        else:
            print("Найдены следующие товары:")
            for i, found_item in enumerate(found_items, start=1):
                print(f"{i}. {found_item}")
            choice = int(input("Выберите номер товара: "))
            item = found_items[choice - 1]

        quantity = int(input(f"Введите количество единиц товара '{item}' для добавления в корзину: "))

        if check_stock(item, quantity):
            if item in cart:
                cart[item] += quantity
            else:
                cart[item] = quantity
            print(f"'{item}' добавлен в корзину.")
            update_stock(item, quantity)
        else:
            print("Извините, товара не хватает.")
    else:
        print("Товар не найден.")


# Функция для отображения корзины
def show_cart():
    print("Ваша корзина:")
    for item, quantity in cart.items():
        print(f"{item}: {quantity} единиц")


# Главная функция программы
def main():
    while True:
        print("Меню магазина:")
        print("1. Показать товары")
        print("2. Выбрать товар и разместить заказ")
        print("3. Поиск товара")
        print("4. Добавить товар в корзину")
        print("5. Показать корзину")
        print("6. Выйти из магазина")

        choice = input("Выберите действие (введите номер): ")

        if choice == "1":
            show_menu(shop_menu)
        elif choice == "2":
            place_order()
        elif choice == "3":
            query = input("Введите поисковый запрос: ")
            found_items = search_item(query)
            if found_items:
                print("Найдены следующие товары:")
                for i, found_item in enumerate(found_items, start=1):
                    print(f"{i}. {found_item}")
            else:
                print("Товары не найдены.")
        elif choice == "4":
            add_to_cart()
        elif choice == "5":
            show_cart()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

name = "main"
if name == "main":
    main()