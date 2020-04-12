from Database.models import User
from flask import jsonify
from Database import db
from app import request

def getUsers():
    Users = User.query.all()
    return jsonify([{'id':u.id,'username':u.username,'email':u.email} for u in Users]),200

def createUser():
    input = request.json
    user = User.query.filter_by(username=input['username']).first()
    if user is None:
        try:
            db.session.add(User(username=input['username'], email=input['email']))
            db.session.commit()
        except:
            return jsonify("username or email is not unique"),400
    else:
        return jsonify("User already exist with username {}.Try with other username".format(user.username)),400
    return jsonify("User created successfully with {}".format(input['username'])),201

def updateUser(id):
    user = User.query.filter_by(id=id).first()
    input = request.json
    user.email = input['email']
    db.session.commit()
    return jsonify('updated user with username {}'.format(user.username)),200

def deleteUser(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify('deleted user with username {}'.format(user.username)),200

