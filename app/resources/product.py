from flask import Blueprint, request, jsonify
from app.services import ProductService
from app.models import Product


product = Blueprint("product", __name__)
product_service = ProductService()


@product.route("/", methods=["GET"])
def home():
    return "ya algo funciona", 200


@product.route("/create_product", methods=["POST"])
def create_product():
    id = request.json.get("id", None)
    name = request.json.get("name", None)
    price = request.json.get("price", None)
    activated = request.json.get("activated", None)

    service = ProductService()
    product = Product(id=id, name=name, price=price, activated=activated)

    if service.save(product):
        return {"message": "Producto Creado Correctamente"}, 200
    return {"message": "Error al Crear Producto"}, 400


@product.route("/get_product/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = product_service.get_product_by_id(product_id)
    data = [
        {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "activated": product.activated,
        }
    ]
    if product:
        return jsonify(data), 200
    return "Producto no encontrado", 404


@product.route("/delete_product/<int:product_id>", methods=["DELETE"])
def delete_producto(product_id):
    product_service.delete(product_id)
    return "Producto eliminado", 200


@product.route("/product/check_price/<int:product_id>", methods=["GET"])
def check_price(product_id):
    price = product_service.check_price(product_id)
    return {"price": price}, 200
