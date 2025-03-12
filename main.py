from flask import Flask, request, render_template, jsonify
from datetime import datetime
import random

app = Flask(__name__)

list_user_db = {"users": [
    { 
        "id": 1,
        "created_at": "2025-09-08 15:00:00",
        "email": "andika@mail.com",
        "first_name": "andika",
        "last_name": "Septalonika",
        "full_name": "andika Septalonika",
        "password": "terserah gue"
    }
]}

def all_users_repository():
    return list_user_db.copy()

 
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

# def update_user(user_id):
#     update_data = request.json
#     email = update_data.get("email")
#     password = update_data.get("password")
#     first_name = update_data.get("first_name")
#     last_name = update_data.get("last_name")
#     full_name = f"{first_name} {last_name}"
#     user = next((user for user in list_user_db["users"] if user["id"] == user_id), None)
#     if user is None:
#         return jsonify({"data": [], "message": "User not found", "success": False, "status": 404}), 404
#     user["email"] = email
#     user["password"] = password
#     user["first_name"] = first_name
#     user["last_name"] = last_name
#     user["full_name"] = full_name
#     return jsonify({"data": user, "message": f"User {full_name} updated successfully", "success": True, "status": 200})

    
def delete_user(user_id):
    user = next((user for user in list_user_db["users"] if user["id"] == user_id), None)
    if user is None:
        return jsonify({"data": [], "message": "User not found", "success": False, "status": 404}), 404
    list_user_db["users"].remove(user)
    list_user = list_user_db["users"].copy()
    formatted_user_list = []
    for user in list_user:
        formatted_user_list.append(
            {
                "id": user["id"],
                "email": user["email"],
                "full_name": user["full_name"]
            }
        )
    return jsonify({"data": formatted_user_list, "message": f"User {user["full_name"]} deleted successfully", "success": True, "status": 202})


# @app.route("/users/<int:user_id>", methods=["GET"])

# def get_detail_user(user_id):
#     user = next((user for user in list_user_db["users"] if user["id"] == user_id), None)
#     if user is None:
#         return jsonify({"data": [], "message": "User not found", "success": False, "status": 404}), 404
#     return jsonify({"data": user, "message": "User data retrieved successfully", "success": True, "status": 200})

# @app.route("/users/<int:user_id>", methods=["PUT"])

# @app.route("/users/<int:user_id>", methods=["DELETE"])





@app.route('/')
def main():
    list_user = list_user_db["users"].copy()
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
        return render_template('index.html', list_user=[])
    return render_template('index.html', list_user=formatted_user_list)

if __name__ == "__main__":
    main()
