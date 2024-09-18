import os

from tests_.baseTest import BaseTest
from unittest.mock import patch


class FunctionalTests(BaseTest):
    def setUp(self):
        super().setUp()

    @patch('builtins.input', side_effect=['5', 'validFile.txt'])
    def test_valid_inputs(self, mock_input):
        """
            Test Case: Verify the functionality with valid levels and file path.
        """
        self.tree.create_symmetrical_tree()
        self.assertTrue(os.path.exists('validFile.txt'), "Error: Expected file to be created, but it was not found.")
        with open('validFile.txt', 'r') as file:
            content = file.readlines()
        expected_content = [
            "         W\n",
            "         *\n",
            "       @*****       \n",
            "     *********@     \n",
            "   @*************   \n",
            "       TTTTT       \n",
            "       TTTTT       \n"
        ]
        self.assertEqual(content, expected_content, f"Error: Expected tree content does not match. Got: {content}")
        self.createdFiles.append("validFile.txt")

    @patch('builtins.input', side_effect=['5', 'files_/validFile2.txt'])
    def test_valid_inputs_file_path_contains_directory_name(self, mock_input):
        """
            Test Case: Verify the functionality with valid levels and file path. The file path value contains directory name.
        """
        self.tree.create_symmetrical_tree()
        self.assertTrue(os.path.exists('files_/validFile2.txt'), "Error: Expected file to be created, but it was not found.")
        with open('files_/validFile2.txt', 'r') as file:
            content = file.readlines()
        expected_content = [
            "         W\n",
            "         *\n",
            "       @*****       \n",
            "     *********@     \n",
            "   @*************   \n",
            "       TTTTT       \n",
            "       TTTTT       \n"
        ]
        self.assertEqual(content, expected_content, f"Error: Expected tree content does not match. Got: {content}")
        self.createdFiles.append("files_/validFile2.txt")

    @patch('builtins.input', side_effect=['three', 'validFilePath.txt'])
    def test_levels_value_is_non_integer(self, mock_input):
        """
            Test Case: Verify the functionality with non-integer levels value.
        """
        with self.assertRaises(ValueError, msg="Error: Expected ValueError for non-integer levels value, but no exception was raised."):
            self.tree.create_symmetrical_tree()

    @patch('builtins.input', side_effect=['1', 'validFilePath.txt'])
    def test_levels_value_is_less_than_two(self, mock_input):
        """
            Test Case: Verify that ValueError is raised for levels value if it is less than 2.
        """
        with self.assertRaises(ValueError, msg="Error: Expected ValueError for levels if it is less than 2, but no exception was raised."):
            self.tree.create_symmetrical_tree()

    @patch('builtins.input', side_effect=['', 'validFilePath.txt'])
    def test_levels_value_is_empty(self, mock_input):
        """
            Test Case: Verify the functionality with an empty levels value.
        """
        with self.assertRaises(ValueError, msg="Error: Expected ValueError for empty levels value, but no exception was raised."):
            self.tree.create_symmetrical_tree()

    @patch('builtins.input', side_effect=['5', '路径.txt'])
    def test_file_path_value_is_non_latin(self, mock_input):
        """
            Test Case: Verify the functionality with non-Latin letters in file path value.
        """
        with self.assertRaises(ValueError, msg="Error: Expected ValueError for non-Latin file path value, but no exception was raised."):
            self.tree.create_symmetrical_tree()

    @patch('builtins.input', side_effect=['5', ''])
    def test_file_path_value_is_empty(self, mock_input):
        """
            Test Case: Verify the functionality with an empty file path value.
        """
        with self.assertRaises(OSError, msg="Error: Expected OSError for empty file path value, but no exception was raised."):
            self.tree.create_symmetrical_tree()

    @patch('builtins.input', side_effect=['0', 'validFilePath.txt'])
    def test_levels_value_is_zero(self, mock_input):
        """
            Test Case: Verify the functionality with levels value as zero.
        """
        with self.assertRaises(ValueError, msg="Error: Expected ValueError for zero levels, but no exception was raised."):
            self.tree.create_symmetrical_tree()

    @patch('builtins.input', side_effect=['-5', 'validFilePath.txt'])
    def test_levels_value_is_negative(self, mock_input):
        """
            Test Case: Verify the functionality with levels value as a negative number.
        """
        with self.assertRaises(ValueError, msg="Error: Expected ValueError for negative levels value, but no exception was raised."):
            self.tree.create_symmetrical_tree()

    @patch('builtins.input', side_effect=['3  ', 'files_/validFileWithSpaces.txt'])
    def test_levels_value_is_with_spaces(self, mock_input):
        """
            Test Case: Verify the functionality with levels value containing spaces.
        """
        self.tree.create_symmetrical_tree()
        self.assertTrue(os.path.exists('files_/validFileWithSpaces.txt'), "Error: Expected file to be created, but it was not found.")
        with open('files_/validFileWithSpaces.txt', 'r') as file:
            content = file.readlines()
        expected_content = [
            "     W\n",
            "     *\n",
            "   @*****   \n",
            "   TTTTT   \n",
            "   TTTTT   \n"
        ]
        self.assertEqual(content, expected_content, f"Error: Expected tree content does not match. Got: {content}")
        self.createdFiles.append("files_/validFileWithSpaces.txt")

    @patch('builtins.input', side_effect=['0x3', 'validFilePath.txt'])
    def test_levels_value_with_other_number_system(self, mock_input):
        """
            Test Case: Verify the functionality with levels value in other number systems.
        """
        with self.assertRaises(ValueError, msg="Expected ValueError for levels value in other number systems, but no exception was raised."):
            self.tree.create_symmetrical_tree()

    @patch('builtins.input', side_effect=['3', 'files_/@#$%.txt'])
    def test_file_path_value_with_only_allowed_symbols(self, mock_input):
        self.tree.create_symmetrical_tree()
        self.assertTrue(os.path.exists('files_/@#$%.txt'), "Error: Expected file to be created, but it was not found.")
        with open('files_/@#$%.txt', 'r') as file:
            content = file.readlines()
        expected_content = [
            "     W\n",
            "     *\n",
            "   @*****   \n",
            "   TTTTT   \n",
            "   TTTTT   \n"
        ]
        self.assertEqual(content, expected_content, f"Error: Expected tree content does not match. Got: {content}")
        self.createdFiles.append("files_/@#$%.txt")

    @patch('builtins.input', side_effect=['5', '<validFilePath:>.txt'])
    def test_file_path_value_contains_not_allowed_symbols(self, mock_input):
        """
            Test Case: Verify the functionality with file path value containing not allowed symbols.
        """
        with self.assertRaises(ValueError, msg="Error: Expected ValueError for file path value with not allowed symbols, but no exception was raised."):
            self.tree.create_symmetrical_tree()

    @patch('builtins.input', side_effect=['5', 'C::\invalid\path.txt'])
    def test_file_path_value_is_in_invalid_os_syntax(self, mock_input):
        """
            Test Case: Verify the functionality with file path containing invalid OS syntax.
        """
        with self.assertRaises(OSError, msg="Error: Expected OSError for file path with invalid OS syntax, but no exception was raised."):
            self.tree.create_symmetrical_tree()
