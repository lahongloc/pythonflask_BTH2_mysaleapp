from saleapp import app
from flask import render_template, request
import utils


@app.route('/')
def home():
    cates = utils.load_categories()
    return render_template("index.html", categories=cates)


@app.route('/products')
def products_list():
    cate_id = request.args.get('category_id')

    prods = utils.load_products(cate_id=cate_id)
    kw = request.args.get('keyword')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')

    if kw:
        prods = [p for p in prods if p['name'].lower().find(kw.lower()) >= 0]

    if to_price and from_price:
        prods = [p for p in prods if float(from_price) <= p['price'] <= float(to_price)]
    elif from_price:
        prods = [p for p in prods if float(from_price) <= p['price']]
    elif to_price:
        prods = [p for p in prods if p['price'] <= float(to_price)]

    return render_template('products.html', products=prods)


@app.route('/products/<product_id>')
def product_details(product_id):
    prods = utils.load_products()
    current_product = {}

    for p in prods:
        if p['id'] == int(product_id):
            current_product = p

    return render_template('details.html', current_product=current_product)


if __name__ == '__main__':
    app.run(debug=True)
