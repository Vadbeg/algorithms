"""Module with BoomFilter realization"""

import math
from typing import Any
from random import shuffle

import mmh3
from bitarray import bitarray


class BloomFilter:

    def __init__(self, items_count, fp_prob):
        """

        :param items_count: number of items to be stored in bloom filter
        :param fp_prob: false positive probability in decimal
        """

        self.fp_prob = fp_prob

        self.size = self.get_size(n=items_count, p=fp_prob)
        self.hash_count = self.get_hash_count(m=self.size, n=items_count)

        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, item: Any):
        """
        Add an item in a filter

        :param item: item to be added
        """

        digests = []

        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size

            digests.append(digest)

            self.bit_array[digest] = True

    def check(self, item: Any) -> bool:
        """
        Check for existence of an item in filter

        :param item: item to be checked
        :return: True if item in BloomFilter, False if not
        """

        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size

            if not self.bit_array[digest]:
                return False

        return True

    @classmethod
    def get_size(cls, n: int, p: int) -> int:
        """
        Returns the size of bit res_array(m) to used using following formula

        :param n: number of items expected to be stored in filter
        :param p: False Positive probability in decimal
        :return: size of res_array
        """

        m = - (n * math.log(p)) / (math.log(2) ** 2)
        m = int(m)

        return m

    @classmethod
    def get_hash_count(cls, m: int, n: int) -> int:
        """
        Returns the hash function(k) to be used using following formula

        :param m: size of bit res_array
        :param n: number of items expected to be stored in filter
        :return: number of hash functions needed
        """

        k = (m / n) * math.log(2)
        k = int(k)

        return k


if __name__ == '__main__':
    num_of_items = 20
    fp_prob = 0.000000005

    bloom_filter = BloomFilter(items_count=num_of_items, fp_prob=fp_prob)

    print(f'Size of bit res_array: {bloom_filter.size}')
    print(f'False positive probability: {bloom_filter.fp_prob}')
    print(f'Number of hash functions: {bloom_filter.hash_count}')

    word_present = ['abound', 'abounds', 'abundance', 'abundant', 'accessable',
                    'bloom', 'blossom', 'bolster', 'bonny', 'bonus', 'bonuses',
                    'coherent', 'cohesive', 'colorful', 'comely', 'comfort',
                    'gems', 'generosity', 'generous', 'generously', 'genial']

    word_absent = ['bluff', 'cheater', 'hate', 'war', 'humanity',
                   'racism', 'hurt', 'nuke', 'gloomy', 'facebook',
                   'geeksforgeeks', 'twitter']

    for item in word_present:
        bloom_filter.add(item)

    shuffle(word_present)

    test_words = word_present[:10] + word_absent

    shuffle(test_words)

    for word in test_words:
        if bloom_filter.check(word):
            if word in word_absent:
                print(f'{word} is false positive!')
            else:
                print(f'{word} is probably present!')

        else:
            print(f'{word} is definitely not present!')
