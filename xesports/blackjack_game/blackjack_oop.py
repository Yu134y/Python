import random
from time import sleep


# トランプ (suit=柄, number=数字)
class Card:

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return f'{self.suit} {self.number}'


# デッキ (deal=カードを配る, shuffle)
class Deck:

    def __init__(self):
        suits = ['♠', '♥', '♣', '♦']
        numbers = [
            {'key': 'A', 'value': 11},
            {'key': '2', 'value': 2},
            {'key': '3', 'value': 3},
            {'key': '4', 'value': 4},
            {'key': '5', 'value': 5},
            {'key': '6', 'value': 6},
            {'key': '7', 'value': 7},
            {'key': '8', 'value': 8},
            {'key': '9', 'value': 9},
            {'key': '10', 'value': 10},
            {'key': 'J', 'value': 10},
            {'key': 'Q', 'value': 10},
            {'key': 'K', 'value': 10},
        ]

        self.cards = []

        for suit in suits:
            for number in numbers:
                self.cards.append(Card(suit, number))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)


# 手札
class Hand:

    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0
        self.total = 0

    def add_card(self, card):
        self.cards.append(card)

    def calc_value(self):
        self.value = 0
        ace = False
        for card in self.cards:
            self.value += int(card.number['value'])
            if card.number['key'] == 'A':
                ace = True

        if ace and self.value > 21:
            self.value -= 10

        return self.value

    def is_blackjack(self):
        return self.calc_value() == 21

    def show(self, show_two_cards=False):
        print(f"{'Dealer' if self.dealer else 'Your'} hand:")  # <Trueの時に返す値> if <条件> else <Falseのときに返す値>

        sleep(1)
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_two_cards and not self.is_blackjack():
                pass
            else:
                print(f"{card.suit} {card.number['key']}")
        if not self.dealer:
            print('Total: ', self.calc_value())
            sleep(1)
        print()


# ゲーム
class Game:

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.calc_value() > 21:
                sleep(1)
                print('あなたは21を超えました. \033[31mYOU LOSE...\033[39m')
                return True
            elif dealer_hand.calc_value() > 21:
                sleep(1)
                print('ディーラーは21を超えました. \033[34mYOU WIN!!!\033[39m')
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                sleep(1)
                print('ふたりともブラックジャックです. \033[33mDRAW\033[39m')
                return True
            elif player_hand.is_blackjack():
                sleep(1)
                print('あなたはブラックジャックです! \033[34mYOU WIN!!!\033[39m')
                return True
            elif dealer_hand.is_blackjack():
                sleep(1)
                print('ディーラーはブラックジャックです! \033[31mYOU LOSE...\033[39m')
                return True
        else:
            if player_hand.calc_value() > dealer_hand.calc_value():
                print('\033[34mYOU WIN!!!\033[39m')
            elif player_hand.calc_value() == dealer_hand.calc_value():
                print('\033[33mDRAW\033[39m')
            else:
                print('\033[31mYOU LOSE...\033[39m')
            return True
        return False

    def play(self):
        game_to_play = 0
        game_number = 0

        while game_to_play <= 0:
            try:
                game_to_play = int(input('何回ゲームをプレーしますか？'))
            except ValueError:
                print('数字で入力してください。')

        while game_number < game_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())

            print()
            sleep(1)
            print(f'ゲームの回数 {game_number}/{game_to_play}')
            sleep(1)
            print()

            player_hand.show()
            dealer_hand.show()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ''
            while choice not in ['s', 'stand'] and player_hand.calc_value() < 21:
                choice = input('Hit or Stand をしてください。(H/S): ').lower()
                print()
                while choice not in ['h', 's', 'hit', 'stand']:
                    choice = input('Hit or Stand をしてください。(H/S): ').lower()
                    print()
                if choice in ['hit', 'h']:
                    player_hand.add_card(deck.deal())
                    player_hand.show()

            if self.check_winner(player_hand, dealer_hand):
                continue

            if dealer_hand.calc_value() >= 17:
                dealer_hand.calc_value()
                sleep(1)
                dealer_hand.show(show_two_cards=True)

            while dealer_hand.calc_value() < 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand.calc_value()
                sleep(1)
                dealer_hand.show(show_two_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            sleep(1)
            print('結果発表')
            print(f'Your hand: {player_hand.calc_value()}')
            print(f'Dealer hand: {dealer_hand.calc_value()}')

            self.check_winner(player_hand, dealer_hand, game_over=True)


Game().play()
