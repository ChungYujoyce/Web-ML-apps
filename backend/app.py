from flask import Flask, request
import json
import db
DB = db.DatabaseDriver()

app = Flask(__name__)

def success_response(data, code=200):
    return json.dumps(data), code

def failure_response(error, code=400):
    return json.dumps(error), code


@app.route("/")
@app.route("/posts/")
def get_posts():
    #endpoint for getting data
    return success_response(DB.get_all_posts())

@app.route("/subposts/")
def get_subposts():
    return success_response(DB.get_all_subposts())

@app.route("/posts/<int:post_id>/subposts/", methods=["POST"])
def create_subposts(post_id):
    body = json.loads(request.data)
    content = body.get("content")

    post = DB.get_post_by_id(post_id)
    if not post:
        return failure_response("post not found")

    subpost_id = DB.insert_subposts(content, False, post_id)
    subpost = DB.get_subpost_by_id(subpost_id)
    return success_response(subpost, 201)

@app.route("/posts/<int:post_id>/subposts/")
def get_subposts_of_post(post_id):
    return success_response({"subposts": DB.get_subposts_of_post(post_id)})

@app.route("/posts/", methods=["POST"])
def create_post():
    body = json.loads(request.data)
    content = body.get("content")
    liked = body.get("liked")
    
    if content is not None:
        post_id = DB.insert_post_table(content, liked)
        return success_response(DB.get_post_by_id(post_id))
    return failure_response("no content", 400)
    

@app.route("/posts/<int:post_id>/")
def get_post(post_id):
    post = DB.get_post_by_id(post_id)
    if post is not None:
        return success_response(post)
    return failure_response("error")

@app.route("/posts/<int:post_id>/", methods = ["POST"])
def update_post(post_id):
    body = json.loads(request.data)
    content = body.get("content")
    liked = body.get("liked")
    post = DB.get_post_by_id(post_id)
    
    if content is None and liked is None:
        return failure_response("no content", 400)
    elif content is None:
        DB.update_post_by_id(post_id, post['content'], liked)
    elif liked is None:
        DB.update_post_by_id(post_id, content, post['liked'])
    else:
        DB.update_post_by_id(post_id, content, liked)
        
    return success_response(DB.get_post_by_id(post_id))

@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    post = DB.get_post_by_id(post_id)
    if post is None:
        return failure_response("post not found")
    DB.delete_post_by_id(post_id)
    return success_response(post)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)