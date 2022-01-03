def func(first, second, third):
    print(f'first: {first}, second: {second}, third: {third}')


# argument（引数に渡す値のこと） <-> parameter（引数のプレースホルダのこと）
func('1', '2', '3')

func('1', third='3', second='2')