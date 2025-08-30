"""This model is used for giving mapped areas a label"""

from sqlalchemy import Column, String

from .. import Base
from ..robot.position import PositionMixin


# This stores all defined points in the map and their positions
# NOTE: The points (x, y, z) are already defined by 'PositionMixin'
class Map(Base, PositionMixin):
    __tablename__ = "map"

    # It is very important to have an unique id for each entry
    # in the table. This is to associate and differentiate
    # different entries that might have different data
    name = Column(String, primary_key=True, index=True)

    # AUDIT: Is this needed?
    # description = Column(String, nullable=False)
