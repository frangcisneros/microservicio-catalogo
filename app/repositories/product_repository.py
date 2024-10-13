from typing import List, Optional
from app.models import Product
from app import db


class ProductRepository:
    """Repository for managing Product entities."""

    def save(self, product: Product) -> Product:
        """Guarda un nuevo producto en la base de datos."""
        db.session.add(product)
        db.session.commit()
        return product

    def update(self, product: Product, id: int) -> Optional[Product]:
        """Actualiza un producto existente en la base de datos."""
        entity = self.find(id)
        if entity is None:
            return None
        entity.name = product.name
        entity.price = product.price
        entity.activated = product.activated

        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, product: Product) -> None:
        """Elimina un producto de la base de datos."""
        db.session.delete(product)
        db.session.commit()

    def all(self) -> List[Product]:
        """Devuelve una lista de todos los productos en la base de datos."""
        return db.session.query(Product).all()

    def get_product_id(self, id: int) -> Optional[Product]:
        """Busca un producto por su ID y que esté activo (activo = true)."""
        return (
            db.session.query(Product)
            .filter(Product.id == id, Product.activated == True)
            .first()
        )

    def find(self, id: int) -> Optional[Product]:
        """Busca un producto por su ID."""
        if id is None:
            return None
        try:
            return db.session.query(Product).filter(Product.id == id).one()
        except Exception:
            return None

    def find_by_name(self, name: str) -> Optional[Product]:
        """Busca un producto por su nombre."""
        return db.session.query(Product).filter(Product.name == name).first()

    def find_by_price(self, price: float) -> List[Product]:
        """Busca productos por su precio."""
        return db.session.query(Product).filter(Product.price == price).all()
