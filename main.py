
from enum import Enum
from typing import Optional

from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

from responses import Response

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        print(e)
    finally:
        db.close()


class Status(str, Enum):
    Active = 'Active'
    Inactive = 'Inactive'
    Maintenance = 'Maintenance'
    Populate = 'Populate'


class computepost(BaseModel):
    huuid: str = Field(None, title="Host Id", max_length=20,example="123ghjkjhg")
    user: str = Field(None, title="user", max_length=40,example="jagruti")
    url: str = Field(None, title="url", max_length=40,example="www.yahoo.com")
    password: str = Field(None, title="password", max_length=20,example="123@hmjhk")
    hypervisor: str = Field(None, title=" hypervisor", max_length=20,example="Xzen")
    is_master: str = Field(None, title="is_master", max_length=20,example="1")


class computeput(BaseModel):
    user: Optional[str]= Field(None, title="user", max_length=40,example="jagruti")
    url: Optional[str] = Field(None, title="url", max_length=40,example="www.yahoo.com")
    password: Optional[str] = Field(None, title="password", max_length=20,example="123@hmjhk")
    status: Optional[Status]


@app.get("/v1/Compute")
async def List_all_Compute(db: Session = Depends(get_db)):
    try:
        data = db.query(models.compute).all()
        if data is not None:
            return Response(data, 'Compute retrieved successfully', False)
        return Response('Compute does not exist', 'Response Failed', True)

    except Exception as e:
        print(e)


@app.post("/v1/Compute")
async def Create_Compute(computepost: computepost, db: Session = Depends(get_db)):
    try:
        compute_model = models.compute()
        compute_model.huuid = computepost.huuid
        compute_model.user = computepost.user
        compute_model.url = computepost.url
        compute_model.password = computepost.password
        compute_model.hypervisor = computepost.hypervisor
        compute_model.is_master = computepost.is_master
        db.add(compute_model)
        db.commit()
    except Exception as e:
        print(e)
    data = [{'huuid': computepost.huuid,
            'user': computepost.user,
            'url': computepost.url,
            'password': computepost.password,
            'hypervisor': computepost.hypervisor,
            'is_master': computepost.is_master}]

    return Response(data, 'compute added successfully', False)



@app.put('/V1/Compute')
async def Upadate_Compute(huuid: str, computeput: computeput, db: Session = Depends(get_db)):
    try:
        compute_model = db.query(models.compute) \
            .filter(models.compute.huuid == huuid) \
            .first()
    except Exception as e:
        print(e)

    if compute_model is None:
        return Response(f'No compute found with this id : {huuid}', 'compute not updated', True)

    if computeput.user != None:
        compute_model.user = computeput.user
    if computeput.url != None:
        compute_model.url = computeput.url
    if computeput.password != None:
        compute_model.password = computeput.password
    if computeput.status != None:
        compute_model.status = computeput.status

    db.add(compute_model)
    db.commit()
    print(compute_model)
    data = [{'user': computeput.user,
             'url': computeput.url,
             'password': computeput.password,
             'status': computeput.status}]

    return Response(data,'compute updated successfully', False)


@app.delete("/V1/Compute")
async def delete_Compute(huuid: str, db: Session = Depends(get_db)):
    try:
        data = compute_model = db.query(models.compute) \
            .filter(models.compute.huuid == huuid) \
            .first()
    except Exception as e:
        print(e)
    if compute_model is None:
        return Response(f'No compute found with this id : {huuid}', 'compute not deleted', True)

    db.query(models.compute) \
        .filter(models.compute.huuid == huuid) \
        .delete()

    db.commit()
    return Response(data, f'compute {huuid} deleted successfully', False)
