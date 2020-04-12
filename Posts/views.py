from Database.models import Post,User
from flask import jsonify
from Database import db
from app import request


def getPosts():
    posts = Post.query.all()
    return jsonify([{'id':p.id,'username':p.author.username,'body':p.body,'timestamp':p.timestamp}for p in posts]),200

def createPost(id):
    u = User.query.filter_by(id=id).first()
    if u is None:
        return jsonify("no user exists with id {}".format(id)),400
    else:
        input=request.json
        post = Post(body=input['body'], author=u)
        db.session.add(post)
        db.session.commit()
    return jsonify('Created Post for username {}'.format(post.author.username)),201

def updatePost(id):
    post = Post.query.filter_by(id=id).first()
    input = request.json
    post.body = input['body']
    db.session.commit()
    return jsonify('updated post for username {}'.format(post.author.username)),200

def deletePost(id):
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    return jsonify('deleted post for username {}'.format(post.author.username)),200

