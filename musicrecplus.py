# A very simple hobby recommender system.
from cs115 import map

PREF_FILE = "hobbyrecplus.txt"
userDict = {}

def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'.
        Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    file = open(fileName, 'r')
    for line in file:
        # Read and parse a single line
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict
         
def getPreferences(userName, userMap):
    ''' Returns a list of the user's preferred artists.

        If the system already knows about the user,
        it gets the preferences out of the userMap
        dictionary and then asks the user if she has
        additional preferences.  If the user is new,
        it simply asks the user for her preferences. '''
    
    newPref = ""
    if userName in userMap:
        prefs = userMap[userName]
        print("I see that you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("Please enter another artist or band that you")
        print("like, or just press enter to return to the main menu.")
        newPref = input("")
    else:
        prefs = []
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        newPref = input("that you like: " )
        
    while newPref != "":
        prefs.append(newPref.strip().title())
        print("Please enter another artist or band that you")
        print("like, or just press enter to return to the main menu.")
        newPref = input("")
        
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs

def returnPreferences(userName, userMap):
    ''' Returns a list of the user's preferred artists only.'''
    
    newPref = ""
    if userName in userMap:
        print("Your music preferences include:")
        prefs = userMap[userName]
        for artist in prefs:
            print(artist)
        
    while newPref != "":
        prefs.append(newPref.strip().title())
        print("Please enter another artist or band that you")
        print("like, or just press enter to return to the main menu.")
        newPref = input("")
        
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs

def deletePreferences(userName, userMap):
    ''' Returns a list of the user's preferred artists with deletions taken out.

        It gets the preferences out of the userMap
        dictionary and then asks the user if she 
        wants to delete preferences.
        It checks for invalid input and asks for a new input '''
    
    delPref = ""
    if userName in userMap:
        prefs = userMap[userName]
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("Please enter an artist or band that you")
        print("want to delete press enter to return to the main menu.")
        delPref = input("").title()
        
    while delPref != "":
        if delPref in prefs:
            prefs.remove(delPref.strip().title())
            print("Please enter another artist or band that you")
            print("want to delete or just press enter to return to the main menu.")
            delPref = input("").title()
            print("Your music preferences now include:")
            for artist in prefs:
                print(artist)
        else:
            print('Invalid input, please try again:')
            delPref = input("").title()
        
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs

def getRecommendations(currUser, prefs, userMap):
    ''' Gets recommendations for a user (currUser) based
        on the users in userMap (a dictionary)
        and the user's preferences in pref (a list).
        Returns a list of recommended artists.  '''
    if len(userMap) == 1:
        print ("I am sorry, there is no one else in the database")
        print ("to compare to so I cannot recommend you anything ")
        menuLoop(currUser,userMap)
    else:
        bestUser = findBestUser(currUser, prefs, userMap)
        recommendations = drop(prefs, userMap[bestUser])
    return recommendations

def printRecs(recs,userName):
    '''Print the user's recommendations'''
    if len(recs) == 0:
        print("I'm sorry but I have no recommendations")
        print("for you right now.")
    else:
        print(userName+"," + " based on the users I currently")
        print("know about, I believe you might like:")
        for artist in recs:
            print(artist)
        print("I hope you enjoy them! I will save your")
        print("preferred artists and have new")
        print(" recommendations for you in the future") 

def findBestUser(currUser, prefs, userMap):
    ''' Find the user whose tastes are closest to the current
        user.  Return the best user's name (a string) '''
    users = userMap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = numMatches(prefs, userMap[user])
        if score > bestScore and currUser != user:
            bestScore = score
            bestUser = user
    return bestUser

def drop(list1, list2):
    ''' Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    
    return list3

def numMatches( list1, list2 ):
    ''' return the number of elements that match between
        two sorted lists '''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def saveUserPreferences(userName, prefs, userMap, fileName):
    ''' Writes all of the user preferences to the file.
        Returns nothing. '''
    userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + \
                    "\n"
        file.write(toSave)
    file.close()    

def mostValue(L):
    '''helper functions for howPopular()'''
    r = {}
    for i in L:
        if not i in r:
            r[i] = 1
        else:
            r[i] += 1
    artist = []
    frequencies = []
    for i in r:
        artist += [i]
        frequencies += [r[i]]
    return artist[frequencies.index(max(frequencies))]

def howPopular():
    '''determines how popular each artist is'''
    c = 0
    L = []
    for i in userDict:
        L += userDict[i]
    for i in L:
        if i == mostValue(L): 
            c += 1
    return c

def mostPopularArtists(userMap):
    '''Returns the most popular artist or artists'''
    users = userMap.keys()
    Freqs = {}
    maxlikes = 0
    mostpop = []
    for user in users:
        for artist in userMap[user]:
            if artist not in Freqs:
                Freqs[artist] = 1
            else:
                popularity_count = Freqs[artist]
                popularity_count += 1
                Freqs[artist] = popularity_count
    for artist in Freqs:
        if Freqs[artist] > maxlikes:
            maxlikes = Freqs[artist]
    
    for artist in Freqs:
        if Freqs[artist] == maxlikes:
            mostpop += [artist]
    return mostpop    
    
def printMostPopularArtists(userMap):
    '''Prints the most popular artist or artists.'''
    mostpop = mostPopularArtists(userMap)
    if len(mostpop) == 1: 
        print (mostpop[0] + " is the most popular artist in the database!")
    else:
        print (mostpop[0] + ' and ' + mostpop[1] + " are the most popular artists in the database!")


def mostLikes():
    '''finds the user(s) with the most likes'''
    L = []
    for i in userDict:
        L += [userDict[i]]
    L = map(len, L)
    
    for i in userDict:
        if max(L) == len(userDict[i]):
            if i[-1] == '$':
                print('Unfortunately, the user has opted out to share their likes')
            else:
                print(str(i) + " likes " + str(len(userDict[i])) + " songs: " + str(userDict[i]))

def main():
    ''' The main recommendation function '''
    userMap = loadUsers(PREF_FILE)
    print("Welcome to the music recommender system!")
    userName = input("Note: if you wish for your name and preferences to be hidden from other users, add a $ to the end of your name.\nPlease enter your name: ")
    print ("\nWelcome, " + userName)
    if userName in userMap:
        menuLoop(userName,userMap)
    else:
        prefs = getPreferences(userName,userMap)
        saveUserPreferences(userName, prefs, userMap, PREF_FILE)
        menuLoop(userName,userMap)
    
def menuLoop(userName,userMap):
    '''Continuously prints the menu until the user decides to quit.'''
    while True:
        print ("\nEnter a letter to choose an option:")
        print ("e - enter preferences")
        print ("s - show preferences")
        print ("r - get recommendations")
        print ("p - show most popular artists")
        print ("h - how popular is the most popular")
        print ("m - which user has the most likes")
        print ("d - delete certain preferences")
        print ("q - save and quit\n")
        userSelect = input()
        
        if userSelect == "e":
            prefs = getPreferences(userName,userMap)
            saveUserPreferences(userName, prefs, userMap, PREF_FILE)

        elif userSelect == "s":
            prefs = returnPreferences(userName,userMap)
                    
        elif userSelect == "r":
            prefs = returnPreferences(userName,userMap)
            recs = getRecommendations(userName, prefs, userMap)
            print('')
            printRecs(recs,userName)
            saveUserPreferences(userName, prefs, userMap, PREF_FILE)
            
        elif userSelect == "p":
            printMostPopularArtists(userMap)
            print("Amount of likes: %d" % howPopular())
            
        elif userSelect == "h":
            print("Our most current most popular artist has %d likes" % howPopular())
            
        elif userSelect == "m":
            print("User(s) with the most likes:")
            mostLikes()
        
        elif userSelect == "d":
            new_prefs = deletePreferences(userName,userMap)
            saveUserPreferences(userName, new_prefs, userMap, PREF_FILE)
            
        elif userSelect == "q":
            try:
                saveUserPreferences(userName, prefs, userMap, PREF_FILE)
                break
            except:
                break
        else:
            print ("Invalid option, try again")
            menuLoop(userName,userMap)

if __name__ == "__main__": main()

