from typing import Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.recipe import RecipeModel
from app.schemas.recipe import RecipeCreate, RecipeUpdate, RecipeUpdateRestricted


class CRUDRecipe(CRUDBase[RecipeModel, RecipeCreate, RecipeUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: RecipeModel,
        obj_in: Union[RecipeUpdate, RecipeUpdateRestricted]
    ) -> RecipeModel:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj


recipe = CRUDRecipe(RecipeModel)
