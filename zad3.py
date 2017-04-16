import csv
#music = []


#przeklejone
with open('music.csv') as csvfile:
    to_split = csvfile.readlines()
    splitted = [line.split(" | ") for line in to_split]
    music = [((line[0].replace('\ufeff', ''), line[1]), (int(line[2]), line[3], line[4].replace('\n', ''))) 
    for line in splitted]


#1
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
        z = artist + ' | ' + album + ' | ' + year + ' | ' + genre + ' | ' + lenght
        with open('music.csv', "a") as adding:
            adding.write(z + "\n")
        music.append(((artist, album), (int(year), genre, lenght)))



#2
def find_albums_by_artist():
    artist = str(input("Name of the artist: "))
    if artist in music:
        print("albums")
        #return?
    else:
        print("Music collector don't have this albums")
        #continue?

'''#3
def find_albums_by_year():

#4
def find_musician_by_album():

#5
def find_albums_by_letter():

#6
def find_albums_by_genre():

#7
def calculate_the_age_of_all_albums():

#8
def choose_a_random_album_by_genre():

#9
def show_the_amount_of_albums_by_an_artist():

#10
def find_the_longest_time_album():'''




def main():
    while True:
        print(
            '''Welcome in the CoolMusic! Choose the action:
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
                ''')

        input_read = input()
        if input_read.isdigit():
            input_read = int(input_read)
        else:
            print("Chose number from 0 to 10")

        if input_read == 1:
            add_new_album()
        elif input_read == 2:
            find_albums_by_artist()
        elif input_read == 3:
            find_albums_by_year()
        elif input_read == 4:
            find_musician_by_album()
        elif input_read == 5:
            find_albums_by_letter()
        elif input_read == 6:
            find_albums_by_genre()
        elif input_read == 7:
            calculate_the_age_of_all_albums()
        elif input_read == 8:
            choose_a_random_album_by_genre()
        elif input_read == 9:
            show_the_amount_of_albums_by_an_artist()
        elif input_read == 10:
            find_the_longest_time_album()
        elif input_read == 0:
            return
        else:
            print ("Menu doesn't have this option")

        ask = ""
        while not (ask == 'YES' or ask == 'NO'):  # ask about game again
            ask = input("Do you want to try again? (YES/NO) ").upper()
        if ask == 'NO':
            break

main()
