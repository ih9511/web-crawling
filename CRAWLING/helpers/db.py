from sqlalchemy import engine, create_engine, DateTime, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import pandas as pd

Base = declarative_base()

class Tausers(Base):
    __tablename__ = "tauser"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email =  Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    Base = declarative_base()

class Crawling(Base):
    __tablename__ = "crawling"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email =  Column(String)
    itemname = Column(String)
    price = Column(Integer)
    link = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    Base = declarative_base()

class MySQLDatabase:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        # Base.metadata.create_all(self.engine)

    def add_user(self, username, email):
        session = self.Session()
        user = Tausers(username=username, email=email)
        session.add(user)
        session.commit()
        session.close()

    def get_user_by_username(self, username):
        session = self.Session()
        user = session.query(Tausers).filter_by(username=username).first()
        session.close()
        return user

    def get_user_by_email(self, email):
        session = self.Session()
        user = session.query(Tausers).filter_by(email=email).first()
        session.close()
        return user

    def update_user_email(self, username, new_email):
        session = self.Session()
        user = session.query(Tausers).filter_by(username=username).first()
        if user:
            user.email = new_email
            session.commit()
        session.close()

    def delete_user(self, username):
        session = self.Session()
        user = session.query(Tausers).filter_by(username=username).first()
        if user:
            session.delete(user)
            session.commit()
        session.close()

    def to_sql(self):
        df = pd.read_excel(r"C:\Users\USER\Desktop\workspace01\crawling\data\모자결과물.xlsx")
        try:
            df.to_sql(name="crawling", con = self.engine)
            print("로그남김 잘됨")
        except Exception as e:
            print(e)    


if __name__ == "__main__":
    try:
        user = "root"
        password = ""
        host = "localhost"
        port = 3306
        db = "test"

        db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
        db = MySQLDatabase(db_url)

        print(db.__repr__)

        db.add_user("john_doe", "john@example.com")
        user =  db.get_user_by_username("john_doe")
        print(user.username, user.email)
        db.update_user_email("john_doe", "new_email@example.com")
        user =  db.get_user_by_username("john_doe")
        print(user.username, user.email)

        # db.delete_user("john_doe")

    except Exception as e:
        print("DB부분처리안됨")    
        print("e")


# 디비명 test

# CREATE TABLE `tauser` (
#   `id` INT(10) NOT NULL AUTO_INCREMENT,
#   `username` VARCHAR(50) NOT NULL DEFAULT '0' COLLATE 'utf8mb4_general_ci',
#   `email` VARCHAR(50) NOT NULL DEFAULT '0' COLLATE 'utf8mb4_general_ci',
#   `created_at` TIMESTAMP NULL DEFAULT NULL,
#   `updated_at` TIMESTAMP NULL DEFAULT NULL,
#   PRIMARY KEY (`id`) USING BTREE
# )
# COLLATE='utf8mb4_general_ci'
# ENGINE=InnoDB
# AUTO_INCREMENT=5
# ;