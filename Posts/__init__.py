from ..app import app,request,abort
from .routes import init_routes


init_routes(app)

