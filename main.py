from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'majda-je-velka-holka'
db = SQLAlchemy(app)


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


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    image = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'image': self.image,
            'author': self.author
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
    return jsonify({"users": u.serialize() for u in User.query.all()})


@app.route('/articles')
def articles():
    return jsonify({"articles": a.serialize() for a in Article.query.all()})


@app.route('/articles/create', methods=['POST'])
@jwt_required()
def addArticle():
    c = request.json

    a = Article(title=c['title'], content=c['content'],
                image=c['image'], author=c['author'])
    db.session.add(a)
    db.session.commit()

    return 'Ok'


@app.route('/register', methods=['POST'])
def register():
    c = request.json
    u = User(username=c["username"], email=c["email"], password=c["password"])

    db.session.add(u)
    db.session.commit()

    return 'Ok'


if __name__ == "__main__":
    app.run(debug=True)
