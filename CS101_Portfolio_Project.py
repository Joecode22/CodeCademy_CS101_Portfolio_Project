"""

Welcome to the portfolio project in CS 101: Introduction to Programming!

In this portfolio project, you will research, brainstorm, and build a basic terminal program of your choice for your
friends and family to play with. After you finish building the program, you will create a blog post to share the
program on a publication of your choice!


"""
import random


class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        self.gen_deck = []
        for suit in self.suits:
            for number in self.numbers:
                self.gen_deck.append(f'The {number} of {suit}')


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.balance = 100
        self.player_card_score = 0

    def choose_a_card(self, deck):
        choice = random.choice(deck)
        deck.remove(choice)
        self.cards.append(choice)
        print(f'The dealer dealt {self.name}:\n {choice}')
        split = choice.split()
        if split[1].isnumeric():
            score = int(split[1])
            self.player_card_score += score

        elif split[1] == 'Ace':
            score = 11
            self.player_card_score += score

        else:
            score = 10
            self.player_card_score += score


        print(f'{self.name}\'s card score is: {score}\n {self.name}\'s total card score is: {self.player_card_score}')

    def place_a_bet(self, amount):
        self.balance -= amount



class Dealer(Player):
    def choose_a_card(self, deck):
        choice = random.choice(deck)
        deck.remove(choice)
        self.cards.append(choice)
        print(f'The dealer dealt {self.name}:\n {choice}')
        split = choice.split()
        if split[1].isnumeric():
            score = int(split[1])
            self.player_card_score += score

        elif split[1] == 'Ace':
            score = 11
            self.player_card_score += score

        else:
            score = 10
            self.player_card_score += score


        print(f'{self.name}\'s card score is: {score}\n {self.name}\'s total card score is: {self.player_card_score}')

class Dealer(Player):

    def __init__(self, name):
        super().__init__(name)


    def hidden_card(self, deck):
        choice = random.choice(deck)
        deck.remove(choice)
        self.cards.append(choice)
        print(f'The dealer dealt a hidden card')
        split = choice.split()
        if split[1].isnumeric():
            score = int(split[1])
            self.player_card_score += score

        elif split[1] == 'Ace':
            score = 11
            self.player_card_score += score

        else:
            score = 10
            self.player_card_score += score



deck = Deck()
dealer = Dealer('Dealer')
player_1 = Player(input('What is your name?\n'))
player_1.place_a_bet(int(input(f'Your balance is {player_1.balance}\nHow much would you like to bet?\n')))

player_1.choose_a_card(deck.gen_deck)
dealer.choose_a_card(deck.gen_deck)
player_1.choose_a_card(deck.gen_deck)
dealer.hidden_card(deck.gen_deck)

action = input('Select from the following Actions:\n'
               'Hit, Stand, Double down, Split, Surrender\n')

if action == 'Hit':
    player_1.choose_a_card(deck.gen_deck)
elif action == 'Stand':
    flag = False
elif action == 'Double Down':
    pass
elif action == 'Split':
    pass
elif action == 'Surrender':
    pass
else:
    print('Please make a valid selection.')