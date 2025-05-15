from annotated_types import Timezone
from sqlalchemy import Column, String, Integer, DateTime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, index = True, primary_key=True, autoincrement=True)
    email = Column(String, index = True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default="now()", nullable=False)