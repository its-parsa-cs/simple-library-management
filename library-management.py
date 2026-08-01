#mid-term project
#Parsa Soltanabadi, Arian Habibi


""" lists: """
members_list = [
               {"Id": 1 , "name":"Arian","last_name":"Habibi"},
               {"Id": 2 , "name":"Parsa","last_name":"Soltan abadi"},
               {"Id": 3 , "name":"Ali","last_name":"Momeni"},
               {"Id": 4 , "name":"Hossein","last_name":"Hoseini"},
               {"Id": 5 , "name":"Behrad","last_name":"Shahriari"},
               {"Id": 6 , "name":"Mohsen","last_name":"Karimi"},
               {"Id": 7 , "name":"Omid","last_name":"Rahmani"},
               {"Id": 8 , "name":"Kiarash","last_name":"Ebrahimi"},
               {"Id": 9 , "name":"Nazgol","last_name":"Mohammadi"},
               {"Id": 10 , "name":"Negin","last_name":"Ahmadi"},
               {"Id": 11 , "name":"Mahsa","last_name":"Kazemi"},
               {"Id": 12 , "name":"Fatemeh","last_name":"Rahimi"},
               {"Id": 13 , "name":"Ahmad","last_name":"Azizi"},
               {"Id": 14 , "name":"Sina","last_name":"Moradi"},
               {"Id": 15 , "name":"Leila","last_name":"Qasemi"},
               {"Id": 16 , "name":"Akbar","last_name":"Gholami"},
               {"Id": 17 , "name":"Arash","last_name":"Ghorbani"},
               {"Id": 18 , "name":"Roham","last_name":"Ebrahimi"},
               {"Id": 19 , "name":"Mohammad","last_name":"Bagheri"},
               {"Id": 20 , "name":"Mehrnoosh","last_name":"Kohestani"},
               {"Id": 21 , "name":"Siavash","last_name":"Jamshidi"},
               {"Id": 22 , "name":"Shariar","last_name":"Jalali"},
               {"Id": 23 , "name":"Mohsen","last_name":"Yousefi"},
               {"Id": 24 , "name":"Javad","last_name":"Farhadi"},
               {"Id": 25 , "name":"Nima","last_name":"Pourmohammadi"},
               {"Id": 26 , "name":"Aria","last_name":"Ameri"},
               {"Id": 27 , "name":"Arash","last_name":"Taheri"},
               {"Id": 28 , "name":"Xaniar","last_name":"Khosravi"},
               {"Id": 29 , "name":"Iman","last_name":"Dastpak"},
               {"Id": 30 , "name":"Kimia","last_name":"Ravangar"},
               {"Id": 31 , "name":"Reza","last_name":"Ayne"},
               {"Id": 32 , "name":"Amir","last_name":"Bakhtiar"},
               {"Id": 33 , "name":"Bahar","last_name":"Kohestani"},
               {"Id": 34 , "name":"Ali","last_name":"Rahimi"},
               {"Id": 35 , "name":"Sara","last_name":"Mohammadi"},
               {"Id": 36 , "name":"Reza","last_name":"Karimi"},
               {"Id": 37 , "name":"Neda","last_name":"Ahmadi"},
               {"Id": 38 , "name":"Hossein","last_name":"Hosseini"},
               {"Id": 39 , "name":"Maryam","last_name":"Ebrahimi"},
               {"Id": 40 , "name":"Amir","last_name":"Bagheri"},
               {"Id": 41 , "name":"Zahra","last_name":"Soleimani"},
               {"Id": 42 , "name":"Mehdi","last_name":"Moradi"},
               {"Id": 43 , "name":"Fatemeh","last_name":"Kazemi"},
               {"Id": 44 , "name":"Sina","last_name":"Shirazi"},
               {"Id": 45 , "name":"Leila","last_name":"Abbasi"}]
