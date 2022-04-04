import random 
import os
import time
import sqlite3
import csv


clear = lambda: os.system("clear")



def wolfCreateTable(): #clear and create table
    connection = sqlite3.connect('/media/oem/Python Linux/WolfGame/Wolf_SQL.db') #file name

    c = connection.cursor()
    
    c.execute('DROP TABLE IF EXISTS wolfchar')

    characterSQL = """
        CREATE TABLE IF NOT EXISTS wolfchar(
            charid INTEGER,
            character VARCHAR(35) NOT NULL,
            shirt VARCHAR(35),
            pants VARCHAR(30),
            location VARCHAR(30),
            location2 VARCHAR(30),
            location3 VARCHAR(30),
            location4 VARCHAR(30),
            greet1 VARCHAR(30),
            greet2 VARCHAR(30),
            spieces VARCHAR(20)      
        )
        """

    c.execute(characterSQL)
    connection.commit()
    connection.close()
    



def addChartoDB(charid,character,shirtt,pants,location,location2,location3,location4,greett1,greet2,spieces):
    
    global shirt, ranShirt, ranPants, greet1 
    global ranGreet1, ranGreet2, characters, ranChar, ranlocate, ranlocate2

    connection = sqlite3.connect('/media/oem/Python Linux/WolfGame/Wolf_SQL.db') #file name

    c = connection.cursor()

    
    c.execute(f'''
        INSERT INTO wolfchar VALUES('{charid}','{character}','{shirtt}','{pants}','{location}','{location2}','{location3}','{location4}','{greett1}','{greet2}','{spieces}') 
        ''')
    
    connection.commit()
    connection.close()


    

def createChar():  #Add to the database
    global spieces, shirt, ranShirt, ranPants, greet1,gameplaylocations
    global ranGreet1, ranGreet2, characters, ranChar, ranlocate, ranlocate2

    w = ['wolf','human','hunter']

    outfit = {
        "a black suit":'a black tie', 
        'some white pants':'a white shirt', 
        'a sweat shirt':'some sweat pants', 
        'a pair of sunglasses':'a swimsuit and sunscreen', 
        'a basketball jersey':'some basketball shoes',
        'some winter gloves': 'a winter jacket'
        
    }
    shirt = list(outfit.keys())
    
    
    greeting = {
        'Hey there, How can I help you':'Not that its your buissness, but I all I remember was ',
        'Sup, What do you want?':'I only remeber ',
        'Uhhhh...Hello?':'Whos asking? Anyway I can only tell you about ', 
        'Howdy, What do you need to know':'Well you see, I can only tell you about ', 
        'Hey kid, Be quick, I dont have much time.':'A little intrusive huh? Errr...  ', 
        'Oh Hello, How are you?':'Hmm let me think. I will tell you about '
    }
    greet1 = list(greeting.keys())
    

    characters = ['Mike','Hawk','Anitia','Dick','Curly','Tim','Max','Paul','Mary','Jane','Dill','Phil']

    ranChar = list(random.sample(characters,6)) #choose random character

    
        
        
        
    char6 = 1
    # while char6 <= 6:
    id = 1
    
    gameplaylocations = []

    
    while char6 <= 6:

        with open('/media/oem/Python Linux/WolfGame/WolfLocation.csv', 'r') as loc:
            #open and read csv file
            
            read = csv.reader(loc)
            next(read)  #skips headers
                    
            ranlocate = random.sample(list(read), 6) #creates 6 random lists of locations
            
            ranlocate2 = random.choice(ranlocate) #one random list
 
            ranShirt = random.choice(shirt) ##Choose random shirt
            ranPants = outfit[ranShirt] #choose random pants based on shirt above
            ranGreet1 = random.choice(greet1)  #chooses greeting        
            ranGreet2 = greeting[ranGreet1]  #choose random greeting
            spieces = random.choice(w)  ### What spieces will they be


            addChartoDB(id,ranChar[0], ranShirt, ranPants, ranlocate2[0],ranlocate2[1],ranlocate2[2],ranlocate2[3],ranGreet1, ranGreet2, spieces)

        #     ###Remove items from list
            id += 1
            char6 += 1
            
            gameplaylocations.append(ranlocate2[0])

            shirt.remove(ranShirt)

            greet1.remove(ranGreet1)

            ranChar.remove(ranChar[0])

            ranlocate.remove(ranlocate2)

       
        



