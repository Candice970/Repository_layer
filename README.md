# Repository_layer
# Smart Inventory Management System - Repository Layer

## Repositories
- Used **Generics** to avoid duplication across entity repositories.
- CRUD operations abstracted via interfaces.

## In-Memory Implementation
- Simple **HashMap** (Python dict) based.

## Abstraction (Factory Pattern)
- Chose **Factory Pattern** for simplicity.
- `RepositoryFactory.get_product_repository("MEMORY")` returns a memory-based repo.

## Future Proofing
- Stub classes ready for future storage backends like **Database** or **FileSystem**.

## Testing
- Unit tests validate CRUD behavior of in-memory repositories.

## Class Diagram (Text version)
- Repository<T, ID>
  - ProductRepository
    - InMemoryProductRepository
    - DatabaseProductRepository (stub)
- RepositoryFactory
  - Returns appropriate repository implementation
