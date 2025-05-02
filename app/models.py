from . import app, db
from flask_sqlalchemy import SQLAlchemy

class View_books_with_authors_and_categories(db.Model):
    __tablename__ = 'View_books_with_authors_and_categories'
    book_id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    author_name = db.Column(db.String(255), nullable=False)
    author_image_url = db.Column(db.Text, nullable=False)
    category_name = db.Column(db.String(100), nullable=False)
    category_image_url = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'{self.book_id} : {self.title} : {self.description} : {self.price} : {self.image_url} : {self.category_name} : {self.author_name}: {self.created_at}'

    