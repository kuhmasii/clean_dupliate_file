import os
import re
import time
from pathlib import Path


def get_path(path="", *args, **kwargs):
    # Path will always return a string, or os.Pathlike object.
    # By default, empty Path is the current working directory
    path_url = Path(path)

    return path_url


path_url = input(
    "Copy the absolute path of the folder here!\n"
).strip(
    '"'
)

if __name__ == "__main__":
    path = get_path(path_url)


def get_files(path, *args, **kwargs):

    try:
        # If the path is not valid or just a mere word,
        # it won't lead to the directory, thus the content
        # won't be found, hence raising an error.
        image_files = os.listdir(path)

    except FileNotFoundError:
        print("Wrong path!, copy the absolute path of the folder here!.")

        # using Quit() will stop the rest of the functions from excuting
        # this will prevent the codes from encountering many errors.
        quit()

    return image_files


if __name__ == "__main__":
    files = get_files(path)


def get_renamed_files(files, path, *args, **kwargs):
    """
    We need to clear out the whitespaces in each file
    and save the new name as the name of the file.
    Representing whitespace in a file with(-).
    Eg; 'John doe' will be 'John-doe'.
    This gives flexibility when it comes to matching
    the file's name with any regex expression. 
    """

    for image_file in files:

        new_name = image_file.replace(" ", "-")
        # new_name is a string not a file's name.
        # we rename it to a file's name using the rename method

        src = os.path.join(path, image_file)
        dst = os.path.join(path_url, new_name)

        try:
            # Making sure we are not naming a file twice in same way
            # An error would be thrown if we didn't check for this
            os.rename(src, dst)
        except FileExistsError:
            print("An instance of a file to be renamed for deleting already exists")
            quit()

    return os.listdir(path)


if __name__ == "__main__":
    renamed_file = get_renamed_files(files, path)


def get_duplicate_files(files, *args, **kwargs):
    """
    Using the name of the file to check for duplicates.
    (file name will either end with (x) where x is an integer, 
    or file name will end with the word 'Copy'). This will
    give us a better chance of matching it when using regex.
    """

    duplicates = []
    # Matching the file that has an integer to indicate a copy of a file
    # eg; John-doe-(2).txt, notice the hypen between the last
    # letter of doe and the integer, this was what we fixed in
    # get_duplicate_files function above.
    pattern = re.compile(
        r"^[a-zA-Z0-9@:%_\+.~#?&//=-]+\-\([0-9]+\)\.[a-zA-Z]+$"
    )
    # pattern2 deals with our problem of a file copy having only
    # Copy not any integer, Eg; John-doe--Copy.txt
    pattern_2 = re.compile(
        r"^[a-zA-Z0-9@:%_\+.~#?&//=-]+[Copy]\.[a-zA-Z]+$"
    )

    for search_files in files:
        search_pattern = pattern.search(search_files)
        if search_pattern:
            duplicates.append(search_pattern.group())

    for search_files in files:
        search_pattern = pattern_2.search(search_files)
        if search_pattern:
            duplicates.append(search_pattern.group())

    return duplicates


if __name__ == "__main__":
    duplicate_files = get_duplicate_files(renamed_file)


def proceed_to_delete(files, *args, **kwargs):

    proceed_on = None
    if files:
        if len(files) == 1:
            print(f"This is your duplicate file {files} ")
        else:
            print(f"These are your duplicate files {files}")
        proceed_on = input("are you ready to delete?\n[y/n] ").strip(" ")

    return proceed_on


if __name__ == "__main__":
    proceed = proceed_to_delete(duplicate_files)


def delete_duplicate_files(files, path, proceed, *args, **kwargs):

    if proceed == None:
        return "Opps! no duplicate file to delete"
    elif proceed.lower() == "y":
        sure = input(
            "Are you sure?, once deleted it's gone from your system\n[y/n] "
        )
        if sure.lower() == "y":
            for delete_files in files:
                time.sleep(2)
                print(
                    f"Deleting file {delete_files}....\nPress ctrlC to break out"
                )
                file_to_remove = os.path.join(
                    path, delete_files
                )
                os.remove(
                    file_to_remove
                )
            return "Duplicate files deleted"
        elif sure.lower() == "n":
            return "Okay, No file lost."
        else:
            return "pick the right choice next time."
    elif proceed.lower() == "n":
        return "Okay, No file lost. Bye!"
    else:
        return "pick the right choice next time."


if __name__ == "__main__":
    deleted_files = delete_duplicate_files
    (
        duplicate_files,
                path, 
            proceed
    )

# print(files)
# print(renamed_file)
# print(duplicate_files)
# print(proceed)
# print(deleted_files)
# C:\Users\OLAOYE\Pictures\isaiah
