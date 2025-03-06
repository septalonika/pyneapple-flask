from flask import Flask, request, render_template, jsonify
import random

app = Flask(__name__)

# @app.error_handler(404)

# list_user_db = {
#     "users": [
#         {
#             "id": 1,
#             "email": "andi@mail.com",
#             "password": "anypassword",
#             "first_name": "andi",
#             "last_name": "cihuy",
#             "full_name": "andi cihuy"
#         },
#         {
#             "id": 2,
#             "email": "bejo@mail.com",
#             "password": "nopassword",
#             "first_name": "bejo",
#             "last_name": "jokowi",
#             "full_name": "bejo jokowi"
#         },
#         {
#             "id": 3,
#             "email": "cindy@mail.com",
#             "password": "passwordwrong"
#         },
#     ]
# }

list_user_db = {"users": []}

@app.route('/', methods=['GET', 'POST'])

@app.route("/register", methods=['POST'])

def register():
    register_data = request.json
    email = register_data.get("email")
    password = register_data.get("password")
    first_name = register_data.get("first_name")
    last_name = register_data.get("last_name")
    full_name = f"{first_name} {last_name}"
    user_data = {
        "id": random.randint(1, 1000),
        "email": email,     
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name,
        "created_at": "2022-09-08 15:00:00"
    }
    list_user_db["users"].append(user_data)
    return jsonify({"data": list_user_db, "message": f"{email} registered successfully", "success": True}), 201

@app.route("/users", methods=["GET"])

def get_users():
    return jsonify({"data": list_user_db, "message": "User data retrieved successfully", "success": True})
    

def main():
    return render_template('index.html')

if __name__ == "__main__":
    main()


