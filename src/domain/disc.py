from termcolor import colored


class Disc:
    def __init__(self, color):
        """
        Disc class initializer
        :param color: The color of the disc
        """
        self.color = color

    @property
    def get_color(self):
        """
        Getter for the color attribute
        """
        return self.color

    def __str__(self):
        """
        Function for printing a disc of the specified color
        :return: The colored disc
        """
        return colored('#', str(self.color))