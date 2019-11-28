from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
   __tablename__ = 'products'
   Id = Column(Integer, primary_key=True)
   name = Column(String)
   price = Column(Float)
   description = Column(String)
   picture_link = Column(String)


class Cart(Base):
	 __tablename__ = 'cart'
	 productID = Column(Integer, primary_key=True)
	
