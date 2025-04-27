### Tests (tests/test_inmemory_product_repository.py)
import unittest
from repositories.inmemory.inmemory_product_repository import InMemoryProductRepository
from models import Product

class TestInMemoryProductRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryProductRepository()
        self.product = Product(id="p1", name="Test Product", category_id="c1", supplier_id="s1", quantity=10)

    def test_save_and_find(self):
        self.repo.save(self.product)
        found = self.repo.find_by_id("p1")
        self.assertEqual(found.name, "Test Product")

    def test_find_all(self):
        self.repo.save(self.product)
        all_products = self.repo.find_all()
        self.assertEqual(len(all_products), 1)

    def test_delete(self):
        self.repo.save(self.product)
        self.repo.delete("p1")
        self.assertIsNone(self.repo.find_by_id("p1"))

if __name__ == '__main__':
    unittest.main()
