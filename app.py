from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

PROFILE_FILE = "profiles.json"


def read_profiles():
    file = open(PROFILE_FILE, "r")
    profiles = json.load(file)
    file.close()
    return profiles


def write_profiles(profiles):
    file = open(PROFILE_FILE, "w")
    json.dump(profiles, file, indent=4)
    file.close()


@app.route("/profile", methods=["POST"])
def save_profile():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Missing JSON"}), 400

    user_id = data.get("user_id")
    username = data.get("username")
    email = data.get("email")

    if user_id is None or user_id == "":
        return jsonify({"error": "user_id is required"}), 400

    if username is None or username == "":
        return jsonify({"error": "username is required"}), 400

    if email is None or email == "":
        return jsonify({"error": "email is required"}), 400

    location = data.get("location")
    favorite_pet_type = data.get("favorite_pet_type")

    profile = {
        "user_id": user_id,
        "username": username,
        "email": email,
        "location": location,
        "favorite_pet_type": favorite_pet_type
    }

    profiles = read_profiles()

    found_profile = False

    for i in range(len(profiles)):
        if profiles[i]["user_id"] == user_id:
            profiles[i] = profile
            found_profile = True

    if found_profile == False:
        profiles.append(profile)

    write_profiles(profiles)

    return jsonify({
        "message": "Profile saved successfully",
        "profile": profile
    }), 201


@app.route("/profile", methods=["GET"])
def get_profile():
    user_id = request.args.get("user_id")

    if user_id is None or user_id == "":
        return jsonify({"error": "user_id is required"}), 400

    profiles = read_profiles()

    for profile in profiles:
        if profile["user_id"] == user_id:
            return jsonify({"profile": profile}), 200

    return jsonify({"error": "Profile not found"}), 404


if __name__ == "__main__":
    app.run(port=5006, debug=True)