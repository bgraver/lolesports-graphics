from flask import Flask, send_from_directory, send_file, request
from werkzeug.utils import secure_filename
import graphs
import esports_lib as esports
import os

app = Flask(__name__)

@app.route('/graphs', methods=["GET", "POST"])
def post_graphs():
    if request.method == "GET":
        '''
        print("Got the request")
        startingTime = request.args.get('startingTime', '')
        window = esports.getFullGameWindow(gameId, startingTime)
        print("dealing with the window")
        graph = graphs.teamGoldLine(window, gameNumber)
        print("have the graph")
        
        path = os.getcwd()
        os.chdir("{0}/graphs".format(path))
        print(os.getcwd())'''
        fileName = request.args.get('fileName', '')
        return send_from_directory(
            directory='graphs',
            filename=fileName,
            mimetype='image/png'
        )
    return "Request again with a GET request"





