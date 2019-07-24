'''
DISPLAY MAIN MENU 1,2,3,q
ask for input
invalid in put handling
option 1 :
        display all the movies
        display the first product 
        ask user input N for next movie
        p for prev
        M for main menu

option 2:
        display movies full names for selection
        display all the products for selection
        ask user input to select number or enter m dor main menu

option 3:
        search by name or category 
        cannot be case sensitive
        ask for user input 
        display results
        display menu 
        1 search again
        2 main menu

option q :
        quit the apllication
bonus* if read data from a text file 
use lists 
import data from scource file
create a main menu design
declare a variable to keep the loop running
ask for user input
display and navigate the content 
'''
# For create a list for main menu
# print main menu
# ask user for input to navigate trough the main menu
# declare a variable for index slicing
import content
MainMenu = content.selections
print(30 * "-", "MENU", 30 * "-")
print(*MainMenu, sep='\n')
print(67*"-")
choice = input("please enter your selection")
print(67*"-")
index = 0  # beginning of the movies
# **** choice 1 ****
# using while command execute the program
# create a product list
# display the product one by one using print command and index
# create a list for submenu and print it
# prompt user input for the submenu
# use if/elif commands and index to display next and prev items
# and the M for main menu
while True:
        if choice == "1":
                print("you have selected display all the movies")
                print(82*"-")
                Movies = content.products
                print(*Movies[index], sep='\n')
                print(82*"-")
                print(*content.selections1, sep='\n')
                usrinpts = input("please enter your selection")
                if usrinpts == "N":
                        index += 1
                elif usrinpts == "P":
                        index -= 1
                elif usrinpts == "M":
                        print(30 * "-", "MENU", 30 * "-")
                        print(*MainMenu, sep='\n')
                        print(67*"-")
                        choice = input("please enter your selection")
                        print(67*"-")
        #  **** choice 2 ****
        # create a list for the movie names and their numbers
        # using index display products form1 to 6 one by one by prompting the user for numbers
        # and exit to main menu if the user input is M
        elif choice == "2":
                print("you have selected display full movies names for selection")
                print(20*"-")
                movlist = content.Movienames
                print(*movlist, sep="\n")
                print(20*"-")
                print("Enter M to return to the Main Menu")
                usrinpts1 = input("please enter your selection")
                if usrinpts1 == "1":
                        print(20*"-")
                        print(*content.products[0], sep="\n")
                        print(20*"-")
                        print("Enter M to return to the previous Menu")      
                elif usrinpts1 == "2":
                        print(20*"-")
                        print(*content.products[1], sep="\n")
                        print(20*"-")
                        print("Enter M to return to the previous Menu")
                elif usrinpts1 == "3":
                        print(20*"-")
                        print(*content.products[2], sep="\n")
                        print(20*"-")
                        print("Enter M to return to the previous Menu")
                elif usrinpts1 == "4":
                        print(20*"-")
                        print(*content.products[3], sep="\n")
                        print(20*"-")
                        print("Enter M to return to the previous Menu")
                elif usrinpts1 == "5":
                        print(20*"-")
                        print(*content.products[4], sep="\n")
                        print(20*"-")
                        print("Enter M to return to the previous Menu")
                elif usrinpts1 == "6":
                        print(20*"-")
                        print(*content.products[5], sep="\n")
                        print(20*"-")
                        print("Enter M to return to the previous Menu")
                elif usrinpts1 == "M":
                        print(67 * "-")
                        print(*MainMenu, sep='\n')
                        print(67*"-")
                        choice = input("please enter your selection")
                        print(67*"-")

        #  **** choice 3 ****
        #  firstly prompt user for an input for search
        # create a modified movie list without []
        # create an empty list inorder to filter movies
        #  append the search and make it non case sensitive by using.lower()
        # print the search results
        # create a list for the submenu
        # prompt the user for another input to search again ot exit to the main menu
        elif choice == "3":
                print("you have selected 3... search based on name or category")
                search = input("please enter your search input")
                movilist = content.movielist
                filtermovies = []
                for word in movilist:
                        if search.lower() in word.lower():
                                filtermovies.append(word)
                                str_word ="".join(word)
                                print(20*"-")
                                print(*filtermovies, sep="\n")
                                print(20*"-")
                                print("1. search again")
                                print("M. return to main menu")
                                print(20*"-")
                                ch3input = input("please enter your selection")
                                if search.lower() not in word.lower():
                                        print(20*"-")
                                        print(*content.selections2, sep="\n")
                                        print(20*"-")
                                        ch3input = input("please enter your selection")
                                if ch3input == ("1"):
                                        search = input("please enter your search input")
                                        if search.lower() in word.lower():
                                                filtermovies.append(word)
                                                str_word ="".join(word)
                                                print(20*"-")
                                                print(*filtermovies, sep="\n")
                                                print(20*"-")
                                if ch3input == "M":
                                        print(30 * "-", "MENU", 30 * "-")
                                        print(*MainMenu, sep='\n')
                                        print(67*"-")
                                        choice = input("please enter your selection")
                                        print(67*"-")
        #  **** choice Q ****
        # assign Q to a variable
        # use while > break to quit the programme
        Q = "quit"
        if choice == "Q":
                break
        # ***THE END***
else:
        pass



