# clean_dupliate_file
Automated script that cleans duplicate files on a system.

6 diff functions that each has a specific tasks.
GET_PATH()
has an argument, path_url.
This function collects and returns an absolute path or a string.

GET_FILES()
get_files has one argument, the 'path' returned in the get_path() function.
If an empty string was given, the directory of the path will be CWD.
(Current Working Directory)

get_files() returns a list of files that is contained in the last directory 
of the given path.

GET_RENAMED_FILES()
get_renamed_files() takes in 2 argument files, path.

list of files that are returned in the get_files() function is passed
to get_renamed_files() and the absolute path.

GET_DUPLICATE_FILES()
This function takes in an argument, files.
These files are files from the get_renamed_function.
(get_renamed_function() will rename files from get_files())

get_duplicate_files() returns list of duplicate files.

PROCEED_TO_DELETE():
This function takes in an argument, files.
If get_duplicate_files() returned an empty list, this will affect 
the delete_duplicate_files()
If get_duplicate_files() return a list of files, proceed_to_delete()
returns either the string 'y' or 'n'
