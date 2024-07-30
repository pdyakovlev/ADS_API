from pydantic import BaseModel


class AdCreate(BaseModel):
    header: str
    id: int
    author: str
    views: int
    position: int

    class Config:
        from_attributes = True


class AdRead(BaseModel):
    header: str
    id: int
    author: str
    views: int
    position: int

    class Config:
        from_attributes = True
