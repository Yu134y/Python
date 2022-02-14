with open('writing_file.txt', mode='w') as f:
    # truncatedされる：byte=0に切り詰める(実行するたびに中身が削除される)
    f.write('You can write contents here\nuse "backslash" to break the row')
    f.write("new write() doesn't break row")

    print('You can add a new row using "file" parameter', file=f)
    print('new print() method breaks the row for you!', file=f)
    # print(f.read())  # read()はできない
