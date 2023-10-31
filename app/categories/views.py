from flask import  request, render_template, redirect, url_for,send_from_directory
from app.categories.forms import CategoryForm
from app.models import Category
from app.models import db
from app.categories import category_blueprint
import os

@category_blueprint.route('/',endpoint="index")
def index():
    Categories = Category.get_all_categories()
    return render_template('categories/index.html', categories=Categories)

@category_blueprint.route('/add_category' ,methods=['GET', 'POST'],endpoint="add_category")
def add_category():
    form = CategoryForm()

    if form.validate_on_submit():

        image = form.image.data
        image_path = f"app/upload/{image.filename}"
        image.save(image_path)
        
        new_category = Category(
            name=form.name.data,
            description=form.description.data,
            image= image.filename
    
        )
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('categories.index'))

    return render_template('categories/add_category.html', form=form)

    
def delete_category_image(category):
    if category.image:
        try:
            os.remove(category.image)
        except Exception as e:
            print(f"Error deleting image file: {e}")
            

@category_blueprint.route('/delete_category/<int:category_id>',endpoint="delete_category")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    delete_category_image(category)  
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('categories.index'))






@category_blueprint.route('/categories/<int:id>',endpoint='categories_show')
def category_show(id):
    category=  Category.get_specific_category(id)
    return render_template('categories/show_category.html', category=category)





@category_blueprint.route('/edit_category/<int:category_id>',methods=['GET', 'POST'],endpoint='edit_category')
def edit_category(category_id):
    category = Category.get_specific_category(category_id)
    form = CategoryForm(obj=category) 

    if form.validate_on_submit():
        image = form.image.data
        if image:
            image = form.image.data
            image_path = f"app/upload/{image.filename}"
            image.save(image_path)

        category.name = form.name.data
        category.description = form.description.data
        category.image=image.filename

        category.verified = True
        db.session.commit()
        return redirect(url_for('categories.index'))

    return render_template('categories/edit_category.html', form=form, category=category)

