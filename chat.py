chatHistoryFile = "chat.txt"

def add_message(message):
  with open(chatHistoryFile,'a') as f:
    f.write(message + '\n')

def get_chat():
  full_chat = []
  with open(chatHistoryFile) as f:
    for line in f:
      full_chat.append({"message" : line.rstrip("\n\r") } )
  return full_chat