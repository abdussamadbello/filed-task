from pydantic import  BaseModel,ValidationError,validator,PositiveInt,conlist,constr,Field
from datetime import datetime


class Song(BaseModel):
    name: constr(max_length=100) 
    duration:PositiveInt=...
    upload_time:datetime=...

    @validator('upload_time')
    def check_sum(cls, v):
        if v < datetime.now(v.tzinfo):   
            raise ValueError('time cannot be in the past')
        return v

class AudioBook(BaseModel):
    title: constr(max_length=100) = ...
    author: constr(max_length=100) = ...   
    narrator: constr(max_length=100) = ...
    duration:PositiveInt = ...
    upload_time:datetime = ...

class Podcast(BaseModel):
    name: constr(max_length=100) = ...
    host: constr(max_length=100) = ...
    Participants: conlist(constr(max_length=10), max_items=10) = ...
    duration:PositiveInt = ...
    upload_time:datetime = ...
  