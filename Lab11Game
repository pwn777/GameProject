# CST 205 - Lab 7
# Team: Byte Bistro
# April 4, 2016
hasKey = false
doorIsOpen = false

def playGame():
  displayHelp()
  currentRoom = getNextRoom("Home")

  while true:
    printNow("\nYou are currently in the " + currentRoom[0])
    printNow(currentRoom[3])
    printPossibleDirections(currentRoom)
    
    input = raw_input("What would you like to do (i.e 'north', 'south', 'open', 'help'?   ")
    if input == "help":
      displayHelp()
    elif input == "north" or input == "east" or input == "south" or input == "west":
      currentRoom = goDirection(currentRoom, input)     
    elif input == "exit":
      break;
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
        printNow("Invalid command. Try again.")

def getNextRoom(string):
  if string == "Home":
    return ["Home", ["north", "east"], ["Study", "Kitchen"], "Welcome home. You feel safe in this comfortable environment.", [], []]
  elif string == "Kitchen":
    return ["Kitchen", ["north", "west"], ["Lounge", "Home"], "You've entered the kitchen. There is a cabinet and a drawer.", ["cabinet", "drawer"], ["plate", "golden key"]]
  elif string == "Study":
    return ["Study", ["south", "east"], ["Home", "Lounge"], "Welcome to room 3", [], []]
  elif string == "Lounge":
    return ["Lounge", ["north", "south", "west"], ["Library", "Kitchen", "Study"], "Welcome to room 4.", [], []]
  elif string == "Library":
    printNow(doorIsOpen)
    if doorIsOpen == true:
      return ["Library", ["north", "south", "east"], ["Conservatory", "Lounge", "Ballroom"], "You are in the library and you stand before the open gold door", ["door"], ["... wait the door is already open!"]]
    elif hasKey == true:
      return ["Library", ["south", "east"], ["Lounge", "Ballroom"], "You step into the library. A large golden door is north of you", ["door"], ["You have opened the door"]]
    else:
      return ["Library", ["south", "east"], ["Lounge", "Ballroom"], "You step into the library. A large golden door is north of you", ["door"], ["clue. You need a key to open this door!"]]
  elif string == "Ballroom":
    return ["Ballroom", ["west"], ["Library"], "Welcome to room 6", [], []]
  elif string == "Conservatory":
    return ["Conservatory", ["south", "west"], ["Library", "Deck"], "Welcome to room 7", [], []]
  elif string == "Deck":
    return ["Deck", ["east"], ["Conservatory"], "Welcome to room 8", [], []]

def executeCommand(command, container, object):
  if command == "open":
    if object == "golden key":
      global hasKey
      hasKey = true
    if container == "door":
      if hasKey == true:
        global doorIsOpen
        doorIsOpen = true
        return "You have opened the golden door!"
    return "You have opened the " + container + " and found a(n) " + object

def doesCommandExist(room, command):
  return len(room[5])

def goDirection(cur, dir):
  for i in range(0, len(cur[1])):
    if cur[1][i] == dir:
      return getNextRoom(cur[2][i])
  return cur

def printPossibleDirections(room):
  output = "Your possible directions are: "
  rooms = ""
  for i in range(0, len(room[1])):
    if i == 0:
      rooms = rooms + room[1][i]
    else:
      rooms = rooms + ", " + room[1][i]
  printNow(output + rooms)
            
def displayHelp():
  printNow("Available commands:\nhelp - List all possible commands\nexit - Quit the game\n")

