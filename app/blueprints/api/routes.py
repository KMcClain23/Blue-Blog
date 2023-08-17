from . import api
from app import db
from app.models import Post


@api.route('/posts')
def get_posts():
    posts = db.session.execute(db.select(Post)).scalars().all()
    return [post.to_dict() for post in posts]

@api.route('/posts/<post_id>')
def get_post(post_id):
    post = db.session.get(Post, post_id)
    if post:
        return post.to_dict()
    else:
        return {'error': f'Post with an ID of {post_id} does not exist'}, 404