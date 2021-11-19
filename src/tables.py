import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'
    
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Text)
    text = sa.Column(sa.Text)
    date = sa.Column(sa.Date)
    is_done = sa.Column(sa.Boolean, default=False)
