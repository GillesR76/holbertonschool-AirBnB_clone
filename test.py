#!/usr/bin/python3
from models.user import User
from models.base_model import BaseModel

user = User(email="test@example.com", password="password123", first_name="John", last_name="Doe")
mod = BaseModel()
print(user.to_dict())
print("--------------")
print(mod.to_dict())