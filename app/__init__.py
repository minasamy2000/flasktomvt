from flask import Flask, render_template,send_from_directory
from flask_migrate import Migrate

from flask_restful import Api
from app.config import  app_config as AppConfig
from app.models import db
from app.posts import post_blueprint
from app.categories import  category_blueprint
from app.posts.api.api_views import PostListClass,PostResource

def create_app(config_mode='dev'):
    app = Flask(__name__)
    CurrentConfigClass = AppConfig[config_mode]
  
    
    app.config["SQLALCHEMY_DATABASE_URI"] = CurrentConfigClass.SQLALCHEMY_DATABASE_URI
    app.config.from_object(CurrentConfigClass) 
    app.config['UPLOAD_FOLDER'] = 'upload'
    app.config['SECRET_KEY'] = '12345'

    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)


    @app.route('/' ,endpoint="home")
    def index():
        return render_template('home.html',)
    
    @app.route('/aboutus' ,endpoint="aboutus")
    def aboutus():
        return render_template('aboutus.html')
    
    @app.route('/contactsus' ,endpoint="contactus")
    def contactus():
        return render_template('contactsus.html')

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)  
    
    # @app.errorhandler(404)
    # def page_not_found(error):
    #     return render_template('notfound.html')
    

    app.register_blueprint(post_blueprint)
    app.register_blueprint(category_blueprint)
    
    
    api.add_resource(PostListClass, '/api/post')
    api.add_resource(PostResource, '/api/post/<int:post_id>')
    
    

    return app