# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# Import modules
from lib.hello import Hello
from lib.square import Square
from lib.openapi import OpenAPI

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

# adding the defined resources along with their corresponding urls
api.add_resource(Hello, "/")
api.add_resource(Square, "/square/<int:num>")
api.add_resource(OpenAPI, "/openai")

# driver function
if __name__ == "__main__":
    ####### LIVE
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=80, debug=True)
    ####### DEBUG ONLY
    app.run(host="0.0.0.0", port=80, debug=True)
