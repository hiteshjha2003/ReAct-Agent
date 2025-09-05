from pydantic import BaseModel , Field
import sys 
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .enums import Name

class Message(BaseModel):
    role: str = Field(... , description= "Sender role")
    content :str = Field(..., description="Message Content")

class Choice(BaseModel):
    name:Name
    reason:str

