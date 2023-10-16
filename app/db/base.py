# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import BaseModel  # noqa
from app.models.recipe import RecipeModel  # noqa
from app.models.user import UserModel  # noqa
