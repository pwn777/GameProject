# CST 205 - Lab 7
# Team: Byte Bistro
# April 4, 2016
hasKey = false
doorIsOpen = false

#runs the game in a continuous loop.
def playGame():
  displayHelp()
  currentRoom = getNextRoom("Den")
  prompt(currentRoom)
  while true:
    input = raw_input(" ")
    if input == "help":
      displayHelp()
      input = raw_input("Press any key to continue")
      continue
    elif input == "north" or input == "east" or input == "south" or input == "west":
      currentRoom = goDirection(currentRoom, input)
      prompt(currentRoom)
    elif input == "exit":
      break;
    elif input == "look":
      prompt(currentRoom)
    elif input == "open":
      if doesCommandExist(currentRoom, input):
        object = raw_input("What would you like to open?")
        string = ""
        for i in range(0, len(currentRoom[4])):
          if currentRoom[4][i] == object:
            string = executeCommand("open", object, currentRoom[5][i])
        if len(string):
          printNow(string)
        else:
          printNow("That object does not exist.")
      else:
        printNow("There is nothing to open in this room.")
      currentRoom = getNextRoom(currentRoom[0])
    else:
        printNow("I can't do that for you.")

#returns an array containing information about current room.
def getNextRoom(string):
  if string == "Den":
    return getDen()
  elif string == "Kitchen":
    return getKitchen()
  elif string == "Study":
    return getStudy()
  elif string == "Lounge":
    return getLounge()
  elif string == "Library":
    return getLibrary();
  elif string == "Ballroom":
    return getBallroom()
  elif string == "Conservatory":
    return getConservatory()
  elif string == "Deck":
    return getDeck()
    
def getLounge():
  return ["Lounge", ["north", "south", "west"], ["Library", "Kitchen", "Study"], "Welcome to room 4.", [], []]
def getDen():    
    return ["Den", ["north", "east"], ["Study", "Kitchen"], "Welcome. There is a large oriental rug in the center of the room and a cofee table. There is an unopened letter sitting on the table. You feel safe in this comfortable environment. ", ["letter"], ["\n(picks up letter)\nGreetings, You must escape this house. There is only one way out! HAHAHA!"]]
def getKitchen():
    return ["Kitchen", ["north", "west"], ["Lounge", "Den"], "You've entered the kitchen. There is a cabinet and a drawer.", ["cabinet", "drawer"], ["plate", "golden key"]]
def getStudy():
    return ["Study", ["south", "east"], ["Den", "Lounge"], "Welcome to room 3", [], []]

def getBallroom():
    return ["Ballroom", ["west"], ["Library"], "Welcome to room 6", [], []]
def getConservatory():
    return ["Conservatory", ["south", "west"], ["Library", "Deck"], "Welcome to room 7", ["chest"], ["rope"]]
def getDeck():
    return ["Deck", ["east"], ["Conservatory"], "You stand out on the deck. You would not survive the fall. If only you had some rope.", [], []]

def getLibrary():
    if doorIsOpen == true:
      return ["Library", ["north", "south", "east"], ["Conservatory", "Lounge", "Ballroom"], "You are in the library and you stand before the open gold door", ["door"], ["... wait the door is already open!"]]
    elif hasKey == true:
      return ["Library", ["south", "east"], ["Lounge", "Ballroom"], "You step into the library. A large door is north of you. It appears to be solid gold", ["door"], ["You try your golden key on the door and it opens easily. You have opened the golden door!"]]
    else:
      return ["Library", ["south", "east"], ["Lounge", "Ballroom"], "You step into the library. A large door is north of you.  It appears to be solid gold", ["door"], ["It wont budge. You need a key to open this door."]]
     

#executes command and returns a string
def executeCommand(command, container, object):
  if command == "open":
    if object == "golden key":
      global hasKey
      hasKey = true
    if container == "door":
      if hasKey == true:
        global doorIsOpen
        doorIsOpen = true
      return object
    if container == "letter":
       return object
    else:
      return "You have opened the " + container + " and found a(n) " + object

#detirmines if command exist
def doesCommandExist(room, command):
  return len(room[5])

def prompt(currentRoom):
    printNow("\nYou are currently in the " + currentRoom[0])
    printNow(currentRoom[3])
    printPossibleDirections(currentRoom)

#returns a room in a legal direction
def goDirection(cur, dir):
  for i in range(0, len(cur[1])):
    if cur[1][i] == dir:
      return getNextRoom(cur[2][i])
  return cur

#returns a list of all legal directions
def printPossibleDirections(room):
  output = "Your possible directions are: "
  rooms = ""
  for i in range(0, len(room[1])):
    if i == 0:
      rooms = rooms + room[1][i]
    else:
      rooms = rooms + ", " + room[1][i]
  printNow(output + rooms)
  printNow("Enter 'help' for more options")
            
#displays helpful options
def displayHelp():
  printNow("\n\nAvailable commands:\n'north', 'south', 'east', west, 'open', 'help' \nexit - Quit the game\n")

