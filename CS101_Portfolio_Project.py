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
        self.card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
                            'Queen': 10, 'King': 10, 'Ace': 11}
        self.gen_deck = []
        for suit in self.suits:
            for number in self.numbers:
                self.gen_deck.append(f'The {number} of {suit}')


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.bet_amount = 0
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
            if self.player_card_score + 11 > 21:
                score = 1
            else:
                score = 11
            self.player_card_score += score

        else:
            score = 10
            self.player_card_score += score

        print(f'{self.name}\'s card score is: {score}\n {self.name}\'s total card score is: {self.player_card_score}')

    def place_a_bet(self, amount):
        self.balance -= amount

    def win(self, amount):
        self.balance += amount


class Dealer(Player):

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
play_flag = True
while play_flag == True:
    player_1.player_card_score = 0
    dealer.player_card_score = 0
    bet_amount = (int(input(f'Your balance is {player_1.balance}\nHow much would you like to bet?\n')))
    player_1.place_a_bet(bet_amount)

    player_1.choose_a_card(deck.gen_deck)
    input('hit enter to continue')
    dealer.choose_a_card(deck.gen_deck)
    input('hit enter to continue')
    player_1.choose_a_card(deck.gen_deck)
    input('hit enter to continue')
    dealer.hidden_card(deck.gen_deck)

    flag = True
    action = ''

    while player_1.player_card_score < 21 and dealer.player_card_score < 21 and flag == True:
        action = input('Select from the following Actions:\n'
                       'Hit, Stand, Double down, Split, Surrender\n')
        if action == 'Hit':
            player_1.choose_a_card(deck.gen_deck)
            if dealer.player_card_score < 17:
                dealer.hidden_card(deck.gen_deck)
        elif action == 'Stand':
            flag = False
        elif action == 'Double Down':
            player_1.place_a_bet(player_1.bet_amount)
            print(f'You Doubled your bet to: {player_1.bet_amount}')
        elif action == 'Split':
            pass
        elif action == 'Surrender':
            pass
        else:
            print('Please make a valid selection.')


    def who_won(P1_score, D_Score, action):
        if P1_score > 21:
            print(f'You lose {bet_amount} dollars')
        elif action == 'Surrender':
            print(f'You lose {player_1.bet_amount} dollars')
        elif P1_score == 21:
            print(f'BlackJack, You Win! {bet_amount * 2} dollars')
            player_1.win(bet_amount * 2)
        elif P1_score > D_Score:
            print(f'You beat the dealer, You Win! {bet_amount * 2} dollars')
            player_1.win(bet_amount * 2)
        elif P1_score == D_Score:
            print(f'Tie game - you keep {bet_amount} dollars')
            player_1.win(bet_amount)
        elif P1_score < D_Score:
            print(f'You lose {bet_amount} dollars')


    who_won(player_1.player_card_score, dealer.player_card_score, action)
    print(f'the score was {player_1.player_card_score} to {dealer.player_card_score}')
    print([player_1.balance])
    if input('would you like to play again Y or N?') == 'Y' and player_1.balance > 0:
        play_flag = True
    else:
        print(f'you exited the game and your balance is: {player_1.balance}')
