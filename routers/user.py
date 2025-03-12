from flask import Blueprint, jsonify, request
from views.user import get_users, create_user, delete_user, update_user

user_router = Blueprint("user_router", __name__, url_prefix="/api/v1/users")

@user_router.route("", methods=["GET","POST"])
def get_all_users():
    match request.method.lower():
        case "get":
            user_list = get_users()
            if len(user_list) < 1:
                return jsonify({"data": [], "message": "No Data!", "success": True, "status": 204})
            return jsonify({"data": user_list, "message": "User data retrieved successfully", "success": True, "status": 200})
        case "post":
            return create_user()
        case default:
            return jsonify({"message": "Invalid request method", "success": False, "status": 405})
@user_router.route("/<int:user_id>", methods=["GET", "DELETE", "PUT"])
def get_detail_user(user_id):
    match request.method.lower():
        case "get":
            user_list = get_users()
            user = next((user for user in user_list if user["id"] == user_id), None)
            if user is None:
                return jsonify({"data": [], "message": "User not found", "success": False, "status": 404}), 404
            return jsonify({"data": user, "message": "User data retrieved successfully", "success": True, "status": 200})
        case "delete":
            return delete_user(user_id)
        case "put":
            return update_user(user_id)
        case default:
            return jsonify({"message": "Invalid request method", "success": False, "status": 405})