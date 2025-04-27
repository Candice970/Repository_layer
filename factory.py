### Factory Pattern (factories/repository_factory.py)
from repositories.inmemory.inmemory_product_repository import InMemoryProductRepository
# Future: from repositories.database.database_product_repository import DatabaseProductRepository

class RepositoryFactory:
    @staticmethod
    def get_product_repository(storage_type: str):
        if storage_type == "MEMORY":
            return InMemoryProductRepository()
        # elif storage_type == "DATABASE":
        #     return DatabaseProductRepository()
        else:
            raise ValueError("Unknown storage type")
