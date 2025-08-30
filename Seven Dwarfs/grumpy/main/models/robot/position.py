"""This model stores all positions of different contexts"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer

from .. import Base


# This is a template model in storing positions
class PositionMixin:
    # The positions defined in 3D coordinates
    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)
    z = Column(Integer, nullable=False)


# This table stores all positions of all robots.
# NOTE: The points (x, y, z) are already defined by 'PositionMixin'
class RobotPositions(Base, PositionMixin):
    __tablename__ = "robot_positions"

    # It is very important to have an unique id for each entry
    # in the table. This is to associate and differentiate
    # different entries that might have different data
    id = Column(Integer, primary_key=True, index=True)

    # Associate to id of the robot
    robot_id = Column(Integer, ForeignKey("robots.id"), nullable=False)

    # Used for history
    timestamp = Column(DateTime, nullable=False)
