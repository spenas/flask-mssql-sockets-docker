import socketio as sio
sio = sio.Client()
    
@sio.event
def connect():
  print('connection established')

@sio.on('message')
def on_message(data):
  print(data)

@sio.event
def disconnect():
    print('disconnected from server')  

sio.connect('http://localhost:4000')

