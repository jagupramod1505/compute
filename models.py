
from sqlalchemy import  Column, Integer, String, TIMESTAMP, text,false,Float
from database import Base





class compute(Base):

    __tablename__ = "compute"
    huuid = Column(String, primary_key=True, index=True)
    user = Column(String, nullable=false)
    url= Column(String, nullable=false)
    password = Column(String,nullable=false)
    hypervisor = Column(String,nullable=false)
    is_master = Column(String,nullable=false,default=0)
    memory_used = Column(Float ,nullable=false, default=0)
    memory_total = Column(Float, nullable=false, default=0)
    cpu_used = Column(Float, nullable=false, default=0)
    cpu_total = Column(Integer,default=0)
    uptime = Column(Integer, nullable=false, default=0)
    monthly_uptime = Column(String, nullable=false, default=0)
    total_uptime = Column(Integer, nullable=false, default=0)
    num_sockets = Column(Integer, nullable=false,default=0)
    num_cpu_cores = Column(Integer, nullable=false, default=0)
    num_cpu_threads = Column(Integer,default=0)
    cpu_freq_MHz = Column(String,default=0)
    processor_model = Column(String,default=None)
    status = Column(String, server_default="Active")
    created_on = Column(TIMESTAMP, nullable=false, server_default=text("CURRENT_TIMESTAMP"))
    last_updated = Column(TIMESTAMP, nullable=false, server_default=text("CURRENT_TIMESTAMP"))

