# カプセル化（encapsulation）：外からアクセスできないようにする（情報隠蔽）

def casino_entrance(age, min_age=21):
    if age < min_age:
        print(f'{min_age}歳未満お断り')
        return

    def inner_casino_entrance():
        print('ようこそカジノへ')

    return inner_casino_entrance()


casino_entrance(19)