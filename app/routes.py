from fastapi import HTTPException, APIRouter
from connection import manager
from dal import * 

router = APIRouter()
manager.init_data()

@router.get('/employees/engineering/high-salary')
def get_engineering_high_salary():
    data = get_engineering_high_salary_employees()
    if data:
        return {"data":data}
    else:
        HTTPException(status_code=404,detail='no detail')


@router.get('/employees/by-age-and-role')
def get_employees():
    data = get_employees_by_age_and_role()
    if data:
        return {"data":data}
    else:
        HTTPException(status_code=404,detail='no detail')
        
@router.get('/employees/top-seniority')
def get_top_seniority_employees():
    data = get_top_seniority_employees_excluding_hr()
    if data:
        return {"data":data}
    else:
        HTTPException(status_code=404,detail='no detail')
   
@router.get('/employees/age-or-seniority')
def get_employees_age_or_seniority():
    data = get_employees_by_age_or_seniority()
    if data:
        return {"data":data}
    else:
        HTTPException(status_code=404,detail='no detail')
   
@router.get('/employees/managers/excluding-departments')
def get_managers():
    data = get_managers_excluding_departments()
    if data:
        return {"data":data}
    else:
        HTTPException(status_code=404,detail='no detail')
   
@router.get('/employees/by-lastname-and-age')
def get_employees_by_lastname():
    data = get_employees_by_lastname_and_age()
    if data:
        return {"data":data}
    else:
        HTTPException(status_code=404,detail='no detail')
   