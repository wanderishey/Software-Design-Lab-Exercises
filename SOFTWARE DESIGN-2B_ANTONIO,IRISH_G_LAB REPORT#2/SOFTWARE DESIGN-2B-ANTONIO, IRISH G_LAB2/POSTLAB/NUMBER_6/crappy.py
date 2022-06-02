from runordie import Die

class Player(object):

    def __init__(self):
        """Has a pair of dice and an empty rolls list."""
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []
        self.rollscount=0
        self.atStartup=True
        self.winner=False
        self.looser=False

    def __str__(self):
        """Returns a string representation of the list of rolls."""
        result = ""
        for (v1, v2) in self.rolls:
            result = result + str((v1, v2)) + " " +\
                str(v1 + v2) + "\n"
        return result

    def getNumberOfRolls(self):
        """Returns the number of the rolls."""
        return len(self.rolls)

    def rollDice(self):
        #roll the dice q
        self.die1.roll()
        diefirst=self.die1.getValue()
        self.die2.roll()
        #roll the dice2
        diesecond=self.die2.getValue()
        res=(diefirst,diesecond)
        #update the roll count
        self.rollscount+=1
        """same logic as play but just updating
        islooser and is win variable"""
        self.rolls = []
        v1=diefirst
        v2=diesecond
        #append dies to the rolls
        self.rolls.append((v1, v2))
        #sum thereslu of the two dies
        initialSum = v1 + v2
        #check if sum is looser
        if initialSum in (2, 3, 12):
            self.looser=True
        elif initialSum in (7, 11):
            #check if sum is not looser
            #then set winner to true
            self.winner=True
        else:#if sum is not in the both then
        #roll again the two dies
            while (True):
                self.die1.roll()
                self.die2.roll()
                (v1, v2) = (self.die1.getValue(),
                self.die2.getValue())
                self.rolls.append((v1, v2))
                #find sum of the two dies
                laterSum = v1 + v2
                #check if sum is 7
                #then set looser to true
                if laterSum == 7:
                    self.looser= True
                    self.winner= False
                    break
                elif laterSum == initialSum:
                    #check if sum is initialSum
                    #then set winner to true
                    self.winner= True
                    self.looser=False
                    break
                """else continue loop unitl eithercondition is satisfied"""
        return res

    def isWinner(self):
        #checking the varible if true the return true
        if self.winner is True:
            return True

    def isLooser(self):
        #checking the varible if true the return true
        if self.looser is True:
            return True

def __str__(self):
    """Returns a string representation of
    the list of rolls."""
    result = ""
    for (v1, v2) in self.rolls:
        result = result + str((v1, v2)) + " " +\
        str(v1 + v2) + "\n"
    return result

def playOneGame():
    """Plays a single game and prints the results."""
    player = Player()
    yourDice = player.rollDice()
    print("yourDice result is: ",yourDice)
    youWin = player.isWinner()
    youLoose=player.isLooser()
    if youWin:
        print("You win!")
    if youLoose:
        print("You lose!")

def playManyGames(number):
    """Plays a number of games and prints statistics."""
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    
    player = Player()
    for count in range(number):
        dicenum = player.rollDice()
        print("your dice num is: ",dicenum)
        hasWon = player.isWinner()
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
    print("The total number of wins is", wins)
    print("The total number of losses is", losses)
    print("The average number of rolls per win is %0.2f" % \
    (winRolls / wins))
    print("The average number of rolls per loss is %0.2f" % \
    (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins*100 / number)+"%")

def main():
    """Plays a number of games and prints statistics."""
    number = int(input("Enter the number of games: "))
    playManyGames(number)

if __name__ == "__main__":
    main()

