# CST 205 - Lab 7
# Team: Byte Bistro
# April 4, 2016

#runs the game in a continuous loop.
def playGame():
  displayHelp()
  currentRoom = getNextRoom("Home")

  while true:
    printNow("\nYou are currently in the " + currentRoom[0])
    printNow(currentRoom[3])
    printPossibleDirections(currentRoom)
    
    input = raw_input("What would you like to do (i.e 'north', 'south', 'open', 'help'?")
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
    else:
        printNow("Invalid command. Try again.")

#returns an array containing information about current room.
def getNextRoom(string):
  if string == "Home":
    return ["Home", ["north", "east"], ["Study", "Kitchen"], "Welcome home. You feel safe in this comfortable environment.", [], []]
  elif string == "Kitchen":
    return ["Kitchen", ["north", "west"], ["Lounge", "Home"], "You've entered the kitchen. There is a cabinet and a drawer.", ["cabinet", "drawer"], ["a plate", "a golden key"]]
  elif string == "Study":
    return ["Study", ["south", "east"], ["Home", "Lounge"], "Welcome to room 3", [], []]
  elif string == "Lounge":
    return ["Lounge", ["north", "south", "west"], ["Library", "Kitchen", "Study"], "Welcome to room 4.", [], []]
  elif string == "Library":
    return ["Library", ["north", "south", "east"], ["Conservatory", "Lounge", "Ballroom"], "Welcome to room 5", [], []]
  elif string == "Ballroom":
    return ["Ballroom", ["west"], ["Library"], "Welcome to room 6", [], []]
  elif string == "Conservatory":
    return ["Conservatory", ["south", "west"], ["Library", "Deck"], "Welcome to room 7", [], []]
  elif string == "Deck":
    return ["Deck", ["east"], ["Conservatory"], "Welcome to room 8", [], []]

#executes command and returns a string
def executeCommand(command, container, object):
  if command == "open":
    return "You have opened the " + container + " and found a(n) " + object

#detirmines if command exist
def doesCommandExist(room, command):
  return len(room[5])

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
            
#displays helpful options
def displayHelp():
  printNow("Available commands:\nhelp - List all possible commands\nexit - Quit the game\n")

