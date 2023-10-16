from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import BaseModel


class UserModel(BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(256), nullable=True)
    surname = Column(String(256), nullable=True)
    email = Column(String, index=True, nullable=False)
    is_superuser = Column(Boolean, default=False)
    recipes = relationship(
        "UserModel",
        cascade="all,delete-orphan",
        back_populates="submitter",
        uselist=True,
    )

    # New addition
    hashed_password = Column(String, nullable=False)
