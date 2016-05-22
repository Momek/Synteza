# -*- coding: utf-8 -*-


class WriteNumber(object):
    def __init__(self, nb):
        self.number = []
        self.__num = int(nb)
        self.__dictionaryU = {'1': 'jeden', '2': 'dwa', '3': 'trzy', '4': ' cztery', '5': u'pieńć', '6': u'sześć',
                              '7': 'siedem', '8': 'osiem', '9': u'dziewieńć', '0': 'zero'}
        self.__dictionaryT1 = {'0': u'dziesieńć', '1': u'jedynaście', '2': u'dwanaście', '3': u'trzynaście',
                               '4': u'czternaście', '5': u'pietnaście', '6': u'szesnaście', '7': u'siedemnaście',
                               '8': u'osiemnaście', '9': u'dziewietnaście'}
        self.__dictionaryT = {'1': u'dziesieńć', '2': u'dwadzieścia', '3': u'trzydzieści', '4': u'czterdzieści',
                              '5': u'pieńdziesiąt', '6': u'sześdziesiąt', '7': u'siedemdziesiąt', '8': u'osiemdziesiąt',
                              '9': u'dziewieńdziesiąt'}
        self.__dictionaryH = {'1': 'sto', '2': u'dwieście', '3': 'trzysta', '4': 'czterysta', '5': u'pieńćset',
                              '6': u'sześset', '7': 'siedemset', '8': 'osiemset', '9': u'dziewieńćset'}

        self.__result = ""
        self.i = 0

    def how_is_number(self):
        k = self.__num
        while k > 0:
            self.number.append(k % 10)
            k /= 10
            self.i += 1
        print self.i

    def write_units(self):
        n = self.number[0]
        m = str(n)
        return self.__dictionaryU[m]

    def write_tens(self):
        n_u = str(self.number[0])
        n_t = str(self.number[1])

        if n_t == '1':
            self.__result = self.__dictionaryT1[n_u]
        else:
            if n_u == 0:
                return self.__dictionaryT[n_t]
            else:
                n1 = self.__dictionaryT[n_t]
                n2 = self.__dictionaryU[n_u]
                n12 = n1 + " " + n2
                return n12

    def write_hunderds(self):
        n_h = str(self.number[2])
        n3 = self.__dictionaryH[n_h]
        n12 = self.write_tens()
        n123 = n3 + " " + n12
        return n123


# nm = WriteNumber('321')
# nm.how_is_number()
# c = nm.write_hunderds()
print c
