import os

from tests_.baseTest import BaseTest
from unittest.mock import patch


class BoundaryTests(BaseTest):
    def setUp(self):
        super().setUp()

    @patch('builtins.input', side_effect=['2', 'files_/minimumLevelsFile.txt'])
    def test_boundary_minimum_levels_value(self, mock_input):
        """
            Test Case: Verify the functionality with the minimum valid levels value (2).
        """
        self.tree.create_symmetrical_tree()
        self.assertTrue(os.path.exists('files_/minimumLevelsFile.txt'), "Error: Expected file to be created, but it was not found.")
        with open('files_/minimumLevelsFile.txt', 'r') as file:
            content = file.readlines()
        expected_content = [
            "   W\n",
            "   *\n",
            " TTTTT \n",
            " TTTTT \n"
        ]
        self.assertEqual(content, expected_content, f"Error: Expected tree content does not match. Got: {content}")
        self.createdFiles.append("files_/minimumLevelsFile.txt")

    @patch('builtins.input', side_effect=['10000', 'files_/veryHighLevelsFile.txt'])
    def test_boundary_high_levels_value(self, mock_input):
        """
            Test Case: Verify the functionality with a very high number of levels.
        """
        self.tree.create_symmetrical_tree()
        self.assertTrue(os.path.exists('files_/veryHighLevelsFile.txt'), "Error: Expected file to be created, but it was not found.")
        self.createdFiles.append("files_/veryHighLevelsFile.txt")

    @patch('builtins.input', side_effect=['5', 'files_/' + 'a' * 100 + '.txt'])
    def test_boundary_long_file_path_value(self, mock_input):
        """
            Test Case: Verify the functionality with the large allowed length for a file path.
        """
        self.tree.create_symmetrical_tree()
        self.assertTrue(os.path.exists('files_/' + 'a' * 100 + '.txt'), "Error: Expected file to be created, but it was not found.")
        self.createdFiles.append('files_/' + 'a' * 100 + '.txt')

    @patch('builtins.input', side_effect=['5', 'files_/' + 'a' * 255 + '.txt'])
    def test_boundary_file_path_value_is_out_of_range(self, mock_input):
        """
            Test Case: Verify the functionality with the large allowed length for a file path.
        """
        with self.assertRaises(OSError, msg="Error: Expected OSError for out of range file path value, but no exception was raised."):
            self.tree.create_symmetrical_tree()

    @patch('builtins.input', side_effect=['5', 'files_/a.txt'])
    def test_boundary_file_path_value_min_length(self, mock_input):
        """
            Test Case: Verify the functionality with the shortest valid file path.
        """
        self.tree.create_symmetrical_tree()
        self.assertTrue(os.path.exists('files_/a.txt'), "Error: Expected file to be created, but it was not found.")
        self.createdFiles.append('files_/a.txt')
