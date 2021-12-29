"""

Welcome to the portfolio project in CS 101: Introduction to Programming!

In this portfolio project, you will research, brainstorm, and build a basic terminal program of your choice for your
friends and family to play with. After you finish building the program, you will create a blog post to share the
program on a publication of your choice!


"""
import random


class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10,
                   'King': 10, 'Ace': 11}

    def __init__(self):
        self.gen_deck = []
        for suit in Deck.suits:
            for number in Deck.numbers:
                self.gen_deck.append(f'The {number} of {suit}')


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.balance = 100

    def choose_a_card(self, deck):
        choice = random.choice(deck)
        deck.remove(choice)
        self.cards.append(choice)
        print(f'The dealer dealt {self.name}:\n {choice}')

    def place_a_bet(self, amount):
        self.balance -= amount


deck = Deck()
