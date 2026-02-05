from connection import manager



def get_engineering_high_salary_employees():
    projection = {"employee_id":1,'name':1,"salary":1}
    query = {"$and":[{'salary':{"$gt":65000}},{'job_role.department':'Engineering'}]}
    res = list(manager.collection.find(query, projection))
    convert_objectId(res)
    return res


def get_employees_by_age_and_role():
    query = {"$and":[{"age":{"$gte":30}},{"age":{"$lte":45}},{"job_role.title":{"$in":["Specialist","Engineer"]}}]}
    res = list(manager.collection.find(query))
    convert_objectId(res)
    return res


def get_top_seniority_employees_excluding_hr():
    query = {'job_role.department':{"$ne":"HR"}}
    res = list(manager.collection.find(query).sort({'years_at_company':-1}).limit(7))
    convert_objectId(res)
    return res


def get_employees_by_age_or_seniority():
    projection = {"employee_id":1,'name':1,"age":1,"years_at_company":1}
    query = {"$or":[{'age':{"$gt":50}},{'years_at_company':{"$lt":3}}]}
    res = list(manager.collection.find(query, projection))
    convert_objectId(res)
    return res

def get_managers_excluding_departments():
    query = {"$and":[{'job_role.title':"Manager"},{"job_role.department":{"$not":{"$in":["Sales","Marketing"]}}}]}
    res = list(manager.collection.find(query))
    convert_objectId(res)
    return res

def get_employees_by_lastname_and_age():
    projection = {'name':1,"age":1,"jon=b_role.department":1}
    query = {"$and":[{'age':{"$lt":35}},{"$or":[{'name':{"$regex":"Wright"}},{"name":{"$regex":"Nelson"}}]}]}
    res = list(manager.collection.find(query, projection))
    convert_objectId(res)
    return res

# helper function
def convert_objectId(docs:list):
    for doc in docs:
        doc["_id"] = str(doc["_id"])


