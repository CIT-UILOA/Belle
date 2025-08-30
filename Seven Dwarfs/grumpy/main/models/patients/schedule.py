"""
This table records all schedules of all patients

NOTE: This schedules does not store breakfast, lunch and
dinner in one entry but stored in different entries.

Example:

- [1]: 7:00AM - patient-a (for breakfast)
- [2]: 12:00PM - patient-a (for lunch)
- [3]: 6:00PM - patient-a (for dinner)

"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer

from .. import Base


#
class Schedule(Base):
    __tablename__ = "schedules"

    # It is very important to have an unique id for each entry
    # in the table. This is to associate and differentiate
    # different entries with similar labels that might have
    # different data
    id = Column(Integer, primary_key=True)

    # Associate with patient
    patient = Column(Integer, ForeignKey("patients.id"), nullable=False)

    # Column for the specified schedule.
    # Example: 12:00PM for lunch
    time = Column(DateTime, nullable=False)
