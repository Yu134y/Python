# challenge：CarクラスとCarオブジェクトのインスタンスを作ろう
# Carクラスの属性：model_name, mileage, manufacture
# Carクラスのメソッド：gas(), breakes() （いくつかの属性をプリントする）

class Car(object):

    def __init__(self, model_name, mileage, manufacture):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacture = manufacture

    def gas(self):
        # print(f'{self.manufacture}の{self.model_name} (燃費：{self.mileage}km/L), アクセル全開!!')
        print('{0.manufacture}の{0.model_name} (燃費：{0.mileage}km/L), アクセル全開!!'.format(self))

    def brakes(self):
        print('{0.manufacture}の{0.model_name} (燃費：{0.mileage}km/L), ブレーキ!!'.format(self))


if __name__ == '__main__':
    prius = Car('Prius', 20, 'TOYOTA')
    conti_gt = Car('Bentley Continental GT', 4, 'Bentley')
    print(prius.model_name)
    print(prius.mileage)
    print(prius.manufacture)
    prius.gas()
    prius.brakes()
    conti_gt.gas()
