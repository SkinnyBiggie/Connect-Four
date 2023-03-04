class Board:

    def __init__(self):
        """
        Board class initializer
        We use a matrix to keep track of added discs
        """
        self.matrix = [['#' for x in range(7)] for y in range(6)]

    def __str__(self):
        """
        :return: The matrix declared before but as a "board"
        """
        format = ' | 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n'
        format += ' - - - - - - - - - - - - - - -\n'
        for i in range(6):
            for j in range(7):
                format += ' | '
                format += str(self.matrix[i][j])
            format += ' | \n'
            format += ' - - - - - - - - - - - - - - -\n'
            
        return format