books_list   = [
              {"name": "boostan","author":"saadi" ,"year": "1257", "avalibility": "unavailable"},
              {"name": "eleanor and park", "author": "rainbow rowell", "year": "2012", "avalibility": "unavailable"},
              {"name": "golestan", "author": "saadi", "year": "1258", "avalibility": "unavailable"},
              {"name": "shahnameh", "author": "ferdowsi", "year": "1010", "avalibility": "unavailable"},
              {"name": "masnavi manavi", "author": "molavi", "year": "1273", "avalibility": "unavailable"},
              {"name": "divane Hafez", "author": "hafez", "year": "1390", "avalibility": "unavailable"},
              {"name": "gol-afshan", "author": "nezami", "year": "1180", "avalibility": "unavailable"},
              {"name": "leyli va Majnoon", "author": "qeys", "year": "1160", "avalibility": "unavailable"},
              {"name": "sir al Molouk", "author": "asir al Din Tusi", "year": "1240", "avalibility": "unavailable"},
              {"name": "manteq al Tair", "author": "attar", "year": "1190", "avalibility": "unavailable"},
              {"name": "elahi Nameh", "author": "J. K. Rowling", "year": "1260", "avalibility": "unavailable"},
              {"name": "Harry Potter 1","author":"J. K. Rowling" ,"year":"1997 ", "avalibility": "unavailable"},
              {"name": "Harry Potter 2","author":"J. K. Rowling" ,"year":"1998 ", "avalibility": "unavailable"},
              {"name": "Harry Potter 3","author":"J. K. Rowling" ,"year":"1999 ", "avalibility": "unavailable"},
              {"name": "Harry Potter 4","author":"J. K. Rowling" ,"year":"2000 ", "avalibility": "unavailable"},
              {"name": "Harry Potter 5","author":"J. K. Rowling" ,"year":"2003 ", "avalibility": "unavailable"},
              {"name": "Harry Potter 6","author":"J. K. Rowling" ,"year":"2005 ", "avalibility": "unavailable"},
              {"name": "Harry Potter 7","author":"J. K. Rowling" ,"year":"2007 ", "avalibility": "unavailable"},
              {"name": "Harry Potter 8","author":"J. K. Rowling" ,"year":"2016 ", "avalibility": "unavailable"},
              {"name": "boof-e koor","author":"sadegh hedayat" ,"year":"1937 ", "avalibility": "unavailable"},
              {"name": "golestan 2","author":"saadi" ,"year":"1258 ", "avalibility": "unavailable"},
              {"name": "boostan 2","author":"saadi" ,"year":"1257 ", "avalibility": "available"},
              {"name": "shahnameh 2","author":"ferdowsi" ,"year":"1010 ", "avalibility": "available"},
              {"name": "divan hafez 2","author":"hafez" ,"year":"1390 ", "avalibility": "available"},
              {"name": "kelidar","author":"mahmoud dolatabadi" ,"year":"1984 ", "avalibility": "available"},
              {"name": "samfonie mordegan","author":"abbas maroufi" ,"year":"1989 ", "avalibility": "available"},
              {"name": "sovashoun","author":"simin daneshvar" ,"year":"1969 ", "avalibility": "available"},
              {"name": "cheshmhayash","author":"bozorg alavi" ,"year":"1952 ", "avalibility": "available"},
              {"name": "modir-e madreseh","author":"jalal al-e ahmad" ,"year":"1958 ", "avalibility": "available"},
              {"name": "the little prince","author":"antoine de saint-exupery" ,"year":"1943 ", "avalibility": "available"},
              {"name": "animal farm","author":"george orwell" ,"year":"1945 ", "avalibility": "available"},
              {"name": "nineteen eighty four","author":"george orwell" ,"year":"1949 ", "avalibility": "available"},
              {"name": "the old man and the sea","author":"ernest hemingway" ,"year":"1952 ", "avalibility": "available"},
              {"name": "to kill a mockingbird","author":"harper lee" ,"year":"1960 ", "avalibility": "available"},
              {"name": "the great gatsby","author":"f. scott fitzgerald" ,"year":"1925 ", "avalibility": "available"},
              {"name": "moby dick","author":"herman melville" ,"year":"1851 ", "avalibility": "available"},
              {"name": "pride and prejudice","author":"jane austen" ,"year":"1813 ", "avalibility": "available"},
              {"name": "crime and punishment","author":"fyodor dostoevsky" ,"year":"1866 ", "avalibility": "available"},
              {"name": "the brothers karamazov","author":"fyodor dostoevsky" ,"year":"1880 ", "avalibility": "available"},
              {"name": "war and peace","author":"leo tolstoy" ,"year":"1869 ", "avalibility": "available"},
              {"name": "anna karenina","author":"leo tolstoy" ,"year":"1877 ", "avalibility": "available"},
              {"name": "don quixote","author":"miguel de cervantes" ,"year":"1605 ", "avalibility": "available"},
              {"name": "the alchemist","author":"paulo coelho" ,"year":"1988 ", "avalibility": "available"},
              {"name": "the stranger","author":"albert camus" ,"year":"1942 ", "avalibility": "available"},
              {"name": "the plague","author":"albert camus" ,"year":"1947 ", "avalibility": "available"},
              {"name": "the trial","author":"franz kafka" ,"year":"1925 ", "avalibility": "available"},
              {"name": "metamorphosis","author":"franz kafka" ,"year":"1915 ", "avalibility": "available"},
              {"name": "the hobbit","author":"j.r.r. tolkien" ,"year":"1937 ", "avalibility": "available"},
              {"name": "the lord of the rings","author":"j.r.r. tolkien" ,"year":"1954 ", "avalibility": "available"},
              {"name": "harry potter and the philosopher's stone","author":"j.k. rowling" ,"year":"1997 ", "avalibility": "available"},
              {"name": "harry potter and the chamber of secrets","author":"j.k. rowling" ,"year":"1998 ", "avalibility": "available"},
              {"name": "harry potter and the prisoner of azkaban","author":"j.k. rowling" ,"year":"1999 ", "avalibility": "available"},
              {"name": "the hunger games","author":"suzanne collins" ,"year":"2008 ", "avalibility": "available"},
              {"name": "catching fire","author":"suzanne collins" ,"year":"2009 ", "avalibility": "available"},
              {"name": "mockingjay","author":"suzanne collins" ,"year":"2010 ", "avalibility": "available"},
              {"name": "the fault in our stars","author":"john green" ,"year":"2012 ", "avalibility": "available"},
              {"name": "inferno","author":"dan brown" ,"year":"2013 ", "avalibility": "unavailable"},
              {"name": "the da vinci code","author":"dan brown" ,"year":"2003 ", "avalibility": "available"},
              {"name": "angels and demons","author":"dan brown" ,"year":"2000 ", "avalibility": "available"},
              {"name": "the kite runner","author":"khaled hosseini" ,"year":"2003 ", "avalibility": "available"},
              {"name": "a thousand splendid suns","author":"khaled hosseini" ,"year":"2007 ", "avalibility": "available"},
              {"name": "life of pi","author":"yann martel" ,"year":"2001 ", "avalibility": "available"},
              {"name": "the book thief","author":"markus zusak" ,"year":"2005 ", "avalibility": "available"},
              {"name": "the road","author":"cormac mccarthy" ,"year":"2006 ", "avalibility": "unavailable"},
              {"name":"diary of a wimpy kid","author":"jeff kinney","year":"2007","avalibility":"available"},
              {"name":"blindness","author":"jose saramago","year":"1995","avalibility":"available"},
              {"name":"the stranger","author":"albert camus","year":"1942","avalibility":"available"},
              {"name":"the trial","author":"franz kafka","year":"1925","avalibility":"available"},
              {"name":"metamorphosis","author":"franz kafka","year":"1915","avalibility":"available"},
              {"name":"staring at the sun","author":"irvin yalom","year":"2008","avalibility":"available"},
              {"name":"the art of war","author":"sun tzu","year":"500bc","avalibility":"available"},
              {"name":"animal farm","author":"george orwell","year":"1945","avalibility":"available"},
              {"name":"notes from underground","author":"fyodor dostoevsky","year":"1864","avalibility":"available"},
              {"name":"the death of ivan ilyich","author":"leo tolstoy","year":"1886","avalibility":"available"},
              {"name":"the old man and the sea","author":"ernest hemingway","year":"1952","avalibility":"available"},
              {"name":"the giver","author":"lois lowry","year":"1993","avalibility":"available"},
              {"name":"fahrenheit 451","author":"ray bradbury","year":"1953","avalibility":"available"},
              {"name":"the road","author":"cormac mccarthy","year":"2006","avalibility":"available"},
              {"name":"norwegian wood","author":"haruki murakami","year":"1987","avalibility":"available"},
              {"name":"sputnik sweetheart","author":"haruki murakami","year":"1999","avalibility":"available"},
              {"name":"the alchemist","author":"paulo coelho","year":"1988","avalibility":"available"},
              {"name":"veronika decides to die","author":"paulo coelho","year":"1998","avalibility":"available"},
              {"name":"brave new world","author":"aldous huxley","year":"1932","avalibility":"available"},
              {"name":"lord of the flies","author":"william golding","year":"1954","avalibility":"available"},
              {"name":"the bell jar","author":"sylvia plath","year":"1963","avalibility":"available"},
              {"name":"the little prince","author":"antoine de saint-exupery","year":"1943","avalibility":"available"},
              {"name":"the catcher in the rye","author":"j.d. salinger","year":"1951","avalibility":"available"},
              {"name":"of mice and men","author":"john steinbeck","year":"1937","avalibility":"available"},
              {"name":"the pearl","author":"john steinbeck","year":"1947","avalibility":"available"},
              {"name":"the book thief","author":"markus zusak","year":"2005","avalibility":"available"},
              {"name":"life of pi","author":"yann martel","year":"2001","avalibility":"available"},
              {"name":"the fault in our stars","author":"john green","year":"2012","avalibility":"available"},
              {"name":"looking for alaska","author":"john green","year":"2005","avalibility":"available"},
              {"name":"paper towns","author":"john green","year":"2008","avalibility":"available"},
              {"name":"the hunger games","author":"suzanne collins","year":"2008","avalibility":"available"},
              {"name":"catching fire","author":"suzanne collins","year":"2009","avalibility":"available"},
              {"name":"mockingjay","author":"suzanne collins","year":"2010","avalibility":"available"},
              {"name":"divergent","author":"veronica roth","year":"2011","avalibility":"available"},
              {"name":"insurgent","author":"veronica roth","year":"2012","avalibility":"available"},
              {"name":"allegiant","author":"veronica roth","year":"2013","avalibility":"available"},
              {"name":"the maze runner","author":"james dashner","year":"2009","avalibility":"available"},
              {"name":"the scorch trials","author":"james dashner","year":"2010","avalibility":"available"},
              {"name":"the death cure","author":"james dashner","year":"2011","avalibility":"available"},
              {"name":"the outsiders","author":"s.e. hinton","year":"1967","avalibility":"available"},
              {"name":"a monster calls","author":"patrick ness","year":"2011","avalibility":"available"},
              {"name":"the perks of being a wallflower","author":"stephen chbosky","year":"1999","avalibility":"available"},
              {"name":"the graveyard book","author":"neil gaiman","year":"2008","avalibility":"available"},
              {"name":"coraline","author":"neil gaiman","year":"2002","avalibility":"available"},
              {"name":"neverwhere","author":"neil gaiman","year":"1996","avalibility":"available"},
              {"name":"good omens","author":"terry pratchett","year":"1990","avalibility":"available"},
              {"name":"the lightning thief","author":"rick riordan","year":"2005","avalibility":"available"},
              {"name":"the sea of monsters","author":"rick riordan","year":"2006","avalibility":"available"},
              {"name":"the titan's curse","author":"rick riordan","year":"2007","avalibility":"available"},
              {"name":"the last olympian","author":"rick riordan","year":"2009","avalibility":"available"},
              {"name":"the night circus","author":"erin morgenstern","year":"2011","avalibility":"available"},
              {"name":"shadow and bone","author":"leigh bardugo","year":"2012","avalibility":"available"},
              {"name":"six of crows","author":"leigh bardugo","year":"2015","avalibility":"available"},
              {"name":"the midnight library","author":"matt haig","year":"2020","avalibility":"available"},
              {"name":"reasons to stay alive","author":"matt haig","year":"2015","avalibility":"available"},
              {"name":"the silent patient","author":"alex michaelides","year":"2019","avalibility":"available"},
              {"name":"after dark","author":"haruki murakami","year":"2004","avalibility":"available"},
              {"name":"kafka on the shore","author":"haruki murakami","year":"2002","avalibility":"available"},
              {"name":"the wind-up bird chronicle","author":"haruki murakami","year":"1994","avalibility":"available"},
              {"name":"the shadow of the wind","author":"carlos ruiz zafon","year":"2001","avalibility":"available"},
              {"name":"perfume","author":"patrick suskind","year":"1985","avalibility":"available"},
              {"name":"shantaram","author":"gregory david roberts","year":"2003","avalibility":"available"},
              {"name":"the kite runner","author":"khaled hosseini","year":"2003","avalibility":"available"},
              {"name":"a thousand splendid suns","author":"khaled hosseini","year":"2007","avalibility":"available"},
              {"name":"the catcher was a spy","author":"nicholas dawidoff","year":"1994","avalibility":"available"},
              {"name":"the man who mistook his wife for a hat","author":"oliver sacks","year":"1985","avalibility":"available"},
              {"name":"the curious incident of the dog in the night-time","author":"mark haddon","year":"2003","avalibility":"available"},
              {"name":"the time keeper","author":"mitch albom","year":"2012","avalibility":"available"},
              {"name":"tuesdays with morrie","author":"mitch albom","year":"1997","avalibility":"available"},
              {"name":"we were liars","author":"e. lockhart","year":"2014","avalibility":"available"},
              {"name":"the grave between us","author":"tal bauer","year":"2021","avalibility":"available"},
              {"name":"the ocean at the end of the lane","author":"neil gaiman","year":"2013","avalibility":"available"},
              {"name":"room","author":"emma donoghue","year":"2010","avalibility":"available"},
              {"name":"the girl with all the gifts","author":"m.r. carey","year":"2014","avalibility":"available"},
              {"name":"the boy in the striped pajamas","author":"john boyne","year":"2006","avalibility":"available"},
              {"name":"the sense of an ending","author":"julian barnes","year":"2011","avalibility":"available"},
              {"name":"the handmaid's tale","author":"margaret atwood","year":"1985","avalibility":"available"},
              {"name":"american gods","author":"neil gaiman","year":"2001","avalibility":"available"},
              {"name":"the yellow wallpaper","author":"charlotte perkins gilman","year":"1892","avalibility":"available"},
              {"name":"never let me go","author":"kazuo ishiguro","year":"2005","avalibility":"available"},
              {"name":"the lovely bones","author":"alice sebold","year":"2002","avalibility":"available"},
              {"name":"the girl on the train","author":"paula hawkins","year":"2015","avalibility":"available"},
              {"name":"dark places","author":"gillian flynn","year":"2009","avalibility":"available"},
              {"name":"sharp objects","author":"gillian flynn","year":"2006","avalibility":"available"},
              {"name":"the other boleyn girl","author":"philippa gregory","year":"2001","avalibility":"available"},
              {"name":"a walk to remember","author":"nicholas sparks","year":"1999","avalibility":"available"}]
