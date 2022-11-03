from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:kartik2703@localhost/enlightcloud"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Shubhangi123/MySQL80@localhost:3306/veda?charset=utf8mb4"

#engine = create_engine(
#    SQLALCHEMY_DATABASE_URL
#)postgresql://postgres:pasword@localhost/databasename

