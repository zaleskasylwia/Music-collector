import csv
import datetime
from datetime import date
import random

DATABASE_PATH = "music.csv"


def menu():
    # print menu for music collector
    m = '''Welcome in the CoolMusic! Choose the action:
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
    # Read csv file and convert information to good format
    music = []  # list to use
    with open('music.csv', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            name = (row[0].strip(), row[1].strip())
                    # 1s tuple(artist,album)
            row[2] = (row[2]).strip()
                      # delete int(row[2]) to make a strip()
            information = (
                row[2].strip(),
                row[3].strip(),
                row[4].strip())      # 2nd tuplet (year, genre, length)
            name_and_information = (
                name,
                information)      # make tuplet with 2 tuplets
            music.append(name_and_information)
                         # add all information to 1 list
        return music


# 1
def add_new_album():
    print("You choose 1, now you can add information to music collector \n")
    print("Type artist: ")
    artist = input().lower()
    print("Enter name of the album: ")
    album = input().lower()
    print("Enter a year of release album: ")
    year = input()
    if len(year) == 4:
        if not year.isdigit():
            add_new_album()
        else:
            print("What is the genre: ")
            genre = input()
            length = ask_length()
            # z = artist + ' | ' + album + ' | ' + year + ' | ' + genre + ' | ' +
            # length
            database_file = open(DATABASE_PATH, "a")
            database_file.write(artist + " | " +
                                album + " | " +
                                year + " | " +
                                genre + " | " +
                                length + "\n"
                                )
            database_file.close()
    else:
        print("Year need 4 numbers")
        add_new_album()


def ask_length():
    length = input("Enter length of album in format min:sec, i.e. 31:22 \n")
    if len(length) == 5:
        leght = length.split(":")
        if not (length[0].isdigit() and length[1].isdigit()):
            print("Give me min:sec")
            length = ask_length()
        else:
            len_min = length[0:2]
            len_sec = length[3:5]
            length = (":").join([len_min, len_sec])
            #print(length)
    else:
        leght = ask_length()
    return length

# 2
def find_by_artist():
    #print(artist)
    z = open_music()
    match = False
    for name, information in z:
        if name[0].lower() == artist:
            print("Artist ", name[0], "has albums: ", name[1])
            match = True
    if match is False:
        print("there is no album this artist in database")


# 3
def find_by_year():
    #print(year)
    z = open_music()
    match = False
    for name, information in z:
        if information[0] == year:
            print(
                "In this year",
                information[0],
                "the artist ",
                name[0],
                "write: ",
                name[1])
            match = True
    if match is False:
        print("there is no year this artist in database")


# 4
def find_by_album():
    #print(album_choice)
    z = open_music()
    match = False
    for name, information in z:
        if name[1].lower() == album_choice:
            print("This album: ", name[1], "belongs to", name[0])
            match = True
    if match is False:
        print("there is no album in database")

# 5
def any_phrase(a):
    # Check if given phrase is in any album name and show that album
    z = open_music()
    x = []
    for i in range(0, len(z)):
        if a in z[i][0][1]:
            x.append(z[i])
    if len(x) == 0 or a == "" or a.isspace():
        return "No such entry in any album name"
    else:
        return x


# 6
def find_genre():
    #print(genre)
    z = open_music()
    match = False
    for name, information in z:
        if information[1].lower() == genre:
            print(
                "In the genre ",
                information[1],
                ", artist ",
                name[0],
                ", write: ",
                name[1])
            match = True
    if match is False:
        print("there is no genre in database")

# 7
def ages():
    # Sum age of all albums from csv
    z = open_music()
    now = date.today()      # current date (year month, day)
    now_year = now.year     # current year as int
    age_sume = 0  # zero to add to it
    for name, information in z:
        album_year = int(information[0])
        gap_year = now_year - album_year
        age_sume += gap_year
    return age_sume


# 8 wersja zagniezdzona
def random_genre():
    #print(ran_genre)
    z = open_music()
    match = False
    randomgenre = []
    for album in z:
        if album[1][1].lower() == ran_genre:
            randomgenre.append(album)
            match = True
            # print(len(randomgenre))
    if match is False:
        print("There is no genre like this")
    else:
        print(randomgenre[random.randint(0, len(randomgenre) - 1)])


# 9
def count_artist():
    # print(artist_count)
    z = open_music()
    match = False
    counter = 0
    for name, information in z:
        if name[0].lower() == artist_count:
            counter += 1
            match = True
    if match is False:
        print("there is no album this artist in database")
    print("This artist", artist_count, "has recorded: ", counter, "albums")


# 10 wersja zagniezdzona
def longest_time():
    match = False
    z = open_music()
    longest_length = []
    for length in z:
        length = length[1][2]
        longest_length.append(length)
    #print("The longest album takes:", max(longest_length))
    max_length = max(longest_length)
    for album in z:
        if album[1][2].lower() == max_length:
            print(
                "the longest album takes:",
                album[1][2],
                ", artist ",
                album[0][0],
                ", write: ",
                album [0][1])
            match = True
    if match is False:
        print("Nope")




# BODY
while True:
    print(menu())
    user_choice = input()
    if user_choice == "1":
        add_new_album()
    elif user_choice == "2":         # Find albums by artist
        artist = (input("Give me name of the artist ")).lower()
        find_by_artist()
    elif user_choice == "3":        # Find albums by year
        year = (input("Tell me a year to find album "))
        find_by_year()
    elif user_choice == "4":         # Find musician by album
        album_choice = (input("Enter a name of the album ")).lower()
        find_by_album()
    elif user_choice == "5":       # Find by pharse
        phrase = (input("Type me a pharse which are you looking for ")).lower()
        print(any_phrase(phrase), '\n')
    elif user_choice == "6":       # Find album by genre
        genre = (input("Tell me a genre which you are lookig for "))
        print(find_genre(), '\n')
    elif user_choice == "7":       # Sume of all albums age
        print( "All ages in music collector: ", ages(), '\n')
    elif user_choice == "8":        #Find by genre
        ran_genre = (input("Tell me a genre "))
        random_genre()
    elif user_choice == "9":        #how many albums have one artist
        artist_count = (input("Type artist "))
        count_artist()
    elif user_choice == "10":       #the longest time album
        # input(longest_time)
        longest_time()
    elif user_choice == "0":       # Exit
        exit()  # return
    else:
        print ("Menu doesn't have this option")

    ask = ""
    while not (ask == 'YES' or ask == 'NO'):  # ask about game again
        ask = input(
            "Do you want to use Music Collector again? (YES/NO) ").upper(
        )
    if ask == 'NO':
        break
