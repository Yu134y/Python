# 例外(Exception)を自作する
# ・Exceptionクラスを継承する(BaseExceptionは継承されることを意図されていないので注意)
# ・○○Errorという名前にするとわかりやすい(もしその例外がエラーなら)
# ・自作の例外はなるべく別ファイルにまとめておく(exceptions.pyとかerrors.pyなど)

class MyError(Exception):

    def __str__(self):
        return 'my error occurred'


if __name__ == '__main__':
    response = input('y/n?')
    try:
        if response != 'y' and response != 'n':
            raise MyError
    except MyError as e:
        print(e)  # e.__str__()
