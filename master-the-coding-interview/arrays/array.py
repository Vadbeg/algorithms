"""Array datastructure implementation in Python"""


class Array:
    def __init__(self):
        self._length = 0
        self._data = []

    def append(self, item):
        self._data.append(item)
        self._length += 1

    def __getitem__(self, item: int):
        value = self._data[item]

        return value

    def __len__(self):
        return self._length

    def __str__(self):
        return str(self._data)


if __name__ == '__main__':
    array = Array()

    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    array.append(5)

    print(array)
    print(array[0])
    print(len(array))
