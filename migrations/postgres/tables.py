from sqlalchemy import Column, DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import INTEGER, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import expression, func

from backend.core.constants import UserRole


Base = declarative_base()
metadata = Base.metadata

class DimRole(Base):
    """User roles table"""
    __table_args__ = {"schema": "portal"}
    __tablename__ = 'dim_role'

    id = Column(INTEGER, primary_key=True)
    name = Column(Enum(UserRole, values_callable=lambda enum: [e.value for e in enum]), nullable=False)
    description = Column(Text)


class DimUser(Base):
    """Users table"""
    __table_args__ = {"schema": "portal"}
    __tablename__ = 'dim_user'

    id = Column(INTEGER, primary_key=True)
    username = Column(String(64), nullable=False, unique=True)
    password_hash = Column(String(1024), nullable=False)
    name = Column(String(256))
    email = Column(String(256))
    is_active = Column(BOOLEAN, server_default=expression.true(), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


class MapUserRole(Base):
    """Mapping users and roles table"""
    __table_args__ = {"schema": "portal"}
    __tablename__ = 'map_user_role'

    id = Column(INTEGER, primary_key=True)
    role_id = Column(INTEGER, ForeignKey(DimRole.id))
    user_id = Column(INTEGER, ForeignKey(DimUser.id))
