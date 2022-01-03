class MyErrow(Exception):

    def __str__(self):
        return 'my srror occurred'


if __name__ == '__main__':
    response = input('y/n?')
    try:
        if response != 'y' and response != 'n':
            raise MyErrow('my error occurred')
    except MyErrow as e:
        print(e)  # e.__str__()