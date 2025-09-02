class Car:
    def __init__(self, gas=10, capacity=50, gas_per_100km=10, mileage=50):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_100km = gas_per_100km
        self.mileage = mileage

    def fill(self, liters):
        """Заправить авто N-liters"""
        self.gas += liters
        if self.gas > self.capacity:
            diff = self.gas - self.capacity
            self.gas -= diff
            print(f'Превышен лимит объема бака, возвращено {diff} литров')

    def ride(self, mileage):
        """Проехать на авто N-km"""
        total_distance = self.gas_per_100km * self.gas
        if mileage > total_distance:
            self.mileage += total_distance
            self.gas -= total_distance / self.gas_per_100km
            print(
                f'Максимальное расстояние, которые вы проедите - {total_distance}')
        else:
            self.mileage += mileage
            self.gas -= mileage / self.gas_per_100km

    def car_info(self):
        print(f'Остаток бензина = {self.gas}л., пробег = {self.mileage}км.')


car1 = Car()
car1.fill(5)
car1.ride(25)
car1.car_info()
