from Database.models import Post,User
from flask import jsonify
from Database import db
from Posts import request,abort


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
        #return "user does not exist with id {}".format(id)
        return abort(400)
    else:
        input=request.json
        post = Post(body=input['body'], author=user)
        db.session.add(post)
        db.session.commit()
    return 'Created Post {}'.format(id)

def updatePost(id):
    post = Post.query.filter_by(id=id).first()
    input = request.json
    post.body = input['body']
    db.session.commit()
    return 'updated post id {}'.format(id)

def deletePost(id):
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    return 'deleted post with id {}'.format(id)

