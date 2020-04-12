from . import views


def init_routes(app):
    if app:
        app.add_url_rule('/getPosts', 'getPosts', views.getPosts,methods=['GET'])
        app.add_url_rule('/createPosts/<int:id>', 'createPosts', views.createPosts,methods=['POST'])
        app.add_url_rule('/updatePost/<int:id>', 'updatePost', views.updatePost,methods=['PUT'])
        app.add_url_rule('/deletePost/<int:id>', 'deletePost', views.deletePost, methods=['DELETE'])

