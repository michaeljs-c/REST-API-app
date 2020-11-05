from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, StoreList


app = Flask(__name__)
#Turns off flask SQL SQLAlchemy modification tracker, as SQLAlchemy already has one (and is better)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #can use mysql postgresql etc and they will work
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'key'
api = Api(app)


jwt = JWT(app, authenticate, identity)
# creates a new endpoint /auth
# send /auth a username and password
# jwt sends it to authenticate function
# auth end point returns jwt token
# send jwt token to next request we make
# on next request, jwt calls indentity function and gets correct user
# if successful, user was authenticated and jwt toekn was valid
# THEREFORE, logged in means - can you prove your indentity, i.e. can you provide a valid token which proves you are logged in.


#201: object created
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
