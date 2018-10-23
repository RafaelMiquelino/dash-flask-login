from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy import Integer, String
import configparser

config = configparser.ConfigParser()
config.read('config.txt')

metadata = MetaData()

User = Table('user', metadata, Column('id', Integer, primary_key=True),
             Column('username', String(15), unique=True),
             Column('email', String(50), unique=True),
             Column('password', String(80)))

engine = create_engine(config.get('database', 'con'))


def create_user_table():
    metadata.create_all(engine)


def add_user(username, password, email):
    from werkzeug.security import generate_password_hash

    hashed_password = generate_password_hash(password, method='sha256')

    ins = User.insert().values(
        username=username, email=email, password=hashed_password)

    conn = engine.connect()
    conn.execute(ins)
    conn.close()


def del_user(username):
    delete = User.delete().where(User.c.username == username)

    conn = engine.connect()
    conn.execute(delete)
    conn.close()


def show_users():
    from sqlalchemy.sql import select
    select_st = select([User.c.username, User.c.email])

    conn = engine.connect()
    rs = conn.execute(select_st)

    for row in rs:
        print(row)

    conn.close()