loans_list   = [
    {"Id": 2, "name": "Harry Potter 1", "date": "2025-9-12"},
    {"Id": 2, "name": "Harry Potter 2", "date": "2025-9-12"},
    {"Id": 2, "name": "Harry Potter 3", "date": "2025-9-12"},
    {"Id": 2, "name": "Harry Potter 4", "date": "2025-9-12"},
    {"Id": 2, "name": "Harry Potter 5", "date": "2025-9-12"},
    {"Id": 2, "name": "Harry Potter 6", "date": "2025-9-12"},
    {"Id": 2, "name": "Harry Potter 7", "date": "2025-9-12"},
    {"Id": 2, "name": "Harry Potter 8", "date": "2025-9-12"},
    {"Id": 2, "name": "Eleanor and park", "date": "2025-9-12"},
    {"Id": 2, "name": "the fault in our stars", "date": "2025-9-12"},
    {"Id": 2, "name": "inferno", "date": "2024-9-12"},
    {"Id": 4, "name": "golestan", "date": "2025-9-12"},
    {"Id": 5, "name": "shahnameh", "date": "2023-9-12"},
    {"Id": 1, "name": "masnavi manavi", "date": "2025-9-12"},
    {"Id": 1, "name": "the road", "date": "2025-9-12"},
    {"Id": 1, "name": "divane Hafez", "date": "2025-9-12"},
    {"Id": 1, "name": "gol-afshan", "date": "2025-9-12"},
    {"Id": 1, "name": "leyli va Majnoon", "date": "2025-9-12"},
    {"Id": 1, "name": "sir al Molouk", "date": "2025-9-12"},
    {"Id": 1, "name": "manteq al Tair", "date": "2025-9-12"},
    {"Id": 1, "name": "elahi Nameh", "date": "2025-9-12"},
    {"Id": 1, "name": "boof-e koor", "date": "2022-9-12"},
    {"Id": 1, "name": "boostan", "date": "2019-9-12"}]


