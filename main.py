from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# @app.error_handler(404)

# list_doctor_data = sa.insert(db.ListDoctorClinic).values([
#     {"clinic_id":"1", "doctor_id":"1"},
#     {"clinic_id":"2", "doctor_id":"2"},
#     {"clinic_id":"1", "doctor_id":"3"},
#     {"clinic_id":"2", "doctor_id":"4"},
#     {"clinic_id":"1", "doctor_id":"5"},
#     {"clinic_id":"2", "doctor_id":"1"}
# ])

list_user_db = {
    "users":[
        {
            "id":1,
            "email": "andi@mail.com",
            "password": "anypassword",
            "first_name": "andi",
            "last_name": "cihuy",
            "full_name": "andi cihuy"
        },
        {
            "id":2,
            "email": "bejo@mail.com",
            "password": "nopassword"
            "first_name": "bejo",
            "last_name": "jokowi",
            "full_name": "bejo jokowi"
        },
        {
            "id":3,
            "email": "cindy@mail.com",
            "password": "passwordwrong"
        },
    ]
} 

@app.route('/', methods=['GET', 'POST'])

@app.route("/register", methods=['POST'])

def register():
    register_data = request.json
    # bentuk data register_data 
    # js = json
    # python = dict / dictionary
    email = register_data.get("email")
    password = register_data.get("password")
    first_name = register_data.get("first_name")
    last_name = register_data.get("last_name")
    full_name = f"{first_name} {last_name}"
    user_data = {
        ""
    }
    list_user_db["users"].update()
    return jsonify({"data": register_data, "message": f"{email} registered successfully", "success": True}), 201
    
    # if request.method == 'POST':
    #     name = request.form.get('name')
    #     email = request.form.get('email')
    #     password = request.f 
    #     # Check if the form data is valid
    #     if not name or not email or not password:
    #         return "All fields are required"

    #     # Store the user data in a database or file
    #     # For demonstration purposes, we'll just print the data
    #     print(f"Name: {name}")
    #     print(f"Email: {email}")
    #     print(f"Password: {password}")
 
    #     return "Registration successful"

    # return render_template('register.html'

def main():
    return render_template('index.html')

if __name__ == "__main__":
    main()


