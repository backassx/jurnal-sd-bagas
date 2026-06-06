import random

users = [
    {"id": 1, "name": "Admin"},
    {"id": 2, "name": "User"}
]

def get_users():

    # Simulasi server sibuk
    if random.randint(1, 2) == 1:
        return {
            "status": "error",
            "message": "Server sedang sibuk"
        }

    return {
        "status": "success",
        "data": users
    }