"""This model is used for storing patients"""

from sqlalchemy import Column, ForeignKey, Integer, String

from .. import Base


class Patients(Base):
    __tablename__ = "patients"

    # It is very important to have an unique id for each entry
    # in the table. This is to associate and differentiate
    # different entries with similar labels that might have
    # different data
    id = Column(Integer, primary_key=True)

    # Full name of patient
    name = Column(String, nullable=False)

    # Current place of the patient
    # NOTE: The location may not be defined due to other reasons.
    #       But most of the time, it is defined
    location = Column(String, ForeignKey("map.name"), nullable=True)
