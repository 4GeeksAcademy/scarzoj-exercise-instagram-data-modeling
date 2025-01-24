import os
import sys
from sqlalchemy import create_engine, ForeignKey, Integer, String
from eralchemy2 import render_er
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    username =db.Column(db.String(250), nullable=False, unique=True, index=True)
    first_name =db.Column(db.String(250), nullable=False)
    last_name =db.Column(db.String(250), nullable=False)
    email =db.Column(db.String(250), nullable=False, unique=True)

class Post(db.Model):
    __tablename__ = 'post'
    id =db.Column(db.Integer, primary_key=True, unique=True, index=True)
    author_id =db.Column(db.Integer, ForeignKey('user.id'), nullable=False)

class Follower(db.Model):
    __tablename__ = 'follower'
    user_from_id =db.Column(db.Integer, ForeignKey('user.id'), nullable=False, primary_key=True)
    user_to_id =db.Column(db.Integer, ForeignKey('user.id'), nullable=False, primary_key=True)
    
class Comment(db.Model):
    __tablename__ = 'comment'
    id =db.Column(db.Integer, primary_key=True, unique=True, index=True)
    comment_text =db.Column(String(250), nullable=False)
    author_id =db.Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id =db.Column(Integer, ForeignKey('post.id'), nullable=False)

class Media(db.Model):
    __tablename__ = 'media'
    id =db.Column(db.Integer, primary_key=True, unique=True, index=True)
    type =db.Column(db.String(250), nullable=False)
    url =db.Column(db.String(250), nullable=False)
    post_id =db.Column(db.Integer, ForeignKey('post.id'), nullable=False)

try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e