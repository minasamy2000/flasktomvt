from flask_restful import  fields

categorySerializer={
    "id":fields.Integer,
    "name":fields.String,
    "image":fields.String,
    "created_at":fields.DateTime,
    "updated_at":fields.DateTime,
}

postSerializer={
    "id":fields.Integer,
    "title":fields.String,
    'body':fields.String,
    "image":fields.String,
    "created_at":fields.DateTime,
    "updated_at":fields.DateTime,
    'category_id':fields.Integer,
    'category':fields.Nested(categorySerializer)
    }

