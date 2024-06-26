# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, String, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Bank(Base):
    __tablename__ = 'banks'

    id = Column(UUID, primary_key=True)
    name = Column(String)
    name_ru = Column(String)
    name_kz = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    

class CashbackCategory(Base):
    __tablename__ = 'cashback_categories'

    id = Column(UUID, primary_key=True)
    name = Column(String)
    name_ru = Column(String)
    name_kz = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class CashbackType(Base):
    __tablename__ = 'cashback_types'

    id = Column(UUID, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, server_default=text("now()"))
    updated_at = Column(DateTime, server_default=text("now()"))


class RecurrenceType(Base):
    __tablename__ = 'recurrence_types'

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=text("now()"))
    updated_at = Column(DateTime, server_default=text("now()"))


class RewardType(Base):
    __tablename__ = 'reward_types'

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=text("now()"))
    updated_at = Column(DateTime, server_default=text("now()"))


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True)
    firstname = Column(String)
    surname = Column(String)
    email = Column(String, nullable=False)
    address = Column(Text)
    phone_number = Column(String)
    created_at = Column(DateTime, server_default=text("now()"))
    updated_at = Column(DateTime, server_default=text("now()"))


class CardType(Base):
    __tablename__ = 'card_types'

    id = Column(UUID, primary_key=True)
    name = Column(String)
    name_ru = Column(String)
    name_kz = Column(String)
    bank_id = Column(ForeignKey('banks.id'), nullable=False)
    is_virtual = Column(Boolean, nullable=False)
    payment_system = Column(String, nullable=False)
    card_type = Column(String, server_default=text("'debit'::character varying"))
    created_at = Column(DateTime, server_default=text("now()"))
    updated_at = Column(DateTime, server_default=text("now()"))

    bank = relationship('Bank')


class Recurrence(Base):
    __tablename__ = 'recurrences'

    id = Column(UUID, primary_key=True)
    recurrence_type_id = Column(ForeignKey('recurrence_types.id'), nullable=False)
    active_on = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=text("now()"))
    updated_at = Column(DateTime, server_default=text("now()"))

    recurrence_type = relationship('RecurrenceType')


class Card(Base):
    __tablename__ = 'cards'

    id = Column(UUID, primary_key=True)
    card_type_id = Column(ForeignKey('card_types.id'), nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    card_number = Column(String, nullable=False)
    expiration_date = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    card_type = relationship('CardType')
    user = relationship('User')


class Cashback(Base):
    __tablename__ = 'cashbacks'

    id = Column(UUID, primary_key=True)
    card_type_id = Column(ForeignKey('card_types.id'))
    bank_id = Column(ForeignKey('banks.id'))
    is_qr = Column(Boolean)
    title = Column(String)
    description = Column(Text)
    reward = Column(String, nullable=False)
    reward_type_id = Column(ForeignKey('reward_types.id'), nullable=False)
    min_payment = Column(Float(53))
    max_reward = Column(String)
    category_id = Column(ForeignKey('cashback_categories.id'), nullable=False)
    date_to = Column(Date)
    date_from = Column(Date)
    type_id = Column(ForeignKey('cashback_types.id'), nullable=False)
    recurrence_id = Column(ForeignKey('recurrences.id'))
    comments = Column(Text)
    created_at = Column(DateTime, server_default=text("now()"))
    updated_at = Column(DateTime, server_default=text("now()"))
    special_requirements = Column(Text)

    bank = relationship('Bank')
    card_type = relationship('CardType')
    category = relationship('CashbackCategory')
    recurrence = relationship('Recurrence')
    reward_type = relationship('RewardType')
    type = relationship('CashbackType')
