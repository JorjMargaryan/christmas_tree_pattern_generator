from common_.utilities_.customLogger import logger
import re


class ChristmasTree:
    def __init__(self):
        self.levels = None
        self.filePath = None

    def __inputs_validation(self):
        """
            Validates the input values for levels and file path.
        """
        import os
        if self.levels is None:
            try:
                levelsInput = input("Enter the number of levels for the tree: ").strip()

                if not levelsInput:
                    raise ValueError("The input value of levels cannot be empty.")

                if levelsInput.isdigit():
                    self.levels = int(levelsInput)
                else:
                    raise ValueError(f"Levels input must be a valid decimal integer, but got {levelsInput}")

                if self.levels < 2:
                    raise ValueError(f"The number of levels must be at least 2, but got {self.levels}")
            except ValueError as e:
                logger("ERROR", f"Invalid input value for levels: {e}")
                raise

        if self.filePath is None:
            try:
                self.filePath = input("Enter the path to the output file: ").strip()

                if not self.filePath:
                    raise OSError("The input value of file path cannot be empty.")

                if not isinstance(self.filePath, str):
                    self.filePath = str(self.filePath)

                # Check if the file path includes a directory
                directory = os.path.dirname(self.filePath)
                if directory and not os.path.isdir(directory):
                    try:
                        os.makedirs(directory, exist_ok=True)
                    except OSError:
                        logger("ERROR",
                               f"Failed to create directory for file path. Given value is '{self.filePath}'")
                        raise

                # List of invalid characters for filenames
                invalidChars = '<>:"\\|?*'

                # Validate the file path
                if any(c in invalidChars for c in os.path.basename(self.filePath)):
                    raise ValueError(f"The file path contains invalid characters. Given value is '{self.filePath}'")

                latinRegex = re.compile(r'^[a-zA-Z0-9._\-/@#$%^&()+=!]+$')
                if not latinRegex.match(self.filePath):
                    raise ValueError(f"The file path contains non-Latin characters. Given value is '{self.filePath}'")

            except (ValueError, TypeError, OSError) as e:
                logger("ERROR", f"Invalid input value for file path: {e}")
                raise

        return True

    def create_symmetrical_tree(self):
        """
            Creates a symmetrical tree pattern with a specified number of levels
            and saves it to a file specified by the file_path parameter.
        """
        if not self.__inputs_validation():
            return

        christmasTree = []
        max_width = 2 * (self.levels * 2) - 1

        christmasTree.append(" " * (max_width // 2) + "W")
        christmasTree.append(" " * (max_width // 2) + "*")

        for i in range(1, self.levels - 1):
            stars = "*" * (2 * (i * 2) + 1)
            padding = " " * (self.levels * 2 - i * 2 - 1)
            if i % 2 == 1:
                christmasTree.append(padding + "@" + stars + padding)
            else:
                christmasTree.append(padding + stars + "@" + padding)

        treeTrunkPadding = " " * ((max_width - 5) // 2)
        treeTrunk = treeTrunkPadding + "TTTTT" + treeTrunkPadding
        christmasTree.append(treeTrunk)
        christmasTree.append(treeTrunk)

        try:
            with open(self.filePath, 'w') as file:
                for line in christmasTree:
                    file.write(line + '\n')
            logger("INFO", f"Tree created successfully and saved to {self.filePath}")
        except IOError:
            errorMessage = f"Error writing to file. File path - {self.filePath}"
            logger("ERROR", errorMessage)
            raise IOError(errorMessage)


if __name__ == '__main__':
    tree = ChristmasTree()
    tree.create_symmetrical_tree()
