from CS361_Project.models import Account


def Account_Dict(modelObj):
    result = {
        "username": modelObj.username,
        "name": modelObj.name,
        "role": modelObj.role,
        "email": modelObj.email,
        "address": modelObj.address,
        "telephone": modelObj.telephone
    }
    return result
