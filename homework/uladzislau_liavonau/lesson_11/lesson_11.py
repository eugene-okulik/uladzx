class Book:
    page_material = "бумага"
    test_exists = True
    ISBN = True
    book_is_reserved = False

    def __init__(self, book_name, book_author, page_quantity):
        self.book_name = book_name
        self.book_author = book_author
        self.page_quantity = page_quantity


class SchoolBook(Book):
    tasks_exist = True

    def __init__(self, book_name, book_author, page_quantity, subject, group):
        super().__init__(book_name, book_author, page_quantity)
        self.subject = subject
        self.group = group


sotnikov = Book("Сотников", "В.Быков", 345)
sotnikov.book_is_reserved = True

novaya_ziamlia = Book("Новая земля", "Я.Колас", 400)
ludi_na_bolote = Book("Люди на болоте", "И.Мележ", 350)
master_i_margarita = Book("Мастер и Маргарита", "М.Булгаков", 500)
lotr = Book("Властелин колец", "Д.Толкиен", 850)

books_list = [sotnikov, novaya_ziamlia, ludi_na_bolote, master_i_margarita, lotr]
for i in books_list:
    reserved_info = ", зарезервирована" if i.book_is_reserved else ""
    print(
        f'Название: {i.book_name}, Автор: {i.book_author}, '
        f'страниц: {i.page_quantity}, материал: {i.page_material}{reserved_info}'
    )

algebra = SchoolBook(
    "Алгебра", "Иванов", 564, "Математика", "6"
)
history = SchoolBook(
    "История Беларуси", "Адамович", 350, "История", "11"
)
history.book_is_reserved = True

school_books_list = [algebra, history]
for i in school_books_list:
    reserved_info = ", зарезервирована" if i.book_is_reserved else ""
    print(
        f'Название: {i.book_name}, Автор: {i.book_author}, страниц: {i.page_quantity}, '
        f'предмет: {i.subject}, класс: {i.group}{reserved_info}'
    )
