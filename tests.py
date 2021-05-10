import unittest
import os
from pathlib import Path
from imagecleaner import get_path, get_files, proceed_to_delete


class PathTestCase(unittest.TestCase):
    """ Tests for Paths given."""

    def test_get_path_empty(self):
        """
        If path is not given but an empty string instead,
        the path should return a period.
        """
        path = Path("")
        self.assertEqual(
            get_path(''
                     ),
            path
        )

    def test_get_path_not_empty(self):
        """
        If path is given the path should lead to its
        directory
        """
        path = Path("This is the path")
        self.assertEqual(
            get_path("This is the path"
                     ),
            path
        )


class GetFileTestCase(unittest.TestCase):
    """
    Tests for files in a directory.
    """

    def test_get_files_with_current_dir(self):
        """
        If path is not given but an empty string instead,the
        resulting path becomes a "." leading it to the CWD.
        the files in the current working directory will be
        contained in a list.
        """
        self.assertEqual(
            get_files("."
                      ),
            os.listdir()
        )

    def test_get_files_with_a_correct_path(self):
        """
        If a correct path is given, the files in that directory
        will be contained in a list.
        """
        path = Path('/')
        self.assertEqual(
            get_files(path
                      ),
            os.listdir(path)
        )


class ProceedTestCase(unittest.TestCase):
    y
    """Testing for proceed to delete"""

    def test_file_not_avalible_to_proceed(self):
        """If file is an empty list, the 
        function returns None 
        """
        self.assertEqual(
            proceed_to_delete(
                []
            ),
            None
        )

    def test_file_avalible_to_proceed_if_y(self):
        """If file is not empty, the 
        function returns a string if the provided as is yes
        'y'
        """
        self.assertEqual(
            proceed_to_delete(
                ["file-names"]
            ),
            "y"
        )

    def test_file_avalible_to_proceed_if_n(self):
        """If file is not empty, the 
        function returns a string if the provided as is yes
        'n'
        """
        self.assertEqual(
            proceed_to_delete(
                ["file-names"]
            ),
            "n"
        )


if __name__ == "__main__":
    unittest.main()
