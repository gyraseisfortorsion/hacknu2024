from sqlalchemy.orm import relationship
from .base import isActiveModel, Model
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from core import Base
from datetime import datetime

class User(isActiveModel):
    __tablename__ = 'users'

    user_info_id = Column(ForeignKey('user_info.id', ondelete='SET NULL'), nullable=False)
    role = Column(Integer, nullable=False)
    school_id = Column(UUID)
    password_hash = Column(String, nullable=False)
    email = Column(String, nullable=False)
    last_signed_at = Column(DateTime)


    user_info = relationship('UserInfo', back_populates='user')
    teacher_info = relationship('TeacherInfo', back_populates='user')
    student_info=relationship('StudentInfo', back_populates='user')

class UserInfo(Model):
    __tablename__ = 'user_info'

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    father_name = Column(String)
    address = Column(String)
    gender = Column(Boolean)
    phone_number = Column(String)

    user = relationship('User', back_populates='user_info')

class StudentInfo(Model):
    __tablename__ = 'student_info'

    grade_level = Column(Integer)
    guardian_phone_number = Column(String)
    guardian_first_name = Column(String)
    guardian_last_name = Column(String)
    guardian_father_name = Column(String)
    guardian_email = Column(String)
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'))

    user = relationship('User', back_populates='student_info')


class TeacherInfo(Model):
    __tablename__ = 'teacher_info'

    department_id = Column(UUID)
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'))

    user = relationship('User', back_populates='teacher_info')

# class RefreshToken(Base):
#     __tablename__ = "refresh_tokens"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     refresh_token = Column(String, unique=True, index=True)
#     expires_at = Column(DateTime, default=datetime.utcnow)