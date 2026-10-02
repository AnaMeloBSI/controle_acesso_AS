from flask import abort
from flask_restful import Resource
from loja.model import Product

class ProductResource(Resource):
    def get(self, product_id=None):
        if product_id:
            product = Product.query.get_or_404(product_id)
            return {
                "id": product.id,
                "name": getattr(product, "name", str(product.id)),
                "description": product.description,
                "price": product.price,
            }
        
        products = Product.query.all()
        if not products:
            abort(204)

        return {
            "products": [
                {
                    "id": product.id,
                    "name": getattr(product, "name", str(product.id)),
                    "description": product.description,
                    "price": product.price,
                }
                for product in products
            ]
        }