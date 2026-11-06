from typing import Annotated

from pydantic import (BaseModel, ConfigDict, Field, StringConstraints, )

Namestr=Annotated[
    str,
    StringConstraints(
        min_length=2, max_length=4
    ),
]

DescStr=Annotated[
    str,
    StringConstraints(
        min_length=5, max_length=100
    ),
]

class MaintenanceCreate(BaseModel):
    equipment_id:int=Field(gt=0)
    student_id:Namestr|int=Field(ge=0, le=3) 
    
    description:DescStr
    priority:int=Field(ge=0, le=4 )
class MaintenanceRead(BaseModel):
    model_config=ConfigDict (
        from_attributes=True
    )
    id:int
    equipment_id:int
    student_id:Namestr | int
    description:DescStr
    status:str
