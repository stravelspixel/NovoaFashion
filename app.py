from flask import Flask, render_template, session, redirect, url_for, request, jsonify

app = Flask(__name__)
app.secret_key = 'novoafashion123'

productos = [
    {'id': 1, 'nombre': 'Crop 1', 'precio': 25000, 'imagen': 'Crop 1.jpeg'},
    {'id': 2, 'nombre': 'Crop 2', 'precio': 35000, 'imagen': 'Crop 2.jpeg'},
    {'id': 3, 'nombre': 'Portada', 'precio': 45000, 'imagen': 'Portada.jpeg'},
]

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

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