from typing import Any, Dict

from sqlalchemy.ext.declarative import as_declarative, declared_attr

class_registry: Dict = {}


@as_declarative(class_registry=class_registry)
class BaseModel:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        # UserModel -> user
        return (
            cls.__name__[:-5].lower()
            if cls.__name__.endswith("Model")
            else cls.__name__.lower()
        )
