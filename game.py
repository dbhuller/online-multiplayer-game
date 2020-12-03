class Game:
    def __init__(self, id):
        # Player 1 & Player 2 made move
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        # List of moves for [p1, p2]
        self.moves = [None, None]
        # List of wins for [p1, p2]
        self.wins = [0, 0]
        self.ties = 0

    def get_player_move(self, p):
        """
        0 --> p1
        1 --> p2
        :param p: [0, 1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def both_went(self):
        return self.p1Went and self.p2Went

    def winner(self):
        # Get first letter of move made by player (ie: R -> Rock)
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1
        
        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
            
    


