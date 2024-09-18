import time
import os

from tests_.baseTest import BaseTest
from unittest.mock import patch


class PerformanceTests(BaseTest):
    def setUp(self):
        super().setUp()

    @patch('builtins.input', side_effect=['1000', 'files_/largeLevelsFile.txt'])
    def test_performance_large_levels_value(self, mock_input):
        """
            Test Case: Verify the performance with a large number of levels.
        """
        startTime = time.time()
        self.tree.create_symmetrical_tree()
        endTime = time.time()
        self.assertTrue(os.path.exists('files_/largeLevelsFile.txt'), "Error: Expected file to be created, but it was not found.")

        responseTime = endTime - startTime
        self.assertLess(responseTime, 0.1, f"Error: Response time is {responseTime} seconds, which exceeds the acceptable limit of 0.1 seconds")
        self.createdFiles.append("files_/largeLevelsFile.txt")

    @patch('builtins.input', side_effect=['10', 'files_/smallLevelsFile.txt'])
    def test_performance_small_levels_value(self, mock_input):
        """
            Test Case: Verify the performance with a small number of levels.
        """
        startTime = time.time()
        self.tree.create_symmetrical_tree()
        endTime = time.time()
        self.assertTrue(os.path.exists('files_/smallLevelsFile.txt'), "Error: Expected file to be created, but it was not found.")

        responseTime = endTime - startTime
        self.assertLess(responseTime, 0.01, f"Error: Response time is {responseTime} seconds, which exceeds the acceptable limit of 0.01 second")
        self.createdFiles.append("files_/smallLevelsFile.txt")

    @patch('builtins.input', side_effect=['100', 'files_/mediumLevelsFile.txt'])
    def test_performance_medium_levels_value(self, mock_input):
        """
            Test Case: Verify the performance with a medium number of levels.
        """
        startTime = time.time()
        self.tree.create_symmetrical_tree()
        endTime = time.time()
        self.assertTrue(os.path.exists('files_/mediumLevelsFile.txt'), "Error: Expected file to be created, but it was not found.")

        responseTime = endTime - startTime
        self.assertLess(responseTime, 0.008, f"Error: Response time is {responseTime} seconds, which exceeds the acceptable limit of 0.005 seconds")
        self.createdFiles.append("files_/mediumLevelsFile.txt")
