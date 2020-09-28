from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()
users_table = Table('users', metadata,
   Column('id', Integer, primary_key=True),
   Column('name', String),
   Column('fullname', String),
   Column('password', String)
)
# Column('name', String(50))

metadata.create_all(engine)

Session = sessionmaker(bind=engine)

