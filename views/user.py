import random
from datetime import datetime
from flask import jsonify, request
from repositories.user import all_users_repository, list_user_db


def get_users():
    list_user = all_users_repository()["users"]
    formatted_user_list = []
    for user in list_user:
        formatted_user_list.append(
            {
                "id": user["id"],
                "email": user["email"],
                "full_name": user["full_name"]
            }
        )
    if len(formatted_user_list) < 1:
        return []
    return formatted_user_list

def create_user():
    try:
        register_data = request.json
        email = register_data.get("email")
        password = register_data.get("password")
        first_name = register_data.get("first_name")
        last_name = register_data.get("last_name")
        full_name = f"{first_name} {last_name}"
        
        list_user = get_users()
        if any(user["email"] == email for user in list_user):
            return jsonify({"message": "Email already registered", "success": False, "status": 409}), 409
        if not first_name:
            return jsonify({"message": "First name is required", "success": False, "status": 400}), 400
        if not last_name:
            return jsonify({"message": "Last name is required", "success": False, "status": 400}), 400
        if not email:
            return jsonify({"message": "Email is required", "success": False, "status": 400}), 400
        if not password:
            return jsonify({"message": "Password is required", "success": False, "status": 400}), 400
        if len(password) < 8:
            return jsonify({"message": "Password must be at least 8 characters long", "success": False, "status": 400}), 400
        user_data = {
            "id": random.randint(1, 1000),
            "email": email,     
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
            "full_name": full_name,
            "created_at": datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        }
        list_user_db["users"].append(user_data)
        formatted_user_list = {
            "id": user_data["id"],
            "email": user_data["email"],
            "full_name": user_data["full_name"]
        }
        return jsonify({"data": formatted_user_list, "message": f"User {formatted_user_list["full_name"]} created", "success": True, "status": 201})
    except:
        return jsonify({"data": [], "message": "user failed to create", "success": False, "status": 500})