from flask import Flask, render_template, request
from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_catalog.db'
db.init_app(app)

class BookCatalogModel:
    def add_book(self, book):
        new_book = Book(title=book)
        db.session.add(new_book)
        db.session.commit()

    def get_books(self):
        return Book.query.all()

    def edit_book(self, book_id, new_title):
        book = Book.query.get(book_id)
        if book:
            book.title = new_title
            db.session.commit()

    def delete_book(self, book_id):
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()

 
class BookCatalogView:
    def display_books(self, books):
        return books

class BookCatalogPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_book(self, book):
        self.model.add_book(book)
        books = self.model.get_books()
        return self.view.display_books(books)

@app.route("/", methods=["GET", "POST"])
def book_catalog():
    if request.method == "POST":
        if "add_book" in request.form:
            new_book = request.form["book"]
            result = presenter.add_book(new_book)
        elif "edit_book" in request.form:
            book_id = request.form["book_id"]
            new_title = request.form["new_title"]
            model.edit_book(book_id, new_title)
        elif "delete_book" in request.form:
            book_id = request.form["book_id"]
            model.delete_book(book_id)
    else:
        result = model.get_books()

    books = model.get_books()
    return render_template("book_catalog.html", books=books)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    model = BookCatalogModel()
    view = BookCatalogView()
    presenter = BookCatalogPresenter(model, view)

    app.run(debug=True, port=8082)
