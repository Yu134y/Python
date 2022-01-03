# 論理演算子(logical operators)
# and, or, not

a = 1
b = 1
c = 10
d = 100

print(a == b and c > d)  # False
print(a == b or c > d)  # True
print(not a == b)  # False

# challenge1：年齢が10歳以上かつ身長が110㎝以上なら乗れるアトラクション
age = 22
height = 180
print(age >= 10 and height >= 110)

# challenge2：修士号保持もしくは5年以上実務経験があればVisaの取得が可能
master = False
job_experience = 0
print(master or job_experience >= 5)