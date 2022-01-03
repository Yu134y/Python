# challenge：Carクラスを継承するTruckクラスを作ってみよう
# Carクラスの属性に加えて、最大積載量と現在の積載量の情報を持つようにする
# load()メソッドで、指定した重荷の重さを積んだり降ろせたりできるようにする（積載量がマイナスにならないように注意する）
# 積載量をオーバーしたらその旨をprint()するが積むことは可能にする

# 自分で考えたやつ

from car import Car


# class Truck(Car):
#
#     def __init__(self, model_name, mileage, manufacture, max_capacity, now_capacity):
#         super().__init__(model_name, mileage, manufacture)
#         self.max_capacity = max_capacity
#         self.now_capacity = now_capacity
#
#     def stack_load(self, weight):
#         self.now_capacity += weight
#         if self.now_capacity <= self.max_capacity:
#             self.show_capacity()
#         else:
#             self.show_capacity()
#             self.over_capacity()
#
#     def take_load(self, weight):
#         self.now_capacity -= weight
#         if self.now_capacity < 0:
#             print('その量は取り出せません')
#         elif self.now_capacity <= self.max_capacity:
#             self.show_capacity()
#         else:
#             self.show_capacity()
#             self.over_capacity()
#
#     def show_capacity(self):
#         print('{0.model_name}の現在の積載量は{0.now_capacity}kgです'.format(self))
#
#     def over_capacity(self):
#         print(f'最大積載量({self.max_capacity}kg)をオーバーしています')
#
#
#
#
#
# prius = Truck('Prius', 20, 'TOYOTA', 2000, 1000)
# prius.stack_load(20000)
# prius.take_load(10000)

# 正解


class Truck(Car):
    def __init__(self, model_name, mileage, manufacture, max_loading):
        super().__init__(model_name, mileage, manufacture)
        self._max_loading = max_loading
        self._loadings = 0

    def gas(self):
        if self._loadings > self._max_loading:
            print('重量オーバーなので走れません')
            print(f'最低でも{self._loadings - self._max_loading}tの荷物を降ろしてください')
        else:
            super().gas()

    def load(self, weight):
        if weight > 0:
            print(f'{weight}tの荷物を積みました')
            self._loadings += weight
        else:
            if self._loadings <= -weight:
                print(f'{self._loadings}t全ての荷物を降ろしました')
                self._loadings = 0
            else:
                print(f'{-weight}tの荷物を降ろしました')
                # weightは負の値なので、+=で足し算をする
                self._loadings += weight
        print(f'現在の積載量は{self._loadings}tです')

        if self._loadings > self._max_loading:
            print(f'{self.model_name}の最大積載量は{self._max_loading}tです。重量オーバーです')


if __name__ == '__main__':
    isuzu_truck = Truck('トラックA', 6, 'いすゞ', 10)
    isuzu_truck.gas()
    isuzu_truck.load(5)
    isuzu_truck.load(-3)
    isuzu_truck.load(10)
    isuzu_truck.gas()
    isuzu_truck.load(-30)
