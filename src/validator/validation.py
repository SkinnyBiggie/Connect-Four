class Validation:
    """
    Class for game validation
    """
    @staticmethod
    def is_name_correct(name):
        """
        Checks if the name is made of letters and valid. If it's invalid it raises a ValidationException
        :param name: the name of the player
        :return: -
        """
        if len(name.strip()) == 0:
            raise Exception("Invalid name! Player name cannot be empty")

        while True:
            if all(char.isalpha() or char.isspace() for char in name):
                break
            else:
                raise Exception("Invalid name! The name can only be made of letters and whitespaces!")

    @staticmethod
    def is_column_valid(number):
        """
        Checks if the column the players picked is valid
        :param column: the column one of the players picked
        :return: True if valid, otherwise false
        """
        if number.isdigit():
            column = int(number)
            if column > 0 and column < 8:
                return True
        return False