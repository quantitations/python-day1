
# https://www.sqlalchemy.org/


### Initial stuff ###

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


### Defining tables for the database ###

from sqlalchemy import Column, ForeignKey, String, Boolean, Integer, Float
from sqlalchemy.orm import relationship, backref


class Department(Base):
    __tablename__ = "department"
    id = Column(String(4), primary_key=True)


class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    number = Column(String(4))
    credits = Column(Float, default=1)
    fulfills_quantitative = Column(Boolean, default=False)
    department_id = Column(String(4), ForeignKey("department.id"))
    department = relationship(Department, backref=backref('courses'))


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    credits = Column(Integer, default=0)
    fulfilled_quantitative = Column(Boolean, default=False)

    def courseComplete(self, course):
        self.credits += course.credits
        if course.fulfills_quantitative:
            self.fulfilled_quantitative = True




### Creating the (SQLite) database ###

from sqlalchemy import create_engine

engine = create_engine('sqlite:///temp.db')

# can be convenient to instead use a virtual database (no file created) when experimenting:
# engine = create_engine('sqlite:///:memory:')

Base.metadata.create_all(engine)



### Interacting with the database ###

from sqlalchemy.orm import sessionmaker


# connecting to the database

Session = sessionmaker(bind=engine)
session = Session()


# Putting data into the database

dept_stat = Department(id="STAT")
session.add(dept_stat)

dept_arch = Department(id="ARCH")
session.add(dept_arch)


course1 = Course(title="Linear Models", number="312a", fulfills_quantitative=True, department=dept_stat)
course2 = Course(title="Statistical Consulting", number="627a", credits=.5, department=dept_stat)
course3 = Course(title="Introdutory Statistics", number="100b", fulfills_quantitative=True, department=dept_stat)
course4 = Course(title="Architectural Design I", number="1011", department=dept_arch)

session.add_all([course1, course2, course3, course4])

susie = Student(name="Susan Derkins")
session.add(susie)

session.commit() # write session to the database



susie.id

susie.credits
susie.fulfilled_quantitative

susie.courseComplete(course4)
susie.credits
susie.fulfilled_quantitative

susie.courseComplete(course3)
susie.credits
susie.fulfilled_quantitative

session.commit()



# Getting data from the database


for course in session.query(Course).all():
    print(f"{ course.department_id }-{ course.number }")

for course in session.query(Course).order_by(Course.number):
    print(f"{ course.department_id }-{ course.number }")

for course in session.query(Course).filter(Course.fulfills_quantitative).order_by(Course.title):
    print(f"{ course.title } ({ course.department_id }-{ course.number })")


dept = session.get(Department, "STAT") # gets a database entry by id
for course in dept.courses:
    print(course.title)


# Making a change to the database

course = session.query(Course).filter(Course.title=="Linear Models").first()
course.number = "612b"

susie = session.get(Student, 1) # We saw that susie's id is 1
susie.courseComplete(course)

session.commit()

for course in session.query(Course).all():
    print(f"{ course.department_id }-{ course.number }")



# Closing the session

session.close()
engine.dispose()




# Can be convenient to inspect database with "DB Browser (SQLite)"
