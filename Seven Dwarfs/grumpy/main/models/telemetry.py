import enum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer

from . import Base


class ScheduleStatusEnum(enum.Enum):
    SUCCESS = "success"
    FAILED = "failed"


# A telemetry where it checks if the robot has successfully
# delivered the goods given the schedule.
class ScheduleTelemetryMixin:
    schedule = Column(Integer, ForeignKey("schedules.id"), nullable=False)
    schedule_status = Column(Enum(ScheduleStatusEnum), nullable=False)


# This table is for recording data
# NOTE!: This is NOT the robot's metrics.
class Telemetry(Base, ScheduleTelemetryMixin):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True)

    # Used for history
    timestamp = Column(DateTime, nullable=False)
