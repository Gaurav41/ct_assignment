from flask import Blueprint, abort, jsonify,request

from myapp import db

error = Blueprint("error",__name__)

@error.app_errorhandler(400)
def error_400(e):
    print(e)
    return jsonify({"Error":"Bad Request"}),400


@error.app_errorhandler(404)
def error_404(e):
    print(e)
    return jsonify({"Error":"Not Found"}),404
    
@error.app_errorhandler(500)
def error_500(e):
    print(e)
    return jsonify({"Error":"Internal server error"}),500

@error.app_errorhandler(401)
def error_401(e):
    print(e)
    return jsonify({"Error":"Unauthorised"}),401
    

