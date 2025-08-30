"""This model stores the metrics of the robot (e.g. battery status)"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer

from .. import Base


class Metrics(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True)

    # used for history
    timestamp = Column(DateTime, nullable=False)

    # Associate with the robot
    robot_id = Column(Integer, ForeignKey("robots.id"), nullable=False)

    # todo: add metrics here once what's being collected is confirmed.
