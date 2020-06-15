
from sqlalchemy import (   create_engine, Numeric,    Table,    MetaData,    Column,    Integer,    String,    ForeignKey)
from sqlalchemy.orm import (    mapper,    relationship,    sessionmaker)
class person(object):
    def __init__(self,id, firstname, lastname, mobile, email, locationtype, locationstring, status, communication):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.mobile = mobile
        self.email = email
        self.locationtype = locationtype
        self.locationstring = locationstring
        self.status = status
        self.communication = communication

   