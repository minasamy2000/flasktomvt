from flask import  request, render_template, redirect, url_for,send_from_directory
from app.posts.forms import PostForm
from app.models import Post,Category
from app.models import db
from app.posts import post_blueprint
import os

@post_blueprint.route('/' ,endpoint="index")
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)




@post_blueprint.route('/add_post' ,methods=['GET', 'POST'],endpoint="add_post")
def create():
    form = PostForm()
    categories=Category.get_all_categories()
    if form.validate_on_submit():
        
        
        image = form.image.data
        image_path = f"app/upload/{image.filename}"
        image.save(image_path)
        category=request.form.get('category')
        print(category)
        
        new_post = Post(
            title=form.title.data,
            body=form.body.data,
            image=image.filename,
            category_id=category
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('posts.index'))

    return render_template('posts/add_post.html', form=form,categories=categories)





    

def delete_post_image(post):
    if post.image:
        try:
            os.remove(post.image)
        except Exception as e:
            print(f"Error deleting image file: {e}")
            

@post_blueprint.route('/delete_post/<int:post_id>',endpoint="delete_post")
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    delete_post_image(post)  
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts.index'))






@post_blueprint.route('/posts/<int:id>',endpoint='post_show')
def post_show(id):
    post=  Post.get_specific_post(id)
    return render_template('posts/show.html', post=post)





@post_blueprint.route('/edit_post/<int:post_id>',methods=['GET', 'POST'],endpoint='edit_post')
def Update(post_id):
    post = Post.get_specific_post(post_id)
    form = PostForm(obj=post) 
    categories=Category.get_all_categories()
    

    if form.validate_on_submit():
        category=request.form.get('category')
        image = form.image.data
        if image:
            image = form.image.data
            image_path = f"app/upload/{image.filename}"
            image.save(image_path)

        post.title = form.title.data
        post.body = form.body.data
        post.image=image.filename
        post.category_id=category
        

        post.verified = True
        db.session.commit()
        return redirect(url_for('posts.index'))

    return render_template('posts/edit_post.html', form=form,categories=categories)

