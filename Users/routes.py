from . import views


def init_routes(app):
    if app:
        app.add_url_rule('/getUsers', 'getUsers', views.getUsers,methods=['GET'])
        app.add_url_rule('/createUser', 'createUser', views.createUser,methods=['POST'])
        app.add_url_rule('/updateUser/<int:id>', 'updateUser', views.updateUser,methods=['PUT'])
        app.add_url_rule('/deleteUser/<int:id>', 'deleteUser', views.deleteUser, methods=['DELETE'])

