from sqlalchemy import *

engine = create_engine('sqlite:///users.db')

metadata = MetaData()

User = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(15), unique=True),
    Column('email', String(50), unique=True),
    Column('password', String(80))
)

metadata.create_all(engine)