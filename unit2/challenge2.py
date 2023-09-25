# Define the Player class
class Player:
    def play(self):
        print("The player is playing cricket")

# Define the Batsman class, derived from Player
class Batsman(Player):
    def play(self):
        print("The batsman is batting")

# Define the Bowler class, derived from Player
class Bowler(Player):
    def play(self):
        print("The bowler is bowling")

# Create objects of Batsman and Bowler classes and call the play() method
batsman = Batsman()
bowler = Bowler()

batsman.play()  # Output: "The batsman is batting"
bowler.play()   # Output: "The bowler is bowling"
