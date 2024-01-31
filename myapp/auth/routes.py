from flask import Blueprint,request,jsonify
from flask_jwt_extended import create_access_token ,jwt_required
from werkzeug.security import generate_password_hash,check_password_hash
from myapp.models import User
from myapp import db


auth = Blueprint("auth",__name__)

@auth.route("/login",methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password,password):
        token = create_access_token(identity=user.id)
        return jsonify({"message":"login successfull","token":token}),200
    else:
        return jsonify({"error":"login failed"}),400



@auth.route("/register",methods=["POST"])
def register():
    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")
    
    # validation here
    #
    #
    if not (username and email and password):
        return jsonify({"error":"username, email, password mandatory"}),400


    hashed_password= generate_password_hash(password=password)
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"error":"username alredy exists"}),409
    
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"error":"email alredy exists"}),409

    user = User(username=username,email=email,password=hashed_password)
    db.session.add(user)
    db.session.commit()

    user = {
        "user_id":user.id,
        "username":user.username,
        "email":user.email,
    }

    return jsonify({"message":"registration successful","user":user}),201