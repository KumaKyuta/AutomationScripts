import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Prevents root window from appearing
Tk().withdraw()

# Choose current working directory to use
current_directory = askdirectory()

# Gets list of all files in chosen directory
files_to_edit = os.listdir(current_directory)


def fix_date():
    # Loops through each file found
    for file in files_to_edit:

        # Instantiates old_file variable to store the old file
        old_filename = file

        # Separates necessary parts of file so that there's a title, date, and file extension
        # Instantiates new_date variable to store the new date
        new_date = ''
        title = file[0:14]
        date_ext = file[14:-1]
        date_to_edit = file[14:-5]
        ext = file[-5:-1]

        # Dates should be in MM/DD/YY format, if date is already in proper format there's no need to change the date
        if len(date_to_edit) < 8:

            # Splits each part of the date up, using '.' as the indicator for where to split
            # Stores result as list into portions
            portions = date_to_edit.split('.')
            
            # If current date only has a month and day, creates a year for the date and appends it to a list
            if len(portions) < 3:
                portions.append('21')
            
            # Loops through list containing each portion of the date and adds leading zeroes to month and day if necessary
            # Adds each part of date to variable containing new date string
            for idx, portion in enumerate(portions):
                if len(portion) < 2:
                    portion = '0' + portion
                new_date += portion
                if idx < 2:
                    new_date += '.'
            
            # Concatenates path, title, date, and extension into single string
            new_filename = title + new_date + ext

            # Concatenates path and file name into single string for old filename and new filename
            old_filename = os.path.join(current_directory, old_filename)
            new_filename = os.path.join(current_directory, new_filename)

            # Renames file 
            os.rename(old_filename, new_filename)


def fix_extension():
    for file in files_to_edit:
        old_filename = os.path.join(current_directory, file)
        new_filename = old_filename.replace('xl', 'xlsx')
        os.rename(old_filename, new_filename)


fix_extension()