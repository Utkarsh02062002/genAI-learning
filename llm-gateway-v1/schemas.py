from pydantic import BaseModel, Field
 
class UserCreate(BaseModel): # what is base model and why are we passing it as an argument here?
    username:str
    token_limit: int = Field(gt=0) # what is Field and meaning of gt=0, what else gt can take?
    # it let's you attach more validation rules, constraints and metadata to the attribute
    # gt is greater than, lt less than, multiple_of=10

class UserResponse(BaseModel):
    username: str
    token_limit: int    