""" the MAIN MENU """
def menu():
      while True:
        print("")
        print("****** MENU ******")
        print("1: books")
        print("2: members")
        print("3: borrow books")
        print("4: return books")
        print("5: check availibility")
        print("6: reports")
        print("7: exit")
        n= input("Enter the number of your request: ")

        if n == "1":
             books()
        elif n== "2":
             members()
        elif n == "3":
             borrow_book()
        elif n == "4":
             return_book()
        elif n == "5":
             check_availibility()
        elif n == "6":
             reports()
        elif n == "7":
             print("exiting...")
             break
        else:
             print(" invalid input ")



""" from the main menu """
def books():
     # Book Menu And Their Funtions
    print("")
    print("---- BOOKS ----")
    print("1: add a book")
    print("2: search up a book")
    print("3: show all")
    print("4: remove a book")
    print("5: exit")
    n= input("Enter the number of your request: ")

    if n == "1":
         add_book()
    elif n == "2":
         search_books()
    elif n == "3":
         display_all_books()
    elif n == "4":
         delete_book()
    elif n == "5" :
         print(" exiting... ")
         menu()
    else:
         print(" invalid input ")
# ---- minor book defs ----
def add_book():
    # checks if the books exists or not.
    # if the book doesn't exist, it adds it to the list
    print("You have chosen to add a book.")
    name = input("name of the book: ")
    author = input("author: ")
    year = input("year of release: ")
    for book in books_list:
        if book['name'].lower() == name.lower() and book['author'].lower() == author.lower() and book['year'] == year:
            print("This book already exist in the list.")
            proceed()
            return
    books_list.append({"name": name,"author": author,"year": year})  # ذخیره در لیست بیرونی
    print("Book added successfully!")
    proceed()
