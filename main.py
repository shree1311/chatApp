import bottle
import json
import chat

@bottle.route('/')
def send_html():
  return bottle.static_file("index.html", root=".")

@bottle.route("/chat.js")
def send_frontEndJs():
  return bottle.static_file("chat.js", root = '.')

@bottle.route('/ajax.js')
def send_frontEndAJAX():
  return bottle.static_file('ajax.js', root='.')

@bottle.post('/addToChat')
def receiveNewMessage():
  contentJSON = bottle.request.body.read().decode()
  content = json.loads(contentJSON) #this is the dictionary {'message' : textFromTextBox}
  textFromTextBox = content['message']
  chat.add_message(textFromTextBox)
  return json.dumps( chat.get_chat() )

bottle.run(host="0.0.0.0", port = 8080, debug=True)