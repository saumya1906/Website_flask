from flask import Flask, render_template,request,redirect,url_forredirect,url_for,flash
app = Flask(_name_)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem
engine=create_engine('sqlite:///website.db')
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()
@app.route('/')
def Default


if __name__=='__msin__':
