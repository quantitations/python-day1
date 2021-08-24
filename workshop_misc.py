
tao = """The tao that can be described is not the eternal Tao. The name that can be spoken is not the eternal Name.
The nameless is the boundary of Heaven and Earth. The named is the mother of creation.
Freed from desire, you can see the hidden mystery. By having desire, you can only see what is visibly real.
Yet mystery and reality emerge from the same source. This source is called darkness."""


##############################################################


class Card:
    
    def __init__(self, rank, suit):
        if not rank in list(range(2, 15)):
            raise Exception("Invalid 'rank' provided")
        if not suit in ["spades", "hearts", "clubs", "diamonds"]:
            raise Exception("Invalid 'suit' provided")
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        rank = self.rank
        if rank == 11:
            rank = "jack"
        elif rank == 12:
            rank = "queen"
        elif rank == 13:
            rank = "king"
        elif rank == 14:
            rank = "ace"
        return "%s of %s" % (rank, self.suit)
        
    def war(self, other):
        if self.rank > other.rank:
            print("I win")
        elif self.rank < other.rank:
            print("You win")
        else:
            if self.suitNumber() > other.suitNumber():
                print("I win")
            elif self.suitNumber() < other.suitNumber():
                print("You win")
            else:
                print("It's a tie")
            
    def suitNumber(self):
        if self.suit == "spades":
            return 4
        if self.suit == "hearts":
            return 3
        if self.suit == "clubs":
            return 2
        if self.suit == "diamonds":
            return 1