def theWOLF():  ##### this is your wolf/killer
    global wID, rowW
    
    connection = sqlite3.connect('/media/oem/Python Linux/WolfGame/Wolf_SQL.db') #file name

    c = connection.cursor()

    #####Choosing a wolf attachker
    idss = [1,2,3,4,5,6] #fill ID in database
    wID = random.choice(idss)  ##### this is your wolf/killer

    wolf = 'select character,shirt,pants,location,location2,location3,location4 from wolfchar where charid = ?;'  #The ID of killer
    c.execute(wolf, (wID,))

    #######################################
    for rowW in c.fetchall():
        ... # prints (tuple) of wolf
    
    ##########################################
    
    # for wPerson in row:
    #     print(wPerson)

    #####Change spieces to wolf
    change = 'update wolfchar set spieces="wolf" where charid = ?' #ensures person is a wolf
    c.execute(change,(wID,))
    connection.commit()
    connection.close()
    #print(rowW)
        


def guessWolf():
    global gameplaylocations
    
    connection = sqlite3.connect('/media/oem/Python Linux/WolfGame/Wolf_SQL.db') #file name

    c = connection.cursor()
    
    
    #####List of people interrogated####
    for peep in peopleN:
        print(peep)
    
    #user guessing wolf    
    guesswho = input('\nType the number of the wolf you think bit you, then type enter to continue: ')
    who = f'select character from wolfchar where charid = ? ' #database gathering info
    c.execute(who, (guesswho,))
    for g in c.fetchall():
        ...
    for gw in g:
        ... #gw is character guessed 

    clear()
    #####list of locations
    fd = 1
    for find in gameplaylocations:
        print(str(fd) + ") " + find)
        fd += 1
    
    #user guess location
    guessLocation = input('\nType the number of the location you think you were when you were bitten, then type enter to continue: ')
    where = f'select location from wolfchar where charid = ? ' #database gathering info
    c.execute(where, (guessLocation,))
    for gL in c.fetchall():
        ...
    for ug in gL:
        ... #ug is location guessed 
   
    clear()
    ###############  Results
    if gw == rowW[0] and ug == rowW[3]:
        clear()
        input(f'CONGRATLATIONS! You found them!\nTHE wolf that bit you was {rowW[0]}\nTheyre wearing {rowW[1]} and {rowW[2]}\nAnd they did it at{rowW[3]}\nClick enter to continue')
    
    elif gw == rowW[0] and ug != rowW[3]:
        input(f'You found the killer --{rowW[0]}-- but {ug} is NOT the location\nClick enter to continue') 
        gameplay()  
    
    elif gw != rowW[0] and ug == rowW[3]:
        input(f'You got the location --{rowW[3]}--but {gw} is NOT the wolf that bit you\nClick enter to continue')
        gameplay()
        
    else:
        print("You did not guess the wolf or location correctly\nTry again")
        gameplay()
            

    
        



