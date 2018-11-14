from flask import jsonify


class CpfInvalido(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

    def error(self, msg):
        message = { 
            'status': 501,  
            'message':  msg }
        resp = jsonify(message)
        resp.status_code = 501
        return resp