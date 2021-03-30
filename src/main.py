"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, To_do
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/get_to_do', methods=['GET'])
def get_task_to_do():

    get_task = To_do.query.all()
    all_tasks = list(map(lambda x: x.serialize(), get_task))
    return jsonify(all_tasks), 200

@app.route('/post_to_do', methods=['POST'])
def post_to_do():

    request_body = request.get_json()
    post_task = To_do(label=request_body["label"], done=request_body["done"])
    db.session.add(post_task)
    db.session.commit()

    return jsonify("New To Do added!"), 200

@app.route('/del_to_do/<int:fid>', methods=['DELETE'])
def del_to_do(fid):
    
    task = To_do.query.filter_by(id = numb).first()
    if task is None:
        raise APIException('Not found', status_code=405)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"Task deleted": numb}), 200
    

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)