def interview(up):
    global peopleN, rowW
    #################
    connection = sqlite3.connect('/media/oem/Python Linux/WolfGame/Wolf_SQL.db') #file name

    c = connection.cursor()
    
  
    loc234 = ['location2','location3','location4']
    loc234Choice = random.choice(loc234)
    ###################
    while True:
        clear()
        questions = ['1: Where were you last night?', '2: Who are you?', '3: What where you wearing last night?']
        for x in questions:
            print(x)


        up2 = input('\nType the number of the question you want to ask this person\nType "D" when done asking\n: ')    
    ###################
        
        if up == "1":
            
            char1 = []
            chID = 1
            where = f'select character,{loc234Choice},pants from wolfchar where charid = ? '
            c.execute(where, (chID,))
            
            for wh in c.fetchall():
                ...
            for whr in wh:
                char1.append(whr)  #adds character, location2,3or4, and pants to list char1
            
            ################################ QESTIONS
            if up2 == '1': #location
                
                input(f'\nMy location had {char1[1]}\nClick Enter to continue')
                clear()
                
            elif up2 == '2': #name
                
                input(f'\nMy name is {char1[0]}\nClick Enter to continue')
                peopleN[0] = "1) " + char1[0]
                clear()

            elif up2 == '3': #outfit
        
                input(f'\nI had on {char1[2]}\nClick Enter to continue')
                clear()

            elif up2 == 'D' or up2 == 'd':
                clear()
                break
            
                
    ########################        
        elif up == "2":
            char1 = []
            chID = 2
            where = f'select character,{loc234Choice},pants from wolfchar where charid = ? '
            c.execute(where, (chID,))
            
            for wh in c.fetchall():
                ...
            for whr in wh:
                char1.append(whr)
            
            ################################
            if up2 == '1': #location
                
                input(f'\nMy location had {char1[1]}\nClick Enter to continue')
                clear()
                
            elif up2 == '2': #name
                
                input(f'\nMy name is {char1[0]}\nClick Enter to continue')
                peopleN[1] = "2) " + char1[0]
                clear()

            elif up2 == '3': #outfit
        
                input(f'\nI had on {char1[2]}\nClick Enter to continue')
                clear()

            elif up2 == 'D' or up2 == 'd':
                clear()
                break
            
    ######################        
        elif up == "3":
            char1 = []
            chID = 3
            where = f'select character,{loc234Choice},pants from wolfchar where charid = ? '
            c.execute(where, (chID,))
            
            for wh in c.fetchall():
                ...
            for whr in wh:
                char1.append(whr)
            
            ################################
            if up2 == '1': #location
                
                input(f'\nMy location had {char1[1]}\nClick Enter to continue')
                clear()
                
            elif up2 == '2': #name
                
                input(f'\nMy name is {char1[0]}\nClick Enter to continue')
                peopleN[2] = "3) " + char1[0]
                clear()

            elif up2 == '3': #outfit
        
                input(f'\nI had on {char1[2]}\nClick Enter to continue')
                clear()

            elif up2 == 'D' or up2 == 'd':
                clear()
                break
            
    ########################        
        elif up == "4":
            char1 = []
            chID = 4
            where = f'select character,{loc234Choice},pants from wolfchar where charid = ? '
            c.execute(where, (chID,))
            
            for wh in c.fetchall():
                ...
            for whr in wh:
                char1.append(whr)
            
            ################################
            if up2 == '1': #location
                
                input(f'\nMy location had {char1[1]}\nClick Enter to continue')
                clear()
                
            elif up2 == '2': #name
                
                input(f'\nMy name is {char1[0]}\nClick Enter to continue')
                peopleN[3] = "4) " + char1[0]
                clear()

            elif up2 == '3': #outfit
        
                input(f'\nI had on {char1[2]}\nClick Enter to continue')
                clear()

            elif up2 == 'D' or up2 == 'd':
                clear()
                break
            
    #######################
        elif up == "5":
            char1 = []
            chID = 5
            where = f'select character,{loc234Choice},pants from wolfchar where charid = ? '
            c.execute(where, (chID,))
            
            for wh in c.fetchall():
                ...
            for whr in wh:
                char1.append(whr)
            
            ################################
            if up2 == '1': #location
                
                input(f'\nMy location had {char1[1]}\nClick Enter to continue')
                clear()
                
            elif up2 == '2': #name
                
                input(f'\nMy name is {char1[0]}\nClick Enter to continue')
                peopleN[4] = "5) " + char1[0]
                clear()

            elif up2 == '3': #outfit
        
                input(f'\nI had on {char1[2]}\nClick Enter to continue')
                clear()

            elif up2 == 'D' or up2 == 'd':
                clear()
                break
            
    ############
        elif up == "6":
            char1 = []
            chID = 6
            where = f'select character,{loc234Choice},pants from wolfchar where charid = ? '
            c.execute(where, (chID,))
            
            for wh in c.fetchall():
                ...
            for whr in wh:
                char1.append(whr)
            
            ################################
            if up2 == '1': #location
                
                input(f'\nMy location had {char1[1]}\nClick Enter to continue')
                clear()
                
            elif up2 == '2': #name
                
                input(f'\nMy name is {char1[0]}\nClick Enter to continue')
                peopleN[5] = "6) " + char1[0]
                clear()

            elif up2 == '3': #outfit
        
                input(f'\nI had on {char1[2]}\nClick Enter to continue')
                clear()

            elif up2 == 'D' or up2 == 'd':
                clear()
                break


