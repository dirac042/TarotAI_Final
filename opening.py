class OpeningMessage:
    """
    Class imported by main.py,
    executed right after the start of the execution of main.py
    message display, and importing cards.csv
    """

    def __init__(self, filename="TarotAI/BeforetheExecution.txt"):
        """
        defining the filename that will be used.
        """
        self.__filename = filename

    def open_file(self):
        """
        open the file that is defined in __init__
        return the content to the variable 'msg'
        """
        try:
            with open(self.__filename, "r", encoding="utf-8") as opening_message:
                msg = opening_message.read()
                return msg
        except FileNotFoundError:
            return "File not found"
        except UnicodeDecodeError:
            return "File not in UTF-8 format"
        except Exception as e:
            return f"Error: {str(e)}"

    def close_file(self):
        """
        verifying that the file is closed
        """
        open(self.__filename, "r").close()