def search_books():
     if not books_list:
        print("")
        print("")
        print("")
        print("No books added yet.")
        return
     search = input("Enter the name of the book to search: ")
     found = False
     for book in books_list:
         if book['name'].lower() == search.lower():
             print(f"Book found: Name: {book['name']}, Author: {book['author']}, Year: {book['year']}")
             found = True
             proceed()
     if not found:
         print("Book not found.")
         proceed()
def display_all_books():
     if not books_list:
        print("")
        print("")
        print("")
        print("No books added yet.")
        return
     print("---- All Books ----")
     for book in books_list:
         print(f"Name: {book['name']}, Author: {book['author']}, Year: {book['year']}")
         print("----------------------------")
     proceed()
def delete_book():
     book_name= input("Enter the name of the book to delete: ")
     for loan in loans_list:
         if loan["name"].lower() == book_name.lower():
             print("This book is unavailable and can't be deleted")
             proceed()
             return

     for book in books_list:
         if book["name"].lower() == book_name.lower():
             books_list.remove(book)
             print("Book deleted successfully!")
             proceed()
             return
     else:
         print("This book doesn't exist")
         proceed()



""" from the main menu """
def members():
    # Member menu and their functions
    print("")
    print("---- MEMBERS ----")
    print("1: add a member ")
    print("2: remove a member ")
    print("3: search up a member")
    print("4: display all members")
    print("5: exit")
    n= input("Enter the number of your request: ")


    if n == "1":
         add_member()
    elif n == "2":
         delete_member()
    elif n == "3":
         search_member()
    elif n == "4":
         display_all_members()
    elif n == "5" :
         print(" exiting... ")
         menu()
    else:
         print(" invalid input ")
