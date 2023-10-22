import json
from saleapp import app
import os


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_categories():
    return read_json(os.path.join(app.root_path, 'data/categories.json'))


def load_products(cate_id=None):
    products = read_json(os.path.join(app.root_path, 'data/products.json'))

    if cate_id:
        products = [p for p in products if p['category_id'] == int(cate_id)]

    return products
