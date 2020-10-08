# should be able to edit this and it should stil work
starting = [[2,1],[4,3],[6,5]]

class tohInstance():
    def __init__(self):
        self.state = starting
        self.won = 0
    # gets the last number in arr, this is used to get the "top" ring
    def getlast(self,pos:int):
        posObj = self.state[pos]
        return posObj[len(posObj)-1]
    # scuffed check, basically goes through all towers and checks if the length 
    # is 6 (if they all are on it), which should work because it does not move unless 
    # it makes sense in the games rules.
    def checkIfWin(self):
        outcome = 0
        ammount = sum([len(i) for i in starting]) # should be sum of all array values
        for tower in self.state:
            if len(tower) == ammount:
                self.won = 1
                outcome = 1
                break
        return outcome
    # move top ring from a tower to another
    def move(self,pos:int,newPos:int):
        posObj = self.state[pos]
        newPosObj = self.state[newPos]
        if pos == newPos:
            return 1 #ok, but do nothing
        if self.getlast(newPos) < self.getlast(pos): 
            #ok, remove from old tower and add to new
            newPosObj.append( self.getlast(pos) )
            posObj.remove( self.getlast(pos) )
            if self.checkIfWin() == 1:
                return 2 
            return 1 
        else:
            # bad move, return 0
            return 0
# check if input is valid
def inputHandler(out):
    secA = out.split(" ")
    if len(secA) != 2:
        return 0
    if secA[0].isdigit() and secA[1].isdigit():
        return 1
    return 0
# statr the game
game = tohInstance()
def play():
    print("Current state : ", game.state)
    inp = input("Where would you like to move eg: 1 2 , 3 1\n")
    isValid = inputHandler(inp)
    if (isValid != 1):
        print("Invalid input")
        return play()
    # parse to int
    pos1 = int(inp.split(" ")[0])-1
    pos2 = int(inp.split(" ")[1])-1
    outcome = game.move(pos1,pos2)
    if outcome == 0 :
        print("Unable to move to that location")
    elif outcome == 2:
        return print("You have won!")
    play()    
play()