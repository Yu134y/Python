# if文のNoneの取り扱い

a = None

# if a is None:
#     print('a is None!!')
# else:
#     print('a has value!!')

if a:  # aはNoneの場合Falseになる
    print('a has value!!')
else:
    print('a is None!!')

if not a:  # aはNoneの場合Trueになる
    print('a is None!!')
    a = 10
    print(a)
