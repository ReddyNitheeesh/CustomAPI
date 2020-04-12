from app import app
from flask_sqlalchemy import SQLAlchemy
#some import error with migrate object need to fix
#from flask_migrate import Migrate
from settings import Config

app.config.from_object(Config)
db = SQLAlchemy(app)
db.init_app(app)
#migrate = Migrate(app, db)