class FourDigityearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return f'{value:04}'  # 0埋め4桁の数字としてvalueをフォーマットする
