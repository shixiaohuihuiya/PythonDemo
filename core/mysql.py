import datetime
import uuid

from sqlalchemy import Column, String, DateTime, create_engine, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, as_declarative
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# 创建连接
engine = create_engine("mysql+pymysql://root:root@localhost:3306/test?charset=utf8mb4&binary_prefix=true",echo=True)


class User(Base):
    __tablename__ = "user"
    id = Column(String(36), nullable=False, primary_key=True)
    name = Column(String(100),nullable=False,comment='姓名',unique=True)
    age = Column(String(4),nullable=True,comment='年龄')
    sex = Column(String(4),nullable=True,comment='性别')
    hobdy = Column(String(100),nullable=True,comment='爱好')
    createtime = Column('create_time',DateTime,nullable=True,comment="创建时间")
    desc = Column(String(100),nullable=True,comment='备注',default=None)

    def __init__(self,id,name,age,sex,hobdy,createtime,desc):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.hobdy = hobdy
        self.createtime = createtime
        self.desc = desc

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer,nullable=False,primary_key=True)
    name = Column(String,nullable=True)
    birthday = Column(DateTime,nullable=True)
    teacherId = Column('teacher_id',Integer,ForeignKey('teacher.id'))
    teacher = relationship('Teacher', back_populates='student')

    def __init__(self,id,name,birthday):
        self.id = id
        self.name = name
        self.birthday = birthday


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer,nullable=False,primary_key=True)
    name = Column(String,nullable=True)
    classNum = Column(Integer,nullable=True)
    student = relationship('Student', back_populates='teacher')


    def __init__(self,id,name,classNum):
        self.id  = id
        self.name = name
        self.classNum = classNum


Base.metadata.create_all(engine) # 创建表 或者 映射
Session = sessionmaker(bind=engine)
session = Session()

# 新增
def add_sql(T):
    session.add(T)
    session.commit()
    session.close()

# 删除
def del_sql(T):
    pass








if __name__ == '__main__':
    # user =  session.query(User).all()
    # id  = uuid.uuid4()
    # new_user = User(id,"122121","12","女","sss",datetime.datetime.now(),"管理员")
    # session.add(new_user)
    # session.commit()

    # 查询
    # first_t = session.query(Student).join(Teacher).filter(Teacher.id==Student.teacherId).all()
    #
    # for i in first_t:
    #     print(i.id,i.name,i.birthday)

    add_sql(User(112,"223342","2","3","编程",datetime.datetime.now().__str__(),"新增"))