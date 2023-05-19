from flask import Flask, request
import json
from db_orm import db
from db_orm import Category, Subpost, Post


db_filename = "post.db"

app = Flask(__name__)

# setup config
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_filename}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True # debugging purposes

db.init_app(app)
with app.app_context():
    db.create_all()

def success_response(data, code=200):
    return json.dumps(data), code

def failure_response(error, code=400):
    return json.dumps(error), code

# --------------- posts ------------------------
@app.route("/")
@app.route("/posts/")
def get_posts():
    #endpoint for getting data
    return success_response([p.serialize() for p in Post.query.all()])

@app.route("/subposts/")
def get_subposts():
    return success_response([s.serialize() for s in Subpost.query.all()])

@app.route("/categories/")
def get_categories():
    return success_response([c.serialize() for c in Category.query.all()])

@app.route("/posts/", methods=["POST"])
def create_post():
    body = json.loads(request.data)
    new_post = Post(content = body.get("content", ''), liked = body.get("liked", False))
    db.session.add(new_post)
    db.session.commit()
    return success_response(new_post.serialize(), 201)

@app.route("/posts/<int:post_id>/")
def get_post(post_id):
    post = Post.query.filter_by(id = post_id).first()
    if post is not None:
        return success_response(post.serialize())
    return failure_response("error")

@app.route("/posts/<int:post_id>/", methods = ["POST"])
def update_post(post_id):
    post = Post.query.filter_by(id = post_id).first()
    if post is None:
        return failure_response("error")
    
    body = json.loads(request.data)
    post.content = body.get('content', post.content)
    post.liked = body.get('liked', post.liked)
    db.session.commit()
    return success_response(post.serialize())

@app.route("/posts/<int:post_id>/", methods=["DELETE"])
def delete_post(post_id):
    post = Post.query.filter_by(id = post_id).first()
    if post is None:
        return failure_response("error")
    
    db.session.delete(post)
    db.session.commit()
    return success_response(post.serialize())

# --------------- subposts ------------------------

@app.route("/posts/<int:post_id>/subposts/", methods=["POST"])
def create_subposts(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return failure_response('Post not found!')
    
    body = json.loads(request.data)
    new_subpost = Subpost(
        content = body.get('content', ''),
        liked = body.get('liked', False),
        post_id = post_id,
        )
    db.session.add(new_subpost)
    db.session.commit()
    return success_response(new_subpost.serialize())
    
# ---------- category routes ----------------

@app.route("/posts/<int:post_id>/category/", methods=["POST"])
def assign_category(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return failure_response('Post not found!')
    
    body = json.loads(request.data)
    content = body.get('content')
    if content is None:
        return failure_response("No content")
    category = Category.query.filter_by(content=content).first()
    if category is None:
        category = Category(
            content = content,
            field = body.get('field', '')
        )
    post.categories.append(category)
    db.session.commit()
    return success_response(post.serialize())  


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)