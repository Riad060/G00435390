from sqlalchemy  import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass
class MaintenanceDB(Base):
    __tablename__="maintenances"
    id:Mapped[int]=mapped_column(
        primary_key=True,index=True,unique=True
    )
    equipment_id:Mapped[int]=mapped_column(
        Integer,nullable=False
    )
    student_id:Mapped[str | int]=mapped_column(
        String[2],nullable=False
    )
    description:Mapped[str]=mapped_column(
        String(100),nullable=False
    )
    priority:Mapped[int]=mapped_column(
        Integer,nullable=False
    )
    status:Mapped[str]=mapped_column(
        String[20],nullable=False,
        default="OPEN"
    )