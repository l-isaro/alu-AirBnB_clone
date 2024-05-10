#!/usr/bin/python3

#Defining the Base model class

import uuid
from datetime import datetime

class BaseModel:

    '''This class defines all the common attributes
    id: string - assign with an uuid when an instance is created.
    created_at: datetime - assign with the current datetime when an instance is created.
    updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
    '''

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):

        '''updates the public instance attribute updated_at with the current datetime'''

        self.updated_at = datetime.now()

    def to_dict(self):

        '''returns a dictionary containing all keys/values of __dict__'''
        
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
