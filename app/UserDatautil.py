"""
Module to read data from database 
""" 
from app  import db

import app.views as views
import app.models as models
from app.models import User
import logging as log
from wtforms.fields.simple import BooleanField

log.basicConfig(filename='example.log',level=log.DEBUG)
def getUser(username):

    log.debug(username)
    return username

def getId(user_id):
    log.debug("test for user id")
    
    log.debug(id)
    return int(user_id)

def getAge():
    return

def getUserIntput():
    
    db.insert({'type': 'anger', 'count': slider6data})
    db.insert({'type': 'happy', 'count': slider1data})
    db.insert({'type': 'sad', 'count': slider5data})
    db.insert({'type': 'Cal', 'count': slider1data})

    
    
    
