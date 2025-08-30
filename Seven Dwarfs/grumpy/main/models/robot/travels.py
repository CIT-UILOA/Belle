"""This model records all travels of all robots"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from .. import Base


class Travels(Base):
    __tablename__ = "travels"

    # It is very important to have an unique id for each entry
    # in the table. This is to associate and differentiate
    # different entries with similar labels that might have
    # different data
    id = Column(Integer, primary_key=True)

    # Associate to id of the robot
    robot_id = Column(Integer, ForeignKey("robots.id"), nullable=False)

    # Records where it started and where it landed
    origin = Column(String, ForeignKey("map.name"), nullable=False)
    target = Column(String, ForeignKey("map.name"), nullable=False)

    # Records the patient name
    # NOTE: There might be no patient if it is
    #       returning to default location
    patient = Column(Integer, ForeignKey("patients.id"), nullable=True)

    # Used for history
    timestamp = Column(DateTime, nullable=False)
