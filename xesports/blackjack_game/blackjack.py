import random
import time

# トランプを作る: 得点を数えられるように数字
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4


# トランプを２枚配る: 絵札(J,Q,K)で表示させる
def deal():
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = 'J'
        if card == 12:
            card = 'Q'
        if card == 13:
            card = 'K'
        if card == 1:
            card = 'A'
        hand.append(card)
    return hand


# ヒットの場合 hand を追加する
def hit(hand):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:
        card = 'J'
    if card == 12:
        card = 'Q'
    if card == 13:
        card = 'K'
    if card == 1:
        card = 'A'
    hand.append(card)
    return hand


# プレイヤーの合計を求める
def total(hand):
    score = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            score += 10
        elif card == 'A':
            if score >= 11:
                score += 1
            else:
                score += 11
        else:
            score += card
    return score


# もう１度プレイするか確認する
def play_again():
    again = input('もう一度プレイしますか？ (Y/N): ').lower()
    if again == 'y':
        game()
    elif again == 'n':
        print('お疲れ様でした！また遊びましょう！')
        exit()
    else:
        print('Y or N を入力してください。')
        play_again()


def result(dealer_hand, player_hand):
    if total(player_hand) > total(dealer_hand):
        print(f'\nディーラーの合計は {total(dealer_hand)} です。あなたの合計は {total(player_hand)} です。\033[34mYOU WIN!!!\033[39m')
    elif total(player_hand) < total(dealer_hand):
        print(f'\nディーラーの合計は {total(dealer_hand)} です。あなたの合計は {total(player_hand)} です。\033[31mYOU LOSE...\033[39m')
    else:
        print(f'\nディーラーの合計は {total(dealer_hand)} です。あなたの合計は {total(player_hand)} です。\033[33mDRAW\033[39m')


# 実際にプレーする
def game():
    dealer_hand = deal()
    player_hand = deal()
    print(f'ディーラーのカードは {dealer_hand[0]} です。')
    time.sleep(2)
    print(f'プレイヤーのカードは {player_hand} です。合計は {total(player_hand)} です。')
    if total(player_hand) == 21:
        time.sleep(1)
        print(f'BlackJack!!! \033[34mYOU WIN!!!\033[39m')
        play_again()

    choice = ''

    while choice != quit:
        choice = input('ヒットしますか？　スタンドしますか？ (HIT/STAND): ').lower()
        if choice == 'hit':
            print('カードを配っています...')
            hit(player_hand)
            time.sleep(2)
            print(f'\nあなたに {player_hand[-1]} が配られました。現在のカードは {player_hand} です。合計は {total(player_hand)} です')
            if total(player_hand) == 21:
                print(f'BlackJack!!! \033[34mYOU WIN!!!\033[39m')
                choice = quit
                play_again()
            elif total(player_hand) > 21:
                print('あなたは 21 を超えてしまいました。\033[31mYOU LOSE...\033[39m')
                choice = quit
                play_again()
        elif choice == 'stand':
            print('ディーラーの2枚目のカードをオープンします...')
            time.sleep(2)
            print(f'\nディーラーの2枚目のカードは {dealer_hand[1]} です。合計は {total(dealer_hand)} です。')
            while total(dealer_hand) < 17:
                print('ディーラーがカードを引いています...')
                time.sleep(3)
                hit(dealer_hand)
                print(f'ディーラーに{dealer_hand[-1]} が配られました。現在のカードは {dealer_hand} です。合計は {total(dealer_hand)} です')
                if total(dealer_hand) > 21:
                    time.sleep(2)
                    print('ディーラーは21を超えてしまいました。\033[34mYOU WIN!!!\033[39m')
                    choice = quit
                    play_again()
            if total(dealer_hand) <= 21:
                print('結果は...')
                time.sleep(2)
                result(dealer_hand, player_hand)
                choice = quit
                play_again()
        else:
            print('HIT or STAND で入力してください。')


game()
