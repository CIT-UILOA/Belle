"""This model stores the robots"""

import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer

from .. import Base


class RobotStatus(enum.Enum):
    # Used when the robot is idle
    IDLE = "idle"

    # Used when the robot is serviced / charging / disabled
    UNAVAILABLE = "unavailable"

    # Used when the robot is traveling to a destination
    # !: Must have a current "destination" field
    TRAVELING = "traveling"

    # Used when its waiting for the patient to confirm the goods
    AWAITING = "awaiting"

    # Used when the robot encounters an error
    ERROR = "error"


class Robots(Base):
    __tablename__ = "robots"

    # It is very important to have an unique id for each entry
    # in the table. This is to associate and differentiate
    # different entries that might have different data
    id = Column(Integer, primary_key=True)

    # Giving a robot a status by the predefined enums
    status = Column(
        Enum(RobotStatus),
        nullable=False,
        # Start with unavailable since we cannot assume that the robot is ready
        # and we let the robot report its status to this backend
        default=RobotStatus.UNAVAILABLE,
    )