# ---- minor member defs ----
def add_member():
     print("You have chosen to add a member.")
     for member in members_list:
         new_id= member["Id"]
     new_id += 1
     name = input("first name of the member: ")
     last_name= input("last name of the member: ")
     print(f"Your id is: {new_id}")
     members_list.append({'Id': new_id, "name": name, "last_name": last_name})
     print("Member added successfully!")
     proceed()
def delete_member():
    member_id = int(input("Enter the ID of the member you want to delete: "))

    # if it is in loans list or not
    for loan in loans_list:
        if loan['Id'] == member_id:
            print("This member has loans to return.")
            proceed()
            return

    # if it had no loans then delete it
    for member in members_list:
        if member["Id"] == member_id:
            members_list.remove(member)
            print(f"Member with id '{member_id}' and name '{member['name']}' deleted successfully.")
            proceed()
            return

    # if it doesn't exist
    print("No member found with this ID.")
    proceed()
def search_member():
     if not members_list:   # اگر لیست خالی بود
        print("")
        print("")
        print("")
        print("No members added yet.")
        proceed()
        return

     search = input("Enter the last name of the member to search: ")
     found = False
     for member in members_list:
         if member['last_name'].lower() == search.lower():      # مقایسه بدون حساسیت به حروف بزرگ و کوچیک
             print(f"member found: Name: {member['name']}, last name: {member['last_name']}")
             found = True
             proceed()
     if not found:
         print("member not found.")
         proceed()
