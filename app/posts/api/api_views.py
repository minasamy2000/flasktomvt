from flask_restful import Resource, marshal_with
from app.models import  Post, db
from app.posts.api.serializers import postSerializer
from flask import  request
from app.posts.api.parsers import post_request_parser




class PostListClass(Resource):
    @marshal_with(postSerializer)
    def get(self):
        posts= Post.get_all_posts()
        return posts


    @marshal_with(postSerializer)
    def post(self):
        post_args=post_request_parser.parse_args()
        new_post = Post(
            title=post_args['title'],
            body=post_args['body'],
            image=post_args['image'],
            category_id=post_args['category_id']
        )
        db.session.add(new_post)
        db.session.commit()
        return  new_post, 201
        # save object
        return  "Post Method"



class PostResource(Resource):
    @marshal_with(postSerializer)
    def get(self, post_id):
        post =Post.get_specific_post(post_id)
        return post, 200

    @marshal_with(postSerializer)
    def put(self, post_id):
        post =Post.get_specific_post(post_id)
        post_args = post_request_parser.parse_args()
       
        post.title=post_args['title']
        post.image = post_args['image']
        post.body = post_args['body']
        post.category_id = post_args['category_id']
        db.session.add(post)
        db.session.commit()
        return post

        



    def delete(self, post_id):
        Post.delete_object(post_id)
        return  'no content', 204
