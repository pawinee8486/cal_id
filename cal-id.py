from flask import Flask,request
from flask_restful import Resource ,Api ,reqparse

app= Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

parser = reqparse.RequestParser()
parser.add_argument('ID')

def convertToBinary(n):
   return bin(n)[2:]
class studentidToBinary(Resource):
        def post(self):
                args = parser.parse_args()
                studentid = args['ID']
                #studentid_d = int(ID)
		#Don't have variable > ID <
		studentid_d = int(studentid)
                studentid_b = convertToBinary(studentid_d)

                return {"studentid":studentid_b}

api.add_resource(studentidToBinary,'/api/studentid-to-binary')


if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5001)
