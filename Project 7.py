menu = """

******************************
 PROJECT 7 - MENU
******************************
1. Write input to file
2. Write input to screen
3. Quit
******************************
Enter your choice [1-3]: """
open("data.txt_project_7", "a")
data = raw_input(menu)
while data == "1" or data == "2":
    if data == "1":
        user_string = raw_input("Enter a phrase: ")
        with open("data.txt_project_7", "a") as f:
            lines = f.write(user_string)
            print "Writing ... %s" % user_string
            print "Enter another piece of data, e.g. a phrase, sentence, etc."
            data = raw_input(menu)
    elif data == "2":
        user_string = raw_input("Enter a phrase: ")
        print "You entered: %s" % user_string
        print "Enter another piece of data, e.g. a phrase, sentence, etc."
        data = raw_input(menu)
    else:
        print "The program will now quit. Thank you for playing"

#opened in append ("a") mode since don't need to read the lines but need to add them to the file.

