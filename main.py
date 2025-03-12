from flask import Flask, render_template
from models.user import list_user_db
from routers.user import user_router

app = Flask(__name__)
app.register_blueprint(user_router)

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

    
# def delete_user(user_id):
#     user = next((user for user in list_user_db["users"] if user["id"] == user_id), None)
#     if user is None:
#         return jsonify({"data": [], "message": "User not found", "success": False, "status": 404}), 404
#     list_user_db["users"].remove(user)
#     list_user = list_user_db["users"].copy()
#     formatted_user_list = []
#     for user in list_user:
#         formatted_user_list.append(
#             {
#                 "id": user["id"],
#                 "email": user["email"],
#                 "full_name": user["full_name"]
#             }
#         )
#     return jsonify({"data": formatted_user_list, "message": f"User {user["full_name"]} deleted successfully", "success": True, "status": 202})


# @app.route("/users/<int:user_id>", methods=["GET"])

# def get_detail_user(user_id):
#     user = next((user for user in list_user_db["users"] if user["id"] == user_id), None)
#     if user is None:
#         return jsonify({"data": [], "message": "User not found", "success": False, "status": 404}), 404
#     return jsonify({"data": user, "message": "User data retrieved successfully", "success": True, "status": 200})

# @app.route("/users/<int:user_id>", methods=["PUT"])

# @app.route("/users/<int:user_id>", methods=["DELETE"])