class Book:
    def __init__(self, title, author, year, num_pages):
        self.title = title
        self.author = author
        self.year = year
        self.num_pages = num_pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"num_pages: {self.num_pages}")

    def update_num_pages(self, new_num_pages):
        self.num_pages = new_num_pages

    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}, {self.num_pages} pages"

# Создание экземпляров класса "Книга"
Book1 = Book("Demons", "Dostoevsky", 1872, 768)
Book2 = Book("Captain's daughter", "Pushkin", 1836, 352)
Book3 = Book("Hero of our time", "Lermontov", 1840, 224)

# Тестирование методов
print("Book 1:")
Book1.display_info()
Book1.update_num_pages(240)
print(Book1)

print("\nBook 2:")
Book2.display_info()
Book2.update_num_pages(238)
print(Book2)

print("\nBook 3:")
Book3.display_info()
Book3.update_num_pages(350)
print(Book3)


