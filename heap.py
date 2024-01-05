class Queue_heap:
    def __init__(self):
        self.qq = []
        self.size = 0
    # Функция сортирует дерево
    def heapify(self, n, i):
        # Находим самое большое значение среди
        # корневого, правого и левого дочернего элемента
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.qq[i] < self.qq[l]:
            largest = l

        if r < n and self.qq[largest] < self.qq[r]:
            largest = r

        # Меняем местами и продолжаем сортировку,
        # если значение корневого элемента не самое большое
        if largest != i:
            self.qq[i], self.qq[largest] = self.qq[largest], self.qq[i]
            self.heapify(n, largest)


    # Функция вставляет элемент
    def insert(self, newNum):
        self.size = len(self.qq)
        if self.size == 0:
            self.qq.append(newNum)
        else:
            self.qq.append(newNum)
            for i in range((len(self.qq) // 2) - 1, -1, -1):
                self.heapify(len(self.qq), i)


    # Функция удаляет элемент
    def extractMax(self):
        size = len(self.qq)
        print('size: ' + str(self.size))
        self.qq[0], self.qq[self.size] = self.qq[self.size], self.qq[0]

        print('максимальный элемент: '+ str(self.qq.pop()))

        for i in range((len(self.qq) // 2) - 1, -1, -1):
            self.heapify(len(self.qq), i)

    def increase(self, x, p):
        size = len(self.qq)
        print('size: '+ str(self.size))
        i = 0
        for i in range(0, self.size):
            if x == self.qq[i]:
                break
        self.qq[i] = p
        for i in range((len(self.qq) // 2) - 1, -1, -1):
            self.heapify(len(self.qq), i)

def test1():
    arr = Queue_heap()
    arr.insert(3)
    arr.insert(4)
    arr.insert(9)
    arr.insert(5)
    arr.insert(2)
    arr.insert(8)

    print ("Массив max-кучи: " + str(arr.qq))

    arr.extractMax()
    print("После удаления элемента: " + str(arr.qq))

    arr.increase(3, 6)
    print('После замены: '+str(arr.qq))


test1()
