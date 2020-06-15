import sqlite3
from sqlalchemy import (   create_engine,inspect, Numeric,    Table,    MetaData,    Column,    Integer,    String,    ForeignKey)
from sqlalchemy.orm import (    mapper,    relationship,    sessionmaker)
from Person import person

class DatabaseAccess():
   db_url = 'sqlite:///employee.db'
   engine = create_engine(db_url)
   meta = MetaData(bind=engine)
   lead = Table('Lead', meta,
             Column('id', Integer, primary_key=True, autoincrement=False),
             Column('firstname', String, nullable=False),
             Column('lastname', String, nullable= False),
             Column('mobile', Numeric(precision=0, asdecimal=False, decimal_return_scale=None), nullable=False),
             Column('email', String, nullable=False),
             Column('locationtype', String, nullable=False),
             Column('locationstring', String, nullable=False),
             Column('status', String, nullable=False),
             Column('communication', String, nullable=False, default = None))

   mapper(person, lead) 
   
   

   def fetchMethod(id:int):
       Session = sessionmaker()
       Session.configure(bind=DatabaseAccess.engine)
       session = Session()
       #queryValue = session.query(person).first()
       queryValue = session.query(person).filter(person.id == id).first()
       return queryValue

   def createTable():
       DatabaseAccess.lead.create()
       return "Table created"
    
   def insertData(pers):
        
        Session = sessionmaker()
        Session.configure(bind=DatabaseAccess.engine)
        session = Session()
        try:
            print(pers.lastname)
            session.add(pers,_warn = True) 
            session.commit()
            return "success"
        finally:
            session.close()
    
   def deletTable():
         DatabaseAccess.Lead.drop(DatabaseAccess.engine)

   

    
    



       