import unittest
from imagecleaner import get_files


class ImagecleanerTest(unittest.TestCase):

    def get_files_negative(self):
        self.assertEqual(
            get_files(''
        ),
            []
    )




if __name__ =="__main__":
    unittest.main()