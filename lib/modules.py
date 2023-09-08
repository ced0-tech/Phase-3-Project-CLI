from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import os

BASE_DIR = os.path.dirname(os.path.realpath("__file__"))
conn = "sqlite:///" + os.path.join(BASE_DIR, "company_data_base.db")
engine = create_engine(conn)
Session = sessionmaker(bind=engine)

Base = declarative_base()

# Define the association table for the many-to-many relationship
managers_employees = Table(
    'managers_employees',
    Base.metadata,
    Column('manager_id', Integer, ForeignKey('managers.id')),
    Column('employee_id', Integer, ForeignKey('employees.id'))
)


class Managers(Base):
    __tablename__ = 'managers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Define the many-to-many relationship with Employees
    employees = relationship('Employees', secondary=managers_employees)

    """ def __repr__(self):
        print(self.name) """


class Employees(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Define the many-to-many relationship with Managers
    managers = relationship('Managers', secondary=managers_employees)

    """ def __repr__(self):
        print(self.name) """
