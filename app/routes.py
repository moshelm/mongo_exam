from fastapi import APIRouter
from connection import manager


router = APIRouter()
manager.init_data()

