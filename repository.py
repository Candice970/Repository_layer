### Repository Interface (repositories/repository.py)
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')
ID = TypeVar('ID')

class Repository(ABC, Generic[T, ID]):
    @abstractmethod
    def save(self, entity: T) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        pass

    @abstractmethod
    def delete(self, id: ID) -> None:
        pass

### Entity-specific Interfaces (repositories/product_repository.py, etc.)
from .repository import Repository
from models import Product, Category, Supplier, Order, User, InventoryLog

class ProductRepository(Repository[Product, str]):
    pass

class CategoryRepository(Repository[Category, str]):
    pass

class SupplierRepository(Repository[Supplier, str]):
    pass

class OrderRepository(Repository[Order, str]):
    pass

class UserRepository(Repository[User, str]):
    pass

class InventoryLogRepository(Repository[InventoryLog, str]):
    pass
