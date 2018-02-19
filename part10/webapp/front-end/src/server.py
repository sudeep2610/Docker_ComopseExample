import requests 
import os
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

BOOK_API_SERVER = os.environ['BOOK_API_SERVER']
app = Flask(__name__)

@app.route('/')
def show_books():
    Books = requests.get(BOOK_API_SERVER + "/books").json()
    return render_template('show_books.html', books=Books)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        return render_template('add_book.html')

    json = {
            'title': request.form.get('title'),
            'author': request.form.get('author')
    }

    response = requests.post(BOOK_API_SERVER + "/create_book", json=json)
    
    if response.status_code == 200:
        return show_books()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')