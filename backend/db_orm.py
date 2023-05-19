from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

association_table = db.Table(
    'assotiation',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)

class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String, nullable=False)
    liked = db.Column(db.Boolean, nullable=False)
    # cascade='delete' : delete a post also delete all its subposts
    subposts = db.relationship('Subpost', cascade='delete') # class name so capitaionized
    categories = db.relationship('Category', secondary=association_table, back_populates='posts')

    def __init__(self, **kwargs):
        self.content = kwargs.get("content", "")
        self.liked = kwargs.get("liked", False)

    def serialize(self):
        # Serializes a Post Object
        return {
            "id": self.id,
            "content": self.content,
            "liked": self.liked,
            "subposts": [s.serialize() for s in self.subposts],
            "categories": [c.serialize() for c in self.categories]
        }

class Subpost(db.Model):

    __tablename__ = "subpost"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String, nullable=False)
    liked = db.Column(db.Boolean, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)

    def __init__(self, **kwargs):
        self.content = kwargs.get("content", "")
        self.liked = kwargs.get("liked", False)
        self.post_id = kwargs.get("post_id")

    def serialize(self):
        # Serializes Subpost Object
        return {
            "id": self.id,
            "content": self.content,
            "liked": self.liked,
            "post_id": self.post_id
        }
    

class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    field = db.Column(db.String, nullable=False)
    posts = db.relationship('Post', secondary=association_table, back_populates='categories')

    def __init__(self, **kwargs):
        self.content = kwargs.get("content", "")
        self.field = kwargs.get("field", False)

    def serialize(self):
        # Serializes Subpost Object
        return {
            "id": self.id,
            "content": self.content,
            "field": self.field
        }
    