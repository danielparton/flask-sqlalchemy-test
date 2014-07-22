from flask import jsonify
from flask_app import app, db, models

@app.route('/getdata', methods=['GET'])
def get_data():
    rows = db.session.query(models.User).all()
    return_obj = {'users': []}
    for row in rows:
        return_obj['users'].append(row.username)
    print return_obj
    return jsonify(return_obj)
