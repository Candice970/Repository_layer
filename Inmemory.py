### In-Memory Implementations (repositories/inmemory/inmemory_product_repository.py, etc.)
class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self._storage = {}

    def save(self, product: Product) -> None:
        self._storage[product.id] = product

    def find_by_id(self, id: str) -> Optional[Product]:
        return self._storage.get(id)

    def find_all(self) -> List[Product]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
