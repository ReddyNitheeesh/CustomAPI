from Posts import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import Config

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)