import random as rd
from tabnanny import check
from urllib import response
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

API_KEY = "d5958c5af12525faaf56e157ef3a55a9"


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    
## HTTP GET - Read Record

@app.route("/random", methods=['GET'])
def random():
    
    raw_data = db.session.query(Cafe).all()
    data = rd.choice(raw_data)
    
    return jsonify(cafe=data.to_dict())

@app.route("/all", methods=['GET'])
def all():
    
    raw_data = db.session.query(Cafe).all()
    
    data_dict = []
    
    for data in raw_data:
        data_dict.append(data.to_dict())
    
    return jsonify(all_cafes=data_dict)

@app.route("/search", methods=['GET'])
def search():
    
    query_location = request.args.get("loc")
    
    check = db.session.query(Cafe).filter(Cafe.location == query_location).all()
    
    if len(check) == 0:
        return jsonify(error={'Not found' : "sorry, we don't have cafe at that location"})
    
    return jsonify(cafes=[data.to_dict() for data in check])

## HTTP POST - Create Record

@app.route("/add", methods=["POST", "GET"])
def add_new_cafe():
    
    new_name = request.args.get("name")
    new_map_url = request.args.get("map_url")
    new_img_url = request.args.get("img_url")
    new_location = request.args.get("location")
    new_seats = request.args.get("seats")
    new_has_toilet = bool(request.args.get("has_toilet"))
    new_has_wifi = bool(request.args.get("has_wifi"))
    new_has_sockets = bool(request.args.get("has_sockets"))
    new_can_take_calls = bool(request.args.get("can_take_calls"))
    new_coffee_price = request.args.get("coffee_price")
    
    new_cafe = Cafe(
        name = new_name,
        map_url = new_map_url,
        img_url = new_img_url,
        location = new_location,
        seats = new_seats,
        has_toilet = new_has_toilet,
        has_wifi = new_has_wifi,
        has_sockets = new_has_sockets,
        can_take_calls = new_can_take_calls,
        coffee_price = new_coffee_price,
    )
    
    db.session.add(new_cafe)
    db.session.commit()
    
    return jsonify(response={"success" : "Succesfully added the new cafe"})

## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<id>", methods=["PATCH"])
def update_price(id):
    
    cafe = db.session.query(Cafe).filter(Cafe.id == id).first()
    
    if cafe:
        new_price = request.args.get("price")
        cafe.coffee_price = new_price   
        db.session.commit()
    
        return jsonify(success="Succesfully updated the price")
    else:
        return jsonify(error={"Not Found" : "Sorry a cafe with that id was not found"})

## HTTP DELETE - Delete Record

@app.route("/report-closed/<id>", methods=["DELETE"])
def report_closed(id):
    api_key = request.args.get("api-key")
    
    if api_key != API_KEY:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api-key")

    cafe = db.session.query(Cafe).filter(Cafe.id == id).first()
    
    if cafe:
        
        db.session.delete(cafe)
        db.session.commit()
        
        return jsonify(response={"success" : "The record was successfully deleted"})
    
    else:
        
        return jsonify(error={"Not Found" : "Sorry a cafe with that id was not found"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
