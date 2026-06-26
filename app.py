from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'novoafashion123'

productos = [
    {'id': 1, 'nombre': 'Crop 1', 'precio': 9.00, 'imagen': 'Crop 1.jpeg', 'categoria': 'Damas'},
    {'id': 2, 'nombre': 'Crop 2', 'precio': 35000, 'imagen': 'Crop 2.jpeg', 'categoria': 'Damas'},
    {'id': 3, 'nombre': 'Portada', 'precio': 45000, 'imagen': 'Portada.jpeg', 'categoria': 'Damas'},
]

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/Damas')
def damas():
    items = [p for p in productos if p['categoria'] == 'Damas']
    return render_template('Damas.html', productos=items)

@app.route('/Asimetrico')
def asimetrico():
    items = [p for p in productos if p['categoria'] == 'Asimetrico']
    return render_template('Asimetrico.html', productos=items)

@app.route('/Crops')
def crops():
    items = [p for p in productos if p['categoria'] == 'Crops']
    return render_template('Crops.html', productos=items)

@app.route('/Overzize')
def overzize():
    items = [p for p in productos if p['categoria'] == 'Overzize']
    return render_template('Overzize.html', productos=items)

@app.route('/agregar/<int:id>')
def agregar(id):
    carrito = session.get('carrito', [])
    carrito.append(id)
    session['carrito'] = carrito
    return redirect(url_for('index'))

@app.route('/carrito')
def carrito():
    ids = session.get('carrito', [])
    items = [p for p in productos for i in ids if p['id'] == i]
    total = sum(p['precio'] for p in items)
    return render_template('carrito.html', items=items, total=total)

if __name__ == '__main__':
    app.run(debug=True)