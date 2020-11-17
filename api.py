from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import graphs
import esports_lib as esports
import os

app = Flask(__name__)

@app.route('/graphs', methods=["GET", "POST"])
def post_graphs():
    if request.method == "GET":
        fileName = request.args.get('fileName', '')
        '''
                return send_from_directory(
            directory='graphs',
            filename=fileName,
            mimetype='image/png'
        )
        '''
        return fileName
    return "Request again with a GET request"


@app.route('/fullWindow', methods=['GET', 'POST'])
def post_full_window():
    if request.method == "GET":
        print("got it")
        matchId = request.args.get('matchId', '')
        startingTime = request.args.get('startingTime', '')
        # output = esports.getWindow(matchId, startingTime)
        # output = esports.getFullGameWindow(matchId, startingTime)
        # print(output)
        return jsonify(esports.getFullGameWindow(matchId, startingTime))
    return "Request again with a GET request"
