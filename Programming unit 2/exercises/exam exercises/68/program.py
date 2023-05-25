import os
import os.path

def es68(dirname, extensions):
    """Design a function es68(dirname, extensions) such that:
    - it is recursive or uses recursive functions(s)/method(s),
    - it receives as arguments:
      - a directory pathname 'dirname', 
      - a list of strings 'extensions' representing the ending part of
         filenames, a list of strings 'words' that do not contain
      - spaces/tab/newlines
    - it counts how many files ending with any of the given extensions
      can be found in 'dirname' or any of its subdirectories.
    - it returns a dictionary where:
      - the keys are the extensions passed as argument, if at least
        one file ending with such an extension can be found, and
      - the related values are the number of files whose name ends
        with such a keys.

    Note: if no file can be found ending with a given extension, such
    a key is not included in the returned dictionary.
    """
    # insert here your code

