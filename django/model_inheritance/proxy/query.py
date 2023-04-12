from multi_table.models import Book, MyBook


# tables create:
#    - book

# book tabel
# id  | title | price

# ----------------------------------------

Book.objects.create(title="b1", price=1000)
# <Book: Book object (1)>

# book tabel
# id  | title | price
#  1  | b1    | 1000

# ----------------------------------------

MyBook.objects.create(title="b2", price=2000)
# <MyBook: MyBook object (2)>

# book tabel
# id  | title | price
#  1  | b1    | 1000
#  2  | b2    | 2000

MyBook.objects.create(title="b3", price=500)
# <MyBook: MyBook object (3)>

# book tabel
# id  | title | price
#  1  | b1    | 1000
#  2  | b2    | 2000
#  3  | b3    | 500

# ----------------------------------------

# book proxy
MyBook.objects.all()
# <QuerySet [<MyBook: b3 - 500>, <MyBook: b1 - 1000>, <MyBook: b2 - 2000>]>

# book
Book.objects.all()
# <QuerySet [<Book: b1 - 1000>, <Book: b2 - 2000>, <Book: b3 - 500>]>
