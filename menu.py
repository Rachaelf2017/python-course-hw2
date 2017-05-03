from sys import argv
from datetime import date, timedelta
# import datetime
from os.path import exists

def select_menu(menu_list, my_date):
    ordinals = ['First', 'Second', 'Third', 'Fourth', 'Fifth']

    #Figure out which month the next Sunday is in.
    my_date_day = my_date.weekday()
    days_away_from_sunday = 6 - my_date_day
    next_sunday = my_date + timedelta(days=days_away_from_sunday)
    next_sunday_month = next_sunday.month

    #Then figure out whether its the first Sunday, the second, etc.
    first_day_of_that_month = date(next_sunday.year, next_sunday_month, 1)
    sunday_number = (next_sunday.day / 7)

    #Now find the menu
    for menu in menu_list:
        menu_week = menu.split(']')[0]
        month_string = next_sunday.strftime("%B")
        ordinal_string = ordinals[sunday_number]

        if (month_string in menu_week) and (ordinal_string in menu_week):
            output = "It's the %s Sunday in %s and the menu is: " % (ordinal_string, month_string)
            return output + menu.split(']')[1]
# indent one level after this if statment. Ignore it for now, work underneath it.
if __name__ == '__main__':


    # This Sunday dinner menu planning tool requires that you supply
    # the cookbook as a text file.
    # 1. Read the path to the cookbook file and header file as command line arguments
    # store them in cook_book_path and header_file_path respectively.

    # from sys import argv

    script, cook_book_path, header_file_path = argv

    # print cook_book_path
    # print header_file_path

    # 2. Create a variable called (exactly) cook_book_text and read the file contents from cook_book_path into the variable.

    cook_book_open= open(cook_book_path)
    # print cook_book_open.read()
    cook_book_text=cook_book_open.read()
    # print cook_book_text

    # 3. Now, uncomment these two lines, your program should now print one menu
    menus = cook_book_text.split('[Sidenote:')
    # print menus[1]

    # 4. Now, write 3 commandline prompts
    # one for the month (as a number)
    my_month= raw_input("Month: ")
    # one for the date
    my_date= raw_input("Date: ")
    # # and one for the year (four digits). The value should be stored as
    my_year= raw_input("Year: " )

    # input_date= my_month+"/"+my_date+"/"+my_year
    # print input_date

    # variables my_month, my_date, my_year repectively and exactly.

    # correct_date_str= my_month + "/" + my_date + "/" + my_year
    # # print correct_date_str
    # correct_date_obj = datetime.datetime.strptime(correct_date_str,'%m/%d/%Y')
    # print correct_date_obj
    # print type(correct_date_obj)

    # my_birthday_str = birthdate+'/' + `today.year`
    # my_birthday_obj = datetime.strptime(my_birthday_str, '%m/%d/%Y')


    # 5. Now remove the print statement from (3) and uncomment the following line
    #   your program should not print a menu
    #   for the next sunday after the specific date.

    #I had to change this to get it to work.
    # print select_menu(menus,correct_date_obj)

    print select_menu(menus,date(my_year,my_month,my_date))

    # 6. Now we are going to get ready to write the output to a file instead.
    #   The file name should be output.txt and it should be in the same
    #   directory as where the program was run from
    #   we want the user to be able to cancel if the file already exists
    #   look at the book, Exercise 17 for how to do this.
    #   Then add the lines here to check if the file exists and prompt the user
    #   to continue. It's ok to use exactly what the book shows.


    # script, from_file, to_file = argv
    #
    # print "Copying from %s to %s" % (from_file, to_file)
    #
    # # we could do these two on one line, how?
    # in_file = open(from_file)
    # indata = in_file.read()
    #
    # print "The input file is %d bytes long" % len(indata)
    #
    # print "Does the output file exist? %r" % exists(to_file)
    # print "Ready, hit RETURN to continue, CTRL-C to abort."
    # raw_input()
    #
    # out_file = open(to_file, 'w')
    # out_file.write(indata)
    #
    # out_file.close()
    # in_file.close()

    # 7. Now remove the print statement in (5) and write out to the file instead.
    #   Remember to test the
    #   Behaviour of (6) and check the contents of the file.


    # 8. Try reading the code I wrote. Find the place where I am intentionally
    #   using integer division. In a comment below, explain what that line
    #   of code does and how.

    # 9. Now modify your output to always put a header at the top.
    # The header should be read from header.txt, and this should be passed in
    # as a commandline argument from step 1.

    # 10. To submit, submit this file. If you are having trouble, make sure
    #   whatever you have RUNS WITHOUT ERRORS. Comment out anything you haven't
    #   successfully debugged yet.
