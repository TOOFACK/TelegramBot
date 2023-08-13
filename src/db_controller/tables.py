import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# class Settings(Base):
#     key = sa.Column(sa.String(length=255), primary_key=True)
#     value = sa.Column(sa.String(length=255), nullable=False)

#     __tablename__ = "settings"


class Content(Base):
    content_name = sa.Column(sa.String(length=255), primary_key=True)
    content_value = sa.Column(sa.String(length=1000), nullable=False)

    __tablename__ = "content"