###############################
#################################
#################################

def gameplay():
    global peopleN, rowW
    
    wolfCreateTable()
    createChar()
    theWOLF()
    
    #print(f'The wolf that bit you was {rowW[0]}\nTheyre wearing {rowW[1]} and {rowW[2]}\nAnd they did it at{rowW[3]}')

    connection = sqlite3.connect('/media/oem/Python Linux/WolfGame/Wolf_SQL.db') #file name

    c = connection.cursor()

    peopleN = ['1) ?','2) ?','3) ?','4) ?','5) ?','6) ?'] #a list that will be filled each time you interrogate someone

    ####################
    peopleList = []
    theID = [1,2,3,4,5,6]
    
    for y in theID:
        intID = y
        interro = 'select character from wolfchar where charid = ?;'  #The ID of killer in the database
        c.execute(interro, (intID,))
        for getting in c.fetchall():
            ...
        for z in getting:
            peopleList.append(z) # list of people around you to interrogate
    ########################    
    interroPoints = 0

    while True:
        clear()
        
        print("\n\nINTERRO POINTS::  " + str(interroPoints))
        

        print('\nInterrogate the people below to unlock memories.\nYour memories will be clues to who bit you\n')

        for p in peopleN:  #keeps track of people interrogated
            print(p)

        ######### MEMORIES ######
        if interroPoints <= 2:
            print("\nInterrogate More people to unlock memories(you have 2 memories to unlock)")
            ##The user can interrogate each person more than once, but the 'ask' list is not give them memory points each time a person is interrogated, only the first time
            
        elif interroPoints >=3 and interroPoints <= 6:
            k = random.randrange(1,3)
            print(f'\nMEMORY 1 **UNLOCKED**\nThe person was wearing {rowW[k]}')
            
                
            if interroPoints >=3 and interroPoints >= 6:
                l = random.randrange(4,6)
                print(f'\nMEMORY 2 **UNLOCKED**\nThe persons location had {rowW[l]}')

        ##############################
        userIn = input("\nTo choose a person to interrogate, type a number 1-6\nWhen ready to guess, type 'G'\nNote that you can only guess when all people have been interrogated\n:  ")

        ask = [1,2,3,4,5,6]
        
        if userIn == "1":
            clear() 
            ##below is to prevent the user from getting interropoints too fast by interrogating the same person more than once
            ##The user can interrogate each person more than once, but this is not give them memory points each time a person is interrogated, only the first time
           
            if peopleN[0] == '1) ?':
                interroPoints += 1

            interview('1')
         
             
        elif userIn == "2":
            clear()
            
            if peopleN[1] == '2) ?':
                interroPoints += 1

            interview('2')

        elif userIn == "3":
            clear() 
            
            if peopleN[2] == '3) ?':
                interroPoints += 1

            interview('3')

        elif userIn == "4":
            clear() 
            
            if peopleN[3] == '4) ?':
                interroPoints += 1
                
            interview('4')

        elif userIn == "5":
            clear() 
            
            if peopleN[4] == '5) ?':
                interroPoints += 1
                
            interview('5')

        elif userIn == "6":
            clear() 
            
            if peopleN[5] == '6) ?':
                interroPoints += 1

            interview('6')
            
        elif userIn == 'G' or userIn == 'g':
            if interroPoints < 6:
                clear()
                input('You have not interrogated everyone yet!\nGo back and interrogate everyone!\nClick enter to continue')
                             
            else:
                clear()
                guessWolf()
                clear()
                playagain = input('Would you like to play again?(Y/N): ')
                pa = playagain.upper()
                if pa == 'Y':
                    clear()
                    gameplay()
                else:
                    print('Game Ending...')
                    break
            
        else:
            clear()
            



  
gameplay()

# wolfCreateTable()

# createChar()

# theWOLF()



 
    
    
    
    


