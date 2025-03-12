from flask import Blueprint, jsonify, request

user_router = Blueprint("user_router", __name__, url_prefix="/users")

@user_router.route("/users", methods=["GET","POST"])
def show_users():
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