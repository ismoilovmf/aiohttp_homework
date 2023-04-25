from models import User, Advertisement
import time
from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from db_config import DSN_SYNC

engine = create_engine(DSN_SYNC)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


@fixture(scope='session', autouse=True)  # выполнить автоматически 1 раз за сессию
def prepare_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()


@fixture()
def create_user():
    with Session() as session:
        user = User(email=f'test_email_{time.time()}@mail.ru', password='12345678')
        session.add(user)
        session.commit()
        return {
            'id': user.id,
            'email': user.email
        }


@fixture()
def create_adv(create_user):
    with Session() as session:
        adv = Advertisement(
            title='test_title',
            description='test_description',
            user_id=create_user['id'],
        )
        print(f"{create_user['id']} = ")
        session.add(adv)
        session.commit()
        return {
            'id': adv.id,
            'title': adv.title,
            'description': adv.description,
            'user_id': adv.user_id,
        }
