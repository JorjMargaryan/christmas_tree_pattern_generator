import unittest
import os

from sources_.christmasTree import ChristmasTree
from common_.utilities_.customLogger import logger


class BaseTest(unittest.TestCase):
    """
        This class provides a generic base for all test cases, including common setup and teardown methods.
    """
    def setUp(self):
        self.tree = ChristmasTree()
        self.createdFiles = []  # List to track created files

    def tearDown(self):
        # Clean up any test files created during the tests
        print(self.createdFiles)
        for filePath in self.createdFiles:
            if os.path.exists(filePath):
                os.remove(filePath)
                # pass
                logger("INFO", f"The file '{filePath}' is removed successfully")
