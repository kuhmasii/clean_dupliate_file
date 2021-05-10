# clean_dupliate_file
Automated script that cleans duplicate files on a system.

6 diff functions that each has a specific tasks.

GET_PATH()
has an argument, path_url.
This function collects and returns an absolute path or a string.

GET_FILES()
get_files() has one argument, the 'path' returned in the get_path() function.
If an empty string was given, the directory of the path will be CWD.
(Current Working Directory)

get_files() returns a list of files that is contained in the last directory  of the given path.

GET_RENAMED_FILES()
get_renamed_files() takes in 2 argument 'files', 'path'.

list of files that are returned in the get_files() function are passed
to get_renamed_files() and the absolute path.

GET_DUPLICATE_FILES()
This function takes in an argument, 'files'.
These files are files from the get_renamed_files().
(get_renamed_files() will rename files from get_files())

get_duplicate_files() returns list of duplicate files.

PROCEED_TO_DELETE()
This function takes in an argument, 'files'.
If get_duplicate_files() returned an empty list, this will affect 
the delete_duplicate_files()
If get_duplicate_files() return a list of files, proceed_to_delete()
returns either the string 'y' or 'n'

DELETE_DUPLIICATE_FILES()
This file takes in 3 arguments,
'files', 'path' and 'proceed'.

Files argument is the list of files from get_duplicate_files().
If there is no file present, the function delete_duplicate_files() will not run.
If there is file present, the function delete_duplicate_files() runs.

Proceed argument is the string returned in proceed_to_delete().

Path argument is the absolute path given.

delete_duplicate_files() deletes all duplicate file in a folder provided the get_duplicate_files() returns a list of files not an empty list.

