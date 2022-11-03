
def Response(json_data, message, error):
    return {
        "data": json_data,
        "message": message,
        "error": error
    }
'''

import json
import xmltodict

def Response(data, message, error):
    if type (data) == list:
        json_data =data
    else:
        data_dict = xmltodict.parse(data)
        json_data = json.dumps(data_dict) #convert input dict into string
    return {
        "data": json_data,
        "message": message,
        "error": error
        
      *********************************
      create function 
      class compute1(BaseModel):
    huuid: int
    user: str
    url: str
    password: str
    hypervisor: str
    is_master: str
    status: Optional[Status]

update function 
class compute2(BaseModel):
    user: Optional[str]
    url: Optional[str]
    password: Optional[str]
    status: Optional[Status]
    ***************************************************  
        enum
        if sys.version_info >= (3, 7):
    from enum import Enum
    class SafeUUID(Enum):
        safe: int
        unsafe: int
        unknown: None
    }
       compute_model = models.compute()
        compute_model.huuid = compute.huuid
        compute_model.user = compute.user
        compute_model.url = compute.url
        compute_model.password = compute.password
        compute_model.hypervisor = compute.hypervisor
        compute_model.is_master = compute.is_master
        compute_model.memory_used = compute.memory_used
        compute_model.memory_total = compute.memory_total
        compute_model.cpu_used = compute.cpu_used
        compute_model.cpu_total = compute.cpu_total
        compute_model.uptime = compute.uptime
        compute_model.monthly_uptime = compute.monthly_uptime
        compute_model.total_uptime = compute.total_uptime
        compute_model.num_sockets = compute.num_sockets
        compute_model.num_cpu_cores = compute.num_cpu_cores
        compute_model.num_cpu_threads = compute.num_cpu_threads
        compute_model.cpu_freq_MHz = compute.cpu_freq_MHz
        compute_model.processor_model = compute.processor_model
        compute_model.status = compute.status
        
        
        
        
        list all compute 
                if data is not None:
            return Response(data, 'Compute retrieved successfully', False)
        return Response('Compute does not exist', 'Response Failed', True)

    except Exception as e:
        print(e)

**********************************************************
read the data in output 


  data = [{'user': computeput.user,
             'url': computeput.url,
             'password': computeput.password,
             'status':computeput.status}]
             
              data = [{'huuid': computepost.huuid,
                 'user': computepost.user,
                 'url': computepost.url,
                 'password': computepost.password,
                 'hypervisor': computepost.hypervisor,
                 'is_master': computepost.is_master}]

**********************************************

        class enlight_cloud(Base):

    __tablename__ = "enlight_cloud"
    huuid = Column(Integer, primary_key=True, index=True)
    user = Column(String, nullable=false)
    url = Column(String)
    password =Column(String)
    hypervisor = Column(String)
    is_master = Column(String,nullable=false,default=None)
    memory_used = Column(Boolean,nullable=false, default=None)
    memory_total = Column(Boolean, nullable=false,default=None)
    cpu_used =Column(Boolean, nullable=false,default=None)
    cpu_total =Column(Integer)
    uptime =Column(Integer,nullable=false,default=0)
    monthly_uptime =Column(String,nullable=false,default=0)
    total_uptime = Column(Integer,nullable=false,default=0)
    num_sockets = Column(Integer, nullable=false)
    num_cpu_cores = Column(Integer, nullable=false)
    num_cpu_threads = Column(Integer)
    cpu_freq_MHz = Column(String)
    processor_model =Column(String)
    status = Column(String, server_default="Active")
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    last_updated = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

        class enlight_cloud(BaseModel):
    huuid: int
    user: str
    url: str
    password: str
    hypervisor: str
    is_master: str
    memory_used: bool
    memory_total: bool
    cpu_used: bool
    cpu_total: int
    uptime: int
    monthly_uptime: str
    total_uptime: int
    num_sockets: int
    num_cpu_cores: int
    num_cpu_threads: int
    cpu_freq_MHz: str
    processor_model: str
    status: Optional[Status]
    created_on: datetime.datetime
    last_updated: datetime.datetime

   
@app.get("/meeting_room/{meetingroom_id}")
async def read_meeting_room_by_id(meeting_room_id: int, db: Session = Depends(get_db)):
    if meeting_room_id <= 0:
        return Response('Invalid meeting room id', 'Response Failed', True)
    try:
        data = db.query(models.meeting_room) \
            .filter(models.meeting_room.id == meeting_room_id) \
            .first()
    except Exception as e:
        print(e)
    if data is not None:
        return Response(data, f'Meeting Rooms retrieved successfully',False)
    return Response('The Meeting Room does not exist', 'Response Failed', True)


@app.get("/get_available_meetingrooms")
async def read_availability_meeting_room(meeting_room_availability: bool,db: Session = Depends(get_db)):
    try:
        data = db.query(models.meeting_room) \
            .filter(models.meeting_room.Active == meeting_room_availability) \
            .all()
    except Exception as e:
        print(e)
    if data is not None:
        return Response(data, f'Meeting Rooms retrieved successfully', False)
    return Response('The Meeting Room does not exist','Response Failed',True)

@app.post("/")
async def Create_Compute(meeting_room: meeting_room, db: Session = Depends(get_db)):
    try:
        meeting_room_model = models.meeting_room()
        meeting_room_model.Conference_room_name = meeting_room.Conference_room_name
        meeting_room_model.No_of_seats = meeting_room.No_of_seats
        meeting_room_model.Is_Projector_or_TV_availability = meeting_room.Is_Projector_or_TV_availability
        meeting_room_model.Location = meeting_room.Location
        meeting_room_model.Active = meeting_room.Active
        #meeting_room_model.Added_on = meeting_room.Added_on
        #meeting_room_model.Last_updated_on= meeting_room.Last_updated_on

        db.add(meeting_room_model)
        db.commit()
    except Exception as e:
        print(e)
    return Response(f'New meeting room with name {meeting_room_model.Conference_room_name} is get added',
                    'Meeting Room added successfully', False)

@app.put('/{meetingroom_id}')
async def Edite_Compute(meeting_room_id:int, meeting_room: meeting_room,db:Session = Depends(get_db)):
    if meeting_room_id <= 0:
        return Response('Invalid meeting room id', 'Response Failed', True)
    try:
        meeting_room_model= db.query(models.meeting_room)\
            .filter(models.meeting_room.id == meeting_room_id)\
            .first()
    except Exception as e:
        print(e)

    if meeting_room_model is None:
        return Response(f'No Meeting Room found with this id : {meeting_room_id}', 'Meeting Room not updated', True)


    meeting_room_model.Conference_room_name = meeting_room.Conference_room_name
    meeting_room_model.No_of_seats = meeting_room.No_of_seats
    meeting_room_model.Is_Projector_or_TV_availability = meeting_room.Is_Projector_or_TV_availability
    meeting_room_model.Locations = meeting_room.Locations
    meeting_room_model.Active = meeting_room.Active
    #meeting_room_model.Added_on = meeting_room.Added_on
    #meeting_room_model.Last_updated_on = meeting_room.Last_updated_on

    db.add(meeting_room_model)
    db.commit()
    print(meeting_room_model)
    return Response(f'New meeting room with id : {meeting_room_id} is get updated',
                    'Meeting Room updated successfully', False)

@app.delete("/{Compute_id}")
async def delete_Compute(meeting_room_id: int, db: Session = Depends(get_db)):
    if meeting_room_id <= 0:
        return Response('Invalid meeting room id', 'Response Failed', True)
    try:
        data=meeting_room_model = db.query(models.meeting_room) \
            .filter(models.meeting_room.id == meeting_room_id) \
            .first()
    except Exception as e:
        print(e)
    if meeting_room_model is None:
        return Response(f'No Meeting room found with this id : {meeting_room_id}','Meeting room not deleted', True)

    db.query(models.meeting_room) \
        .filter(models.meeting_room.id == meeting_room_id) \
        .delete()

    db.commit()
    return Response(data, f'Meeting Room {meeting_room_id} deleted successfully', False)


@app.put('/room/{meetingroom_id}')
async def release_meeting_room(meeting_room_id:int,db:Session = Depends(get_db)):
        if meeting_room_id <= 0:
            return Response('Invalid meeting room id','Response Failed',True)

        try:
            meeting_room_model= db.query(models.meeting_room)\
                .filter(models.meeting_room.id == meeting_room_id)\
                .first()
        except Exception as e:
            print(e)

        if meeting_room_model is not None:
            if meeting_room_model.Active is False:
                meeting_room_model.Active= True
                data=db.add(meeting_room_model)
                db.commit()
                return Response(f'Meeting room with id {meeting_room_id} is get free', 'Meeting Room update successful', False)
            if meeting_room_model.Active is True:
                return Response('This meeting room is already free','Response Failed',True)
            return Response('Meeting room does not exist','Response Failed',True)
        return Response('Meeting room does not exist','Response Failed',True)

@app.post('/meetingroom/{meetingroom_id}')
async def book_meeting_room(meeting_room_id:int,db:Session = Depends(get_db)):

        if meeting_room_id <= 0:
            return Response('Invalid meeting room id', 'Response Failed', True)
        try:
            meeting_room_model= db.query(models.meeting_room)\
                .filter(models.meeting_room.id == meeting_room_id)\
                .first()
        except Exception as e:
            print(e)

        if meeting_room_model is not None:
            if meeting_room_model.Active is True:
                meeting_room_model.Active= False
                data=db.add(meeting_room_model)
                db.commit()
                return Response(f'Meeting room with id {meeting_room_id} is get booked',
                                'Meeting Room update successful', False)
            if meeting_room_model.Active is False:
                return Response('This meeting room is already booked', 'Response Failed', True)
            return Response('Meeting room does not exist', 'Response Failed', True)
        return Response('Meeting room does not exist', 'Response Failed', True)

if __name__ == '_main_':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level="error", reload = True)
    print("running")
'''





