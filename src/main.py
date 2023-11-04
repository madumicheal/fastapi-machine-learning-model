from typing import List
from uuid import UUID
from fastapi import FastAPI
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("58e0f71f-b6de-4dc4-89cb-547fd79c6c0c"),
        first_name ="Micheal",
        last_name ="Madu",
        gender =Gender.male,
        roles =[Role.student]
    ),
    
    User(
        id=UUID("4335dd42-70b2-4426-b31f-20d7ac01b6ac"),
        first_name ="Esther",
        last_name ="Joy",
        gender =Gender.female,
        roles = [Role.admin, Role.user]
    )
]

@app.get("/") #root 
async def root():
    return{"Hello": "Micheal"}

@app.get("/api/v1/users") # returns a dictionary of all the users in the DB
async def fetch_users():
    return db;
    
@app.post("/api/v1/users") # this method allows for including new user details
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users(user_id)") #deletes user details
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )