from model import Base, Product, Cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))

def add_product(name,price,description,picture_link):
	product_object = Product(
	
	name=name,
	price=price,
	description=description,
	picture_link=picture_link)
	session.add(product_object)
	session.commit()

# add_product("vansclassic",49.99,"classics are always a good coice","https://images.vans.com/is/image/Vans/D3HY28-HERO?$583x583$")
# add_product("vansskatee",59.99,"idk","idek")
# add_product("vansskate",69.99,"go big or go home","https://scontent.fsdv3-1.fna.fbcdn.net/v/t1.0-9/p960x960/43669667_2233682956874144_6519654278225723392_o.jpg?_nc_cat=104&_nc_oc=AQnPzcQ2fFnewTls9d2Yk008yaA2pTQw1GewD0e7MjYw-FE8wuqkG-cGp1iCh1BalyY&_nc_ht=scontent.fsdv3-1.fna&oh=52ec0a02195e19d01909f5bd127d42cf&oe=5E4B7FC1")
# add_product("vansroses",49.99,"roses are red , vans are too!","https://i.etsystatic.com/19635589/r/il/6ce0f3/1808837432/il_570xN.1808837432_mk22.jpg")

def update_product_price(Id,price):
#ther or not they have finished the lab

   product_object = session.query(
       Product).filter_by(
       Id=Id)
   product_object.price = price
   session.commit()

update_product_price(1,39.99)


def delete_product(Id):
	session.query(Product).filter_by(
		Id=Id).delete()
	session.commit()



def query_all():

   products = session.query(Product).all()
   return products


#print(query_all())


def query_by_id(Id):
	product = session.query(
		Product).filter_by(
		Id=Id).first()
	return product
print(query_by_id(1))


def add_to_cart(Id):
	# cartproducte_object=Cart()
	cartproduct = Cart(productID = Id)
	session.add(cartproduct)

	session.commit()


