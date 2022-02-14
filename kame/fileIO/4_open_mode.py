# mode='a'(append)：ファイルの最後尾に内容を追加
with open('writing_file.txt', mode='a') as f:
    f.write('mode=a appends text')

# mode='r+'：読み書きどちらも可能
with open('writing_file.txt', mode='r+') as f:
    f.write('You can write and read with r+ mode!!')
    print((f.read()))
    f.write('This should be the last sentence.')
    print(f.read())

# mode='w+'：読み書きどちらも可能。Truncate（ファイルの中身削除）されることに注意
with open('writing_file.txt', mode='w+') as f:
    print(f.read())
    f.write('You can write and read with w+ mode!!')
    f.seek(0)  # positionを先頭にする
    print(f.read())

# mode='a+'：読み書きどちらも可能で、positionが最後尾から始まる
with open('writing_file.txt', mode='a+') as f:
    print(f.read())
    f.write('\nYou add sentences to the last of the file')
    f.seek(0)
    print(f.read())