def display_all_members():
     if not members_list:   # اگر لیست خالی بود
        print("")
        print("")
        print("")
        print("No members added yet.")
        return
     print("---- All members ----")
     for member in members_list:
         print(f"Id: {member['Id']} ,Name: {member['name']}, last_name: {member['last_name']}")
         print("------------------------------")
     proceed()



""" from the main menu """
def borrow_book():
     #borrow book function from the main menu
     # the date needs to be seperated by -s.
     # checks if the member is in the list or not

     book_name = input("Enter the name of the book to borrow: ")
     member_name= int(input("Enter your ID: "))
     if find_member_id(member_name) == "unknown member":
         print("Member doesn't exist.")
         return

     found = None
     for book in books_list:
         if book['name'].lower() == book_name.lower() and book['avalibility'] == "available" :
             found = book
             break

     if found:
         borrow_date= input("Enter today's date: (YYYY-MM-DD) ")
         loans_list.append({'Id': member_name, 'name': found["name"], 'date': borrow_date})
         found['avalibility'] = 'unavailable'
         print(f"Book {book_name} borrowed successfully.")
         proceed()
     else:
         print("the book isn't availible or doesn't exist")
         proceed()



""" from the main menu """
def return_book():
     # return book function from the main menu
     # removes the infos from loans list
     member_name= int(input("Enter your ID: "))
     book_name = input("Enter the name of the book for returning: ")
     book_found = None

     for book in books_list:
         if (book["name"].lower() == book_name.lower() and book["avalibility"] == "unavailable"):
             book_found = book
             break
     if book_found:
       book_found["avalibility"] = "available"

     found = None
     for loan in loans_list:
         if loan['name'].lower() == book_name.lower() and book_found:
             found = loan
             break

     if found:
         borrow_date= input("Enter the date you borrowed the book: (YYYY-MM-DD) ")
         loans_list.remove({'Id': member_name, 'name': book_name, 'date': borrow_date})
         print(f"Book {book_name} has been returned successfully.")
         proceed()
     else:
         print("you already returned the book or your input was incorrect")
         proceed()



""" from the main menu """
def check_availibility():
     # check availibility from the main menu
     name= input("Enter the name of the book: ")
     for book in books_list:
         if name.lower() == book['name'].lower():
             print(f"- {book['avalibility']}")
             print("")
             return proceed()
     print("the book is not in the list")
     proceed()



""" from the main menu """
def reports():
     # the report menu. takes 2 choices
     print("")
     print("---- REPORTS ----")
     print("1: overall reports")
     print("2: overdue loans reports")
     print("3: exit")

     x= input("Enter the number of your request: ")
     if x == "1":
         generate_reports()
     elif x == "2":
         show_overdue_loans()
     elif x == "3":
         print("exiting...")
         menu()
     else:
          print("Invalid input")
# ---- minor report defs ----
def generate_reports():
     # overall reports for the report menu
     # shows the number of: books/members/loans
     n_members= len(members_list)
     n_books= len(books_list)
     n_loans= len(loans_list)
     #n_overdue= len(overdue_loans_list)
     print("")
     print(f"the number of members: {n_members}")
     print(f"the number of books: {n_books}")
     print(f"the number of loans: {n_loans}")
     #print(f"the number of overdue loans: {n_overdue}")
     proceed()
def find_member_id(member_id):
    # id to name convertor
    for member in members_list:
        if member["Id"] == member_id:
            return print(f"info: {member['name']} {member['last_name']}")
    return "unknown member"
def show_overdue_loans():
     # in our library, loans become overdue when 1 year passes. (not using time module)
     # shows the overdues from the loan list, plus the info of the user
     ayear_due= "2024-09-12"
     for loan in loans_list:
         if loan['date'] < ayear_due:
              print("")
              print(f" id of the member: {loan['Id']}")
              find_member_id(loan['Id'])
              print(f" the name of the book: {loan['name']}")
              print(f" the date of the borrowing: {loan['date']}")
     proceed()


#good looking def
def proceed():
    #for a cleaner look
    print("")
    input("press Enter to proceed")


# the RUN
menu = menu()
