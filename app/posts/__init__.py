

from flask.blueprints import  Blueprint

post_blueprint= Blueprint('posts',__name__, url_prefix='/posts' )

from app.posts import views