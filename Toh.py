starting = [[1,2],[3,4],[5,6]]

class tohInstance():
    def __init__(self):
        self.state = starting
        self.won = 0
    def getlast(self,pos:int):
        posObj = self.state[pos]
        return posObj[len(posObj)-1]
    def checkIfWin(self):
        outcome = 0
        for tower in self.state:
            if len(tower) == 9:
                self.won = 1
                outcome = 1
                break
        return outcome
    def move(self,pos:int,newPos:int):
        posObj = self.state[pos]
        newPosObj = self.state[newPos]
        if pos == newPos:
            return 1
        if self.getlast(newPos) < self.getlast(pos):
            newPosObj.append( self.getlast(pos) )
            posObj.remove( self.getlast(pos) )
            if self.checkIfWin() == 1:
                return 2
            return 1
        else:
            return 0

def inputHandler(out):
    secA = out.split(" ")
    if len(secA) != 2:
        return 0
    return 1

game = tohInstance()
def play():
    print("Current state : ", game.state)
    inp = input("Where would you like to move eg: 1 2 , 3 1\n")
    isValid = inputHandler(inp)
    if (isValid != 1):
        print("Invalid input")
        return play()
    pos1 = int(inp.split(" ")[0])-1
    pos2 = int(inp.split(" ")[1])-1
    outcome = game.move(pos1,pos2)
    if outcome == 0 :
        print("Unable to move to that location")
    elif outcome == 2:
        return print("You have won!")
    play()    
play()