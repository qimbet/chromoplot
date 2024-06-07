#a pseduo-post generator:
#When this function is called, it generates a random string of text which may or may not include a player's name -- given as either Full name, first name, or last name, with possibility of tpyos

import random


playerNames = ["Wayne Gretzky", "Lebron James", "Roger Federer", "Louis Vuitton", "Yannick Borel", "Usain Bolt", "Michael Phelps", "Flipsy McFlippy"] #8 entries

def randomPlayer():
    num = random.randint(0,len(playerNames)-1)
    playerChoice = playerNames[num]

    firstLastOrFullName = random.randint(0,2)
    if (firstLastOrFullName == 1): #arbitrary
        return playerChoice.split()[0]
    elif (firstLastOrFullName == 2): #Calling a player by their last name? How edgy :O
        return playerChoice.split()[1]
    else:
        return playerChoice

def draftPost (player, player2): 
    randomPost = random.randint(1, 5)
    if (randomPost == 1):
        post = f"{player}'s team is doing great this season!"
    elif (randomPost == 2):
        post = f"Wow, I sure do love sports as a general concept."
    elif (randomPost == 3):
        post = f"{player} is nowhere near as talented as {player2}"
    elif (randomPost == 4):
        post = f"Gosh I sure hope I don't misspell {player[:3] + player[4:]}'s name!"
    elif (randomPost == 5):
        post = f"Adding a letter? To {player + 'b'}'s name? I would never!"
    return post
    
def generatePost():
    return draftPost(randomPlayer(), randomPlayer())
    

if __name__ == "__main__":
    for x in range(1, 20):
        print(generatePost())