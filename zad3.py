import csv
import datetime
from datetime import date
from time import strftime
DATABASE_PATH = "music.csv"



def menu():
    #print menu for music collector
    m ='''Welcome in the CoolMusic! Choose the action:
        1) Add new album
        2) Find albums by artist
        3) Find albums by year
        4) Find musician by album
        5) Find albums by letter(s)
        6) Find albums by genre
        7) Calculate the age of all albums
        8) Choose a random album by genre
        9) Show the amount of albums by an artist *
        10) Find the longest-time album *
        0) Exit
        '''
    return m


def open_music():
    #Read csv file and convert information to good format
    music = []      #list to use
    with open('music.csv', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            name = (row[0], row[1])     # 1s tuple(artist,album)
            row[2] = int(row[2])        # change year to int
            information = (row[2], row[3], row[4])      # 2nd tuplet (year, genre, lenght)
            name_and_information = (name, information)      # make tuplet with 2 tuplets
            music.append(name_and_information)      # add all information to 1 list
        return music


#1 dziala
def add_new_album():
    print("You choose 1, now you can add information to music collector \n")
    print("Type artist: ")
    artist = input().capitalize()
    print("Enter name of the album: ")
    album = input().capitalize()
    print("Enter a year of release album: ")
    year = input()
    if not year.isdigit():
        add_new_album()
    else: 
        print("What is the genre: ")
        genre = input()
        print("Enter lenght of album in format min:sec, i.e. 31:22")
        lenght = input()
        #z = artist + ' | ' + album + ' | ' + year + ' | ' + genre + ' | ' + lenght
        database_file = open(DATABASE_PATH, "a")
        database_file.write(artist + " | " +
                            album + " | " +
                            year + " | " +
                            genre + " | " +
                            lenght + "\n"
                            )
        database_file.close()

#7
def ages():
    #Sum age of all albums from csv
    z = open_music()
    now = date.today()      # current date (year month, day)
    now_year = now.year     # current year as int
    age_sume = 0            #zero to add to it
    for i in range(0, len(z)):
        age_sume += (now_year - z[i][1][0])
    return age_sume




def album_artist(b):
    """Made dictionary with proper key depend from argument"""
    z = open_music()
    x = 0
    my_music = {}       # establish dictionary to later use
    for i in range(len(z)):     # made proper key and entry for it
        if b == "2":        # Find albums by artist
            key = z[i][0][0]
            x = z[i][0][1], z[i][1]
        elif b == "3":      # Find albums by year #working
            key = z[i][1][0]
            x = z[i][0], z[i][1][1], z[i][1][1]
        elif b == "4":      # Find musician by album
            key = z[i][0][1]
            x = z[i][0][0], z[i][1]
        elif b == "6":      # Find album by genre
            key = z[i][1][1]
            x = z[i][0], z[i][1][0], z[i][1][2]
        my_music.setdefault(key, []).append(x)      # if entry add key and information for it,
    return my_music                                 # if key already present add next entry to this key

#2, 3, 4, 6
def search(a, b):
    #Depend from input show resault of search message
    u = album_artist(b) #go to another function
    if b == "2":        # Find albums by artist
        c = "No such artst in databse"
    elif b == "3":      # Find albums by year
        c = "No albums from that year in database"
    elif b == "4":      # Find musician by album
        c = "No such album in data base"
    elif b == "6":      # Find album by genre
        c = "No such genre in data base"
    return u.get(a, [c])


#5 dzia
def any_phrase(a):
    #Check if given phrase is in any album name and show that album
    z = open_music()
    x = []
    for i in range(0, len(z)):
        if a in z[i][0][1]:
            x.append(z[i])
    if len(x) == 0 or a == "" or a.isspace():
        return "No such entry in any album name"
    else:
        return x



def print_album(albums):
   #print all given albums date
   print('Artist: ', album[0][0])
   print('Album name: ', album[0][1])
   print('Year of release: ', album[1][0])
   print('Genre: ', album[1][1])
   print('Length: ', album[1][2])





while True:     # body 
    print(menu())
    user_choice = input()
    if user_choice == "1":
        add_new_album()
    elif user_choice == "2":         # Find albums by artist
        artist = (input("Give me name of the artist ")).upper()
        print(search(artist, user_choice))
    elif user_choice == "3":        # Find albums by year
        year = int(input("Tell me a year to find album "))
        print(search(year, user_choice), '\n')
    elif user_choice == "4":         # Find musician by album
        album_choice = (input("Enter a name of the album ")).upper()
        print(search(album_choice, user_choice), '\n')
    elif user_choice == "5":       # Find by pharse
        phrase = (input("Type me a pharse which are you looking for "))
        print(any_phrase(phrase), '\n')
    elif user_choice == "6":       # Find album by genre
        genre = (input("Tell me a genre wich you are lookig for "))
        print(search(genre, user_choice), '\n')
    elif user_choice == "7":       # Sume of all albums age
        print(ages(), '\n')
    elif user_choice == "0":       # Exit
        exit() #return
    else:
        print ("Menu doesn't have this option")


    ask = ""
    while not (ask == 'YES' or ask == 'NO'):  # ask about game again
        ask = input("Do you want to use Music Collector again? (YES/NO) ").upper()
    if ask == 'NO':
        break
