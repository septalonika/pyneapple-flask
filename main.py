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