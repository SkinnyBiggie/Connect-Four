class Player:
    def __init__(self, name, disc):
        """
        Player class initializer
        :param name: player's name
        :param disc: player's disc
        """
        self.__name = name
        self.__disc = disc


    @property
    def get_name(self):
        """
        :return: the player's name
        """
        return self.__name

    @property
    def get_disc(self):
        """
        :return: the disc that the player uses
        """
        return self.__disc

    def __str__(self):
        """
        Function to tell us the color that a player is using
        :return: a string with the player's name and the color he's using
        """
        return "Player {} is using {} discs.".format(self.__name, self.__disc)