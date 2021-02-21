import flask
from bson import ObjectId
from flask import Flask, jsonify, request, redirect
from flask_pymongo import PyMongo
from datetime import datetime, timedelta
import jwt
import random
import string
from flask import request
from passlib.context import CryptContext

JWT_SECRET = 'CodePark1203'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20000000
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/CodeParkToDo"
mongo = PyMongo(app)
db_users = mongo.db.users

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

def get_random_password():
    random_source = string.ascii_letters + string.digits
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)

    # generate other characters
    for i in range(8):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


def encrypt_password(password):
    return pwd_context.encrypt(password)

def check_encrypted_password(password, hashed):
    print(pwd_context.verify(password, hashed))
    return pwd_context.verify(password, hashed)

def createdDefaultUsers():
    password=get_random_password()
    print(password)
    for i in range(5):
        username="Lavanaraj_" + str(i)
        if ((db_users.find_one({'username': username})) == None):
            user_details={
                'username': username,
                'password':encrypt_password(password),
                'jwttoken':""
            }
            db_users.insert_one(user_details)
    print("Users Created successfully")

def get_username(jwttoken):
    try:
        decode_jwttoken=jwt.decode(jwttoken, JWT_SECRET, JWT_ALGORITHM)
        return decode_jwttoken['username']
    except:
        return "Session Expired"

@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        user_detail = request.get_json()
    username=user_detail['username']
    password=user_detail['password']
    user_details = db_users.find_one({'username':username})
    if(user_details==None):
        result_value="Don't have user name"
    else:
        if(user_details['jwttoken']!= ''):
            result_value = "Already login"
        elif(check_encrypted_password(password,user_details['password'])):
            payload = {
                'username': username,
                'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
            }
            jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
            result_value=jwt_token
            updated_user = {"$set":{"jwttoken": result_value}}
            db_users.update_one(user_details, updated_user)
        else:
            result_value="Wrong password"
    result = {'result': result_value}
    return jsonify(result)


@app.route('/save_new_node', methods=['POST'])
def save_new_node():
    jwttoken=request.headers['Authorization']
    if request.is_json:
        node_details = request.get_json()
    user_details = db_users.find_one({'username':get_username(jwttoken)})
    note=node_details['note']
    if(user_details['jwttoken']==jwttoken):
        try:
            notes = {
                'note': note,
                'archive': False,
                '_id':ObjectId()
            }
            if(user_details['notes']!=None):
                db_users.update_one({"_id": user_details["_id"]}, {"$addToSet": {"notes": notes}})
        except:
            notes = {
                'note': note,
                'archive': False,
                '_id': ObjectId()
            }
            db_users.update_one({"_id":user_details["_id"]},{"$set":{"notes":[notes]}})
        result = {'message': "Note Saved Successfully!!!"}
    else:
        result = {'message': "Invalid JWT Token"}
    return jsonify(result)



@app.route('/update_note', methods=['POST'])
def update_note():
    jwttoken=request.headers['Authorization']
    if request.is_json:
        node_details = request.get_json()
    user_details = db_users.find_one({'username':get_username(jwttoken)})
    note=node_details['note']
    note_id=node_details['_id']
    if(user_details['jwttoken']==jwttoken):
        db_users.update_one({"_id": user_details['_id'],"notes":{"_id":ObjectId(note_id)}}, {"$Set": {"note": note}})
        result = {'message': "Note Update Successfully!!!"}
    else:
        result = {'message': "Invalid JWT Token"}
    return jsonify(result)

@app.route('/delete_note', methods=['POST'])
def delete_note():
    jwttoken=request.headers['Authorization']
    if request.is_json:
        node_details = request.get_json()
    user_details = db_users.find_one({'username':get_username(jwttoken)})
    note_id=node_details['_id']
    if(user_details['jwttoken']==jwttoken):
        db_users.delete_one({"notes._id": ObjectId(note_id)})
        result = {'message': "Note Successfully Deleted!!!"}
    else:
        result = {'message': "Invalid JWT Token"}
    return jsonify(result)

@app.route('/get_all_archived_nodes')
def get_all_archived_nodes():
    jwttoken=request.headers['Authorization']
    user_details = db_users.find_one({'username':get_username(jwttoken)})
    if(user_details['jwttoken']==jwttoken):
        notes=user_details["notes"]
        out_notes=[]
        for note in notes:
            if(note["archive"]==True):
                note["_id"]=str(note["_id"])
                out_notes.append(note)
    result = {'all_archived_nodes': out_notes}
    return jsonify(result)

@app.route('/get_all_unarchived_nodes')
def get_all_unarchived_nodes():
    jwttoken=request.headers['Authorization']
    user_details = db_users.find_one({'username':get_username(jwttoken)})
    if(user_details['jwttoken']==jwttoken):
        notes=user_details["notes"]
        out_notes=[]
        for note in notes:
            if(note["archive"]==False):
                note["_id"]=str(note["_id"])
                out_notes.append(note)
    result = {'all_unarchived_nodes': out_notes}
    return jsonify(result)

createdDefaultUsers()

if __name__ == '__main__':
    app.run(debug=True)