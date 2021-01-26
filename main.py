import logging
from dictalchemy import make_class_dictable
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT, jwt_required, current_identity
# try:
#     from flask_cors import CORS  # The typical way to import flask-cors
# except ImportError:
#     # Path hack allows examples to be run without installation.
#     import os
#     parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     os.sys.path.insert(0, parentdir)

#     from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'majda-je-velka-holka'
db = SQLAlchemy(app)

make_class_dictable(db.Model)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }


class ArticleTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    article_id = db.Column(db.Integer, db.ForeignKey('article.id'),
                           nullable=False)
    # article = db.relationship('Article',
    #                           backref=db.backref('article', lazy=True))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    image = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    visible = db.Column(db.Boolean, default=False, nullable=False)

    tags = db.relationship("ArticleTag", backref="article", lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'image': self.image,
            'author': self.author,
            'visible': self.visible,
            'tags': [t.serialize() for t in (self.tags)]
        }


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    link = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'link': self.link
        }

# AUTH


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id)


jwt = JWT(app, authenticate, identity)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users')
def users():
    return jsonify({"users": [u.serialize() for u in User.query.all()]})


@app.route('/api/menu', methods=['GET'])
def menu():
    return jsonify([m.serialize() for m in MenuItem.query.all()])


@app.route('/api/menu/create', methods=['POST'])
@jwt_required()
def menu_add():
    m = MenuItem()

    if 'id' in request.json:
        del request.json['id']

    print(request.json)

    m.fromdict(request.json)

    db.session.add(m)
    db.session.commit()

    return jsonify(m.serialize())


@app.route('/articles')
def articles():
    # return jsonify({"articles": [a.serialize() for a in Article.query.all()]})
    print(current_identity)
    return jsonify({"articles": [a.serialize() for a in Article.query.filter_by(visible=True)]})


@app.route('/articles/all')
@jwt_required()
def all_articles():
    return jsonify({"articles": [a.serialize() for a in Article.query.all()]})


@app.route('/article/<id>')
def article(id):
    a = Article.query.filter_by(id=id).first()
    if a is None:
        return "Not found"
    return jsonify(a.serialize())


@app.route('/articles/create', methods=["POST"])
@jwt_required()
def add_article():
    c = request.json

    a = Article(title=c['title'], content=c['content'],
                image=c['image'], author=c['author'])
    db.session.add(a)
    db.session.commit()

    return jsonify({"result": "ok"})


@app.route('/articles/delete/<id>', methods=["DELETE"])
@jwt_required()
def delete_article(id):
    a = Article.query.filter_by(id=id).first()
    if a is None:
        return "Not found"

    db.session.delete(a)
    db.session.commit()

    return jsonify({"result": "ok"})


@app.route('/articles/put', methods=["PUT"])
@jwt_required()
def put_article():
    # c = request.json
    a = Article.query.filter_by(id=request.json['id']).first()

    del request.json['id']

    print(request.json)
    print(request.json['tags'])

    a.fromdict(request.json, follow=['tags'])

    a.tags[0].name = 'e'
    print(a.tags[0].name)

    db.session.commit()
    return jsonify(a.serialize())


# @app.route('/test')
# def testa():
#     return "SDsadsaa"


@app.route('/register')
def register():
    c = request.json
    u = User(username=c["username"], email=c["email"], password=c["password"])

    db.session.add(u)
    db.session.commit()

    return 'Ok'


@app.after_request
def add_headers(response):
    response.headers.add('Content-Type', 'application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods',
                         'PUT, GET, POST, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Expose-Headers',
                         'Content-Type,Content-Length,Authorization,X-Pagination')
    return response


app.config['CORS_HEADERS'] = 'Content-Type'
# CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
