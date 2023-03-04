class Computer:
    def __init__(self, disc, human_disc, depth):
        """
        Computer class initializer
        :param disc: The disc used by the computer
        :param human_disc: The disc used by the human opponent
        :param depth: The depth at which the computer will explore the "game tree"
        """
        self.disc = disc
        self.human_disc = human_disc
        self.depth = depth

    @property
    def get_disc(self):
        """
        :return: The disc that the computer is using
        """
        return self.disc

    def __str__(self):
        """
        Function to print the disc color that the computer is using
        :return:
        """
        return "The computer is using {} discs".format(self.disc)