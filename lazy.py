class Queue_list:

    def __init__(self):
        self.qq = []
        self.size = 0

    def insert(self, x):
        self.qq.append(x)
        self.size += 1

    def extractMax(self):
        max = self.qq[0]
        pos = 0
        for i in range(len(self.qq)):
            if self.qq[i] > max:
                max = self.qq[i]
                pos = i
        print('максимальный элемент: ' + str(self.qq.pop(pos)))
# функция рор пробегает ао массиву, находит элемент, удаляет его и сдвигает все остальныеэлементы на 1 позицию
# для оптимизации можно мначала переместить элемент в конецЮ а только потом его удалить

        self.size -= 1

    def increase(self, x, p):
        for i in range(self.size):
            if x == i:
                self.qq[i] = p



def test1():
    arr = Queue_list()
    arr.insert(3)
    arr.insert(4)
    arr.insert(9)
    arr.insert(5)
    arr.insert(2)
    arr.insert(8)

    print("Массив max-кучи: " + str(arr.qq))

    arr.extractMax()
    print("После удаления элемента: " + str(arr.qq))
    arr.extractMax()
    print("После удаления элемента: " + str(arr.qq))

    arr.increase(3, 6)
    print('После замены: ' + str(arr.qq))

test1()