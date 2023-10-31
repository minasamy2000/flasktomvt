from flask_sqlalchemy import SQLAlchemy
from datetime import  datetime
from flask import url_for
db= SQLAlchemy()




class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    def __repr__(self):
        return f'<Post {self.id}: {self.title}>'
    
    @classmethod
    def get_all_posts(cls):
        return cls.query.all()

    @classmethod
    def get_specific_post(cls, id):
        return cls.query.get_or_404(id)
    
    @property
    def show_url(self):
        return url_for('posts.post_show', id=self.id)
    
    @classmethod
    def save_object(cls, requestdata):
        post = cls(**post)
        db.session.add(post)
        db.session.commit()
        return post
    
    @classmethod
    def delete_object(cls, id):
        post = cls.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
        return True



class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    posts = db.relationship('Post', backref='category')

    @classmethod
    def get_all_categories(cls):
        return cls.query.all()

    @classmethod
    def get_specific_category(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def delete_object(cls, id):
        category = cls.query.get_or_404(id)
        db.session.delete(category)
        db.session.commit()
        return True


    @property
    def delete_url(self):
        return url_for('category.delete', id=self.id)

    @property
    def show_url(self):
        return url_for('categories.categories_show', id=self.id)
    
    def __str__(self):
        return self.name
        
