from app import app
from flask import render_template, redirect, request



@app.route('/', methods=('GET','POST'))
def home():
    return render_template('index.html')


@app.route('/books', methods=('GET','POST'))
def book():
    if request.method == "POST":
        return redirect('/books/{}'.format(request.form.get('books')))
        print(request.form.get('books'))
    return render_template('books.html')

@app.route('/salesman', methods=('GET','POST'))
def salesman():
    if request.method == "POST":
        print(request.form.get('salesman'))
        return redirect('/salesman/{}'.format(request.form.get('salesman')))
        
    return render_template('salesman.html')


@app.route('/stores', methods=('GET','POST'))
def stores():
    if request.method == "POST":
        print(request.form.get('store'))
        return redirect('/stores/{}'.format(request.form.get('address')))
    return render_template('stores.html')