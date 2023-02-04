"""
Hash table

@by Vadbeg
"""

from typing import Any, Optional


class HashTable:
    """Simple hash table"""

    def __init__(self, length: int=4):
        self.array = [None] * length

    def __get_hash__(self, key: Any) -> int:
        length = len(self.array)
        hash_num = hash(key) % length

        return hash_num

    def add(self, key: Any, value: Any):
        if self.__is_full__():
            self.__double__()

        hash_num = self.__get_hash__(key)

        if self.array[hash_num] is None:
            self.array[hash_num] = [[key, value]]

        else:
            for kvp in self.array[hash_num]:
                if kvp[0] == key:
                    kvp[1] = value

                    break
            else:
                self.array[hash_num].append([key, value])

    def get(self, key: Any) -> Optional[Any]:
        hash_num = self.__get_hash__(key)

        linked_list = self.array[hash_num]

        if linked_list is not None:

            for kvp in linked_list:
                if kvp[0] == key:
                    return kvp[1]

        return None

    def __is_full__(self):
        is_full_counter = 0

        for linked_list in self.array:
            if linked_list is not None:
                is_full_counter += 1

        if is_full_counter > 0.75 * len(self.array):
            return True

        return False

    def __double__(self):
        double_hash_table = HashTable(length=2*len(self.array))

        for linked_list in self.array:
            if linked_list is not None:
                for items in linked_list:
                    key = items[0]
                    value = items[1]

                    double_hash_table[key] = value

        self.array = double_hash_table.array

    def __getitem__(self, key: Any):
        item = self.get(key=key)

        return item

    def __setitem__(self, key: Any, value: Any):
        self.add(key, value)

    def __len__(self):
        length = 0

        for linked_list in self.array:
            if linked_list is not None:
                length += len(linked_list)

        return length

    def __str__(self):
        res = '{'

        for linked_list in self.array:
            if linked_list is not None:

                for key, value in linked_list:
                    res += str(key) + ': ' + str(value) + ', '

        res += '}'

        return res


if __name__ == '__main__':
    hash_table = HashTable()

    hash_table['orange'] = 45
    hash_table['banana'] = 1
    hash_table['apple'] = 15
    hash_table['cucumber'] = 25
    hash_table['avocado'] = 444
    hash_table['raspberry'] = 12

    print(hash_table['apple'])

    hash_table['banana'] = 17
    print(hash_table['banana'])

    print(hash_table)
    print(f'Hash table length: {len(hash_table)}')



