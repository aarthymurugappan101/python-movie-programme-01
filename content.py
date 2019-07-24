import sys
# for option 1 and 2
products = [
    ["Movie 1 of 6","NAME: The Avengers", "GENRE: Fantasy", "Description: Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.","price:16.50"],
    ["Movie 2 of 6","NAME: Mission: Impossible - Fallout", "GENRE: Action", "Description: Ethan Hunt and his IMF team\", along with some familiar allies\", race against time after a mission gone wrong.","price:20"],
    ["Movie 3 of 6","NAME: The Nun","GENRE: Horror","Description: A priest with a haunted past and a novice on the threshold of her final vows are sent by the Vatican to investigate the death of a young nun in Romania and confront a malevolent force in the form of a demonic nun.","price:14"],
    ["Movie 4 of 6","NAME: Incredibles 2","GENRE: Action","Description: Bob Parr (Mr. Incredible) is left to care for the kids while Helen (Elastigirl) is out saving the world.","price:12"],
    ["Movie 5 of 6","NAME: Smallfoot","GENRE: Comedy","Description: A Yeti is convinced that the elusive creatures known as \"humans\" really do exist.","price:10"],
    ["Movie 6 of 6","NAME: 96","GENRE: Romance","Description: Two high school sweethearts meet at a reunion after 22 years and reminisce about their past over the course of an evening.","price:18"]
]

# Mainmenu
selections =["1. Display all movies",
             "2. Display movie full names for selection",
             "3. Search based on Name or Category substring",
             "Q. Press Q to quit"]
# submenu for option1 
selections1 =["N. press N for next movie",
              "P. press P for previous movie",
              "M. press M for Main menu"]
# movie list options for option 2
Movienames = ["1. avengers", 
        "2. Mission: Impossible - Fallout",
        "3. The Nun",
        "4. Incredibles 2",
        "5. Smallfoot",
        "6. 96"]
# for option 3 (search)
movielist = [
    "Name: The Avengers Genre:Fantasy Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity. \"price: 16.50",
    "Name: Mission: Impossible - Fallout \"Genre: Action \"Ethan Hunt and his IMF team\", along with some familiar allies\", race against time after a mission gone wrong. \"price: 20",
    "Name: The Nun \"Genre: Horror\" A priest with a haunted past and a novice on the threshold of her final vows are sent by the Vatican to investigate the death of a young nun in Romania and confront a malevolent force in the form of a demonic nun. \"price: 14",
    "Name: Incredibles 2\" Genre: Action \"Bob Parr (Mr. Incredible) is left to care for the kids while Helen (Elastigirl) is out saving the world. \"price: 12",
    "Name: Smallfoot\" Genre: Comedy \"A Yeti is convinced that the elusive creatures known as \"humans\" really do exist. \"price: 10",
    "Name: 96 \"Genre: Romance\" Two high school sweethearts meet at a reunion after 22 years and reminisce about their past over the course of an evening. \"price: 18"]

# submenu for option 3 (search)
selections2 = ["No results found",
               "1. search again",
               "M. return to main menu"]