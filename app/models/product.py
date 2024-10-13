from dataclasses import dataclass
from app import db


class Product(db.Model):
    __tablename__ = "products"

    # Definición de los atributos del modelo
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(255), nullable=False)
    price: float = db.Column(db.Float, nullable=False)
    activated: bool = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, id=None, name=None, price=None, activated=None):
        self.id = id
        self.name = name
        self.price = price
        self.activated = activated
