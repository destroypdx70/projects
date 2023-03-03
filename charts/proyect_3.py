options = "computer", "cell phone", "wire"

def message_creator(text):
  text.lower()
  if (text == options[0]):
    print("With this computer you can learn Python")
  if (text == options[1]):
    print("In my cell phone I can learn with any app")
  if (text == options[2]):
    print("There is a wire in my bot")

text = 'computer'
response = message_creator(text)
print(response)