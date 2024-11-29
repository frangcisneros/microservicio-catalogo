from typing import List
from app import cache
from app.models import Product
from app.repositories import ProductRepository

repository = ProductRepository()


class ProductService:
    """Clase que se encarga de CRUD de productos"""

    def save(self, product: Product) -> Product:
        producto=repository.save(product)
        cache.set(f'product_{producto.id}',producto,timeout=15)
        return producto

    def update(self, product: Product, id: int) -> Product:
        return repository.update(product, id)

    def delete(self, id: int) -> None:
        product = repository.find(id)
        if product:
            repository.delete(product)

    def all(self) -> List[Product]:
        result=cache.get('products')
        if result is None:
            result=repository.all()
            cache.set('products',result,timeout=15)
        return result

    def get_product_by_id(self, id: int):
        result=cache.get(f'product_{id}')
        if result is None:
            result=repository.get_product_id(id)
            cache.set(f'product_{id}',result,timeout=15)
        return result

    def check_price(self, id: int) -> float:
        return repository.find(id).price

    def check_availability(self, id: int) -> bool:
        return repository.find(id).activated

    def check_availability_name(self, nombre: str) -> bool:
        return repository.find_by_name(nombre).activated

    def find(self, id: int) -> Product:
        """Busca un producto por su ID."""
        return repository.find(id)

    def find_by_name(self, nombre: str) -> Product:
        """Busca un producto por su nombre."""
        return repository.find_by_name(nombre)

    def find_by_price(self, precio: float) -> List[Product]:
        """Busca productos por su precio."""
        return repository.find_by_price(precio)

    def get_all_products(self) -> List[Product]:
        return repository.all()
