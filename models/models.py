# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, String, Text, text, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import Model, NamedModel, NamedModelShort
from core import Base
Base = declarative_base()
metadata = Base.metadata


class Bank(NamedModel):
    __tablename__ = 'banks'

    card_types = relationship("CardType", back_populates="bank")
    

class CashbackCategory(NamedModel):
    __tablename__ = 'cashback_categories'
    pass


class CashbackType(NamedModelShort):
    __tablename__ = 'cashback_types'
    pass


class RecurrenceType(NamedModelShort):
    __tablename__ = 'recurrence_types'
    recurrences = relationship("Recurrence", back_populates="recurrence_type")


class RewardType(NamedModelShort):
    __tablename__ = 'reward_types'
    pass


class User(Model):
    __tablename__ = 'users'

    firstname = Column(String)
    surname = Column(String)
    email = Column(String, nullable=False)
    address = Column(Text)
    phone_number = Column(String)
    password_hash = Column(String, nullable=False) 


class CardType(NamedModel):
    __tablename__ = 'card_types'

    bank_id = Column(ForeignKey('banks.id'), nullable=False)
    is_virtual = Column(Boolean, nullable=False)
    payment_system = Column(String, nullable=False)
    card_type = Column(String, server_default=text("'debit'::character varying"))

    bank = relationship('Bank', back_populates='card_types')


class Recurrence(Model):
    __tablename__ = 'recurrences'

    recurrence_type_id = Column(ForeignKey('recurrence_types.id'), nullable=False)
    active_on = Column(String, nullable=False)

    recurrence_type = relationship('RecurrenceType', back_populates='recurrences')


class Card(Model):
    __tablename__ = 'cards'

    card_type_id = Column(ForeignKey('card_types.id'), nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    card_number = Column(String, nullable=False)
    expiration_date = Column(String, nullable=False)

    card_type = relationship('CardType')
    user = relationship('User')


class Cashback(Model):
    __tablename__ = 'cashbacks'

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
    special_requirements = Column(Text)
    address = Column(Text)
    city = Column(String)

    bank = relationship('Bank')
    card_type = relationship('CardType')
    category = relationship('CashbackCategory')
    recurrence = relationship('Recurrence')
    reward_type = relationship('RewardType')
    type = relationship('CashbackType')
