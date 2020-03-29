from Database.models import Post,User
from flask import jsonify
from Database import db
from Posts import request


def getPosts():
    data=[]
    posts = Post.query.all()
    for p in posts:
        data.append({'id':p.id,
                     'username':p.author.username,
                     'body':p.body
                     })
    return jsonify(data)

def createPosts(id):
    user = User.query.filter.filter_by(User_id=id).first()
    if user is None:
        return "user does not exist with id {}".format(id)
    else:
        input=request.json
        post = Post(body=input['body'], author=user)
        db.session.add(post)
        db.session.commit()
    return 'Created Post {}'.format(id)

def updatePost(id):
    return 'updated post id {}'.format(id)

def deletePost(id):
    return 'deleted post id {}'.format(id)

