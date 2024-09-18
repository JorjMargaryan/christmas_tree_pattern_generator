SUCCESS = 0
GENERAL_ERROR = 1
UNEXPECTED_BEHAVIOR = 2
FILE_NOT_FOUND = 3
LOGGING_ERROR = 4
FILE_NAME_GENERATION_ERROR = 5
REPORT_CREATION_ERROR = 6

MessageCodes = {
    0: "The automation tests ran successfully without any errors.",
    1: "General error occurred during test execution. This code is used for unspecified errors.",
    2: "Unexpected application behavior error. This code is used when the application behaves unexpectedly, indicating a potential bug.",
    3: "File not found error. This code is used when a required file is not found.",
    4: "Logging error. This code is used when An error occurred while logging (creating a log file).",
    5: "File Name generation error. This code is used when an error occurred while generating the html or xml report file name.",
    6: "Report creation error. This code is used when an error occurred while creating html or xml report file.",
}
