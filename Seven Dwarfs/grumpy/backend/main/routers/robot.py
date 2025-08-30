from pydantic import BaseModel
from ..models.patients import schedule

class RobotBase(BaseModel):
    id: int


# ==========================================================================
# ========= THE FOLLOWING SCHEMAS IS NOT USED FOR THE FRONTEND =============
# ==========================================================================
class RegisterRobot(RobotBase):
    models.sc