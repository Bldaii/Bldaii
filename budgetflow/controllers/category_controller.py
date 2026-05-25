from typing import Optional, List
from models.category import Category
from database.repositories.category_repo import CategoryRepository

class CategoryController:
    def __init__(self):
        self.repo = CategoryRepository()

    def get_all(self, type_: Optional[str] = None) -> List[Category]:
        filters = {}
        if type_:
            filters["type"] = type_
        return self.repo.get_all(filters)

    def get_by_id(self, id_: int) -> Optional[Category]:
        return self.repo.get_by_id(id_)

    def create(self, name: str, color: str, icon: str, type_: str) -> Category:
        cat = Category(
            id=None,
            name=name,
            color=color,
            icon=icon,
            type=type_
        )
        new_id = self.repo.create(cat)
        return self.repo.get_by_id(new_id)

    def update(self, cat: Category) -> bool:
        return self.repo.update(cat)

    def delete(self, id_: int) -> bool:
        return self.repo.delete(id_)
