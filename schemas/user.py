def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "frase": item["frase"],
        "autor": item["autor"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]