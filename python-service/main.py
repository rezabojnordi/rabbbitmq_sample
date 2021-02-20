from flask import Flask
from flask import request
from flask import jsonify
from services.user_event_handler import emit_user_profile_update

app = Flask(__name__)

@app.route('/users')
def read_root():
    return 'List of users'

@app.route('/users/<string:user_id>', methods=['POST'])
def update(user_id:str):
    new_name = request.get_json()["full_name"]
    #new_name = request.form['full_name']
    # Update the user in the datastore using a local transaction...
    
    emit_user_profile_update(user_id, {'full_name': new_name})

    return jsonify({'full_name': new_name}), 201





if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True,port=80)
