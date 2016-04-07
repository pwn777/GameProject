# CST 205 - Lab 7
# Team: Byte Bistro
# April 4, 2016
hasGoldenKey = false
hasHairPin = false
hasRope = false
doorIsOpen = false
windowIsOpen = false
gameRun = true

def playGame():
  displayHelp()
  currentRoom = getNextRoom("Den")
  prompt(currentRoom)
  while gameRun:
    input = raw_input("What would you like to do? ")
    if input == "help":
      displayHelp()
      input = raw_input("Press any key to continue. ")
      prompt(currentRoom)
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
        object = raw_input("What would you like to open? ")
        string = ""
        for i in range(0, len(currentRoom[4])):
          if currentRoom[4][i] == object:
            string = executeCommand("open", object, currentRoom[5][i])
        if len(string):
          printNow(string)
        else:
          printNow("That object does not exist. ")
      else:
        printNow("There is nothing to open in this room. ")
      currentRoom = getNextRoom(currentRoom[0])
    else:
        printNow("I can't do that for you. ")

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
  return ["Lounge", ["north", "south", "west"], ["Library", "Kitchen", "Study"], "You've entered the Lounge.  A portrait of a man hangs in the center.  It feels like someone is watching you.", ["portrait"], ["\nThere is nothing behind this portrait, your imagination is playing with your head"]]

def getDen():    
    return ["Den", ["north", "east"], ["Study", "Kitchen"], "You've entered the Den. There is a large oriental rug in the center of the room and a coffee table. There is an unopened letter sitting on the table.", ["letter"], ["\n(picks up letter)\nGreetings, You must escape this house. There is only one way out! HAHAHA!"]]

def getKitchen():
    return ["Kitchen", ["north", "west"], ["Lounge", "Den"], "You've entered the kitchen. There is a cabinet and a drawer.", ["cabinet", "drawer"], ["plate", "golden key"]]

def getStudy():
    return ["Study", ["south", "east"], ["Den", "Lounge"], "You've entered the study.  There is a book on the table and a bottled beverage.  You take a seat and rest for a bit.", ["book","beverage"], ["hair pin", "You open the beverage and take a sip.  A sharp pain roars through your chest and you fall to the floor grasping for air.\nYou died.  Better luck next time!"]]

def getBallroom():
    return ["Ballroom", ["west"], ["Library"], "Music is playing faintly from a jukebox, but no one is around.  You get an eerie feeling down your spine.  ", [], []]

def getConservatory():
    if windowIsOpen == true:
      return ["Conservatory", ["south", "west"], ["Library", "Deck"], "You've entered the conservatory.  On the west side of the room you see the open window that leads to a deck.  A chest sits next to it.", ["window","chest"], ["The window is already open! A slight breeze enters the room.", "rope"]]  
    elif hasHairPin == true:
      return ["Conservatory", ["south"], ["Library"], "You've entered the conservatory.  On the west side of the room you see a window that leads to a deck.  A chest sits next to it.", ["window","chest"], ["You try to pick the lock with the hair pin. 'click' You've opened the window!", "rope"]]
    else:
      return ["Conservatory", ["south"], ["Library"], "You've entered the conservatory.  On the west side of the room you see a window that leads to a deck.  A chest sits next to it.", ["window","chest"], ["The window is locked. Only if you had something to pick the lock. Maybe you should get some rest.","rope"]]

def getDeck():
    if hasRope == true:
      printNow("You use the rope to climb down from the deck.  You reached the ground safely.  You've escaped the mansion.")
      global gameRun
      gameRun = false   
      return ["clear!", ["endless"], [""], "You won!", [], []]
    else: 
      return ["Deck", ["east"], ["Conservatory"], "You stand out on the deck. You would not survive the fall. If only you had some rope.", [], []]

def getLibrary():
    if doorIsOpen == true:
      return ["Library", ["north", "south", "east"], ["Conservatory", "Lounge", "Ballroom"], "You are in the library and you stand before the open gold door", ["door"], ["... wait the door is already open!"]]
    elif hasGoldenKey == true:
      return ["Library", ["south", "east"], ["Lounge", "Ballroom"], "You step into the library. A large door is north of you. It appears to be solid gold", ["door"], ["You try your golden key on the door and it opens easily. You have opened the golden door!"]]
    else:
      return ["Library", ["south", "east"], ["Lounge", "Ballroom"], "You step into the library. A large door is north of you.  It appears to be solid gold", ["door"], ["It wont budge. You need a key to open this door."]]
    

def executeCommand(command, container, object):
  if command == "open":
    if object == "golden key":
      global hasGoldenKey
      hasGoldenKey = true
    if object == "hair pin":
      global hasHairPin
      hasHairPin = true
    if object == "rope":
      global hasRope
      hasRope = true
    if container == "door":
      if hasGoldenKey == true:
        global doorIsOpen
        doorIsOpen = true
      return object
    if container == "window":
      if hasHairPin == true:
        global windowIsOpen
        windowIsOpen = true
      return object
    if container == "letter":
       return object
    else:
      return "You have opened the " + container + " and found a(n) " + object

def doesCommandExist(room, command):
  return len(room[5])

def prompt(currentRoom):
    printNow("\nYou are currently in the " + currentRoom[0])
    printNow(currentRoom[3])
    printPossibleDirections(currentRoom)

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
  printNow("Enter 'help' for more options")
            
def displayHelp():
  printNow("You open your eyes and find yourself in an unfamilliar mansion.  You can't remember what happened to you.  You take a look around and wonder 'Where am I'.") 
  printNow("\nAvailable commands:\n'north', 'south', 'east', 'west', 'open', 'help' \nexit - Quit the game")
