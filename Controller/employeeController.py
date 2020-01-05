from flask import jsonify
from bson.json_util import dumps

class employee:

    def __init__(self, app, PyMongo):
        self.mongo = PyMongo(app)

    def get_emp(self):
        dbinst = self.mongo
        online_users = dbinst.db.employee.find({"gender": "male"})
        return dumps(online_users)




        