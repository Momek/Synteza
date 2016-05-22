# -*- coding: utf-8 -*-
import re
import Write_number as wr


class Statement(object):
    def __init__(self, statement):
        self.__statemnt = statement
        # dokonczyc co potrzeba
        self.__normalized_statment = " "
        self.__tokenStatment = []
        self.__tokenWords = []
        # self.number = wr.WriteNumber()

    def display_statment(self):
        print self.__statemnt

    def display_normalized_statment(self):
        print self.__normalized_statment

    def normalized_statment(self):
        self.__normalized_statment = self.__statemnt
        self.__normalized_statment = self.__normalized_statment.lower()
        flag_number = self.__normalized_statment.isalpha()
        if flag_number is False:
            print " "
            # dopisac metode

    @staticmethod
    def write_number(num):
        k = num
        i = 0
        number = []
        while k > 0:
            number.append(k % 10)
            k /= 10
            i += 1
        print number

    def statement_tokenize_to_sentence(self):
        self.__tokenStatment = re.split("\.[^0-9]", self.__statemnt)
        print self.__tokenStatment

    def sentence_tokenize_to_words(self):
        i = 0
        j = 0
        while i < len(self.__tokenStatment):
            temp = re.split(" ", self.__tokenStatment[i])
            while j < len(temp):
                self.__tokenWords.append(temp[j])
                j += 1
            i += 1
            j = 0
        print self.__tokenWords


st = Statement("Ala ma 2.0 kota. I temperatura wynosi 27.988 stopni. Ala ma kocury 2, ale też 3 psy.")
# wyswietl wprowadzona wypowiedz
st.display_statment()
# normalizacja
st.normalized_statment()
st.display_normalized_statment()
# podziel wypowiedz na zdania
st.statement_tokenize_to_sentence()
# podziel zdania na slowa
st.sentence_tokenize_to_words()
