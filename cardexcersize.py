class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_name(self):
        return self.suit + str(self.rank)


class Stack:
    def __init__(self):
        self.cards = []

    def get_cards(self):
        s = self.cards[0].get_name()
        for c in self.cards[1:]:
            s += ", " + c.get_name()
        return s

    def get_size(self):
        return len(self.cards)

    def add(self, card):
        self.cards.append(card)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
        else:
            print("Cannot remove card, not found!")

    def remove_top(self):
        if len(self.cards) > 0:
            self.cards.pop(0)
        else:
            print("Cannot remove card, stack is empty")

    def sort_suit(self):
        n = len(self.cards)
        is_swapped = True
        while is_swapped:
            is_swapped = False
            for i in range(n - 1):
                c1 = self.cards[i]
                c2 = self.cards[i + 1]
                if c1.get_suit() > c2.get_suit():
                    self.cards[i], self.cards[i + 1] = self.cards[i + 1], self.cards[i]
                    is_swapped = True

    def sort_rank(self):
        n = len(self.cards)
        is_swapped = True
        while is_swapped:
            is_swapped = False
            for i in range(n - 1):
                c1 = self.cards[i]
                c2 = self.cards[i + 1]
                if c1.get_rank() > c2.get_rank():
                    self.cards[i], self.cards[i + 1] = self.cards[i + 1], self.cards[i]
                    is_swapped = True

    def sort(self):
        self.sort_suit()
        self.sort_rank()


# Example usage:
card1 = Card("Hearts", 10)
card2 = Card("Diamonds", 7)
card3 = Card("Clubs", 2)

stack = Stack()
stack.add(card1)
stack.add(card2)
stack.add(card3)

print("Original Stack:", stack.get_cards())

stack.sort()

print("Sorted Stack:", stack.get_cards())
