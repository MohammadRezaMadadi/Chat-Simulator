from flask import flask
from flask_socketio import SocketIO

app = Flask(__name__)
socket = SocketIO(app)
app.config["SECRETKEY"] = "rezamadadi"

@app.route("/")
def sessions():
    return render_tamplate("session.html")

def msg_recvd(method = ['GET','POST']):
    print ('Message was recieved.!!')

@socketio.on('my event')
def handle_my_event(json , method = ['GET','POST']):
    print('Recieve my event :' + str(json))
    socketio.emit('my response' , json , callback = msg_recvd)

if __name__ == "__main__":
    socketio.run(app , debug = True)
