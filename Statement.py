# -*- coding: utf-8 -*-
import re
import WriteNumber as wr


class Statement(object):
    def __init__(self, statement):
        self.__statemnt = statement
        self.__normalized_statment = " "
        self.__tokenStatment = []
        self.__tokenWords = []
        self.__f_word = " "
        self.__flag_number = True

    def display_statement(self):
        print self.__statemnt

    def display_normalized_statment(self):
        print self.__normalized_statment

    def normalized_statment(self):
        self.__normalized_statment = self.__statemnt
        self.__normalized_statment = self.__normalized_statment.lower()
        self.__flag_number = self.__normalized_statment.isalpha()
        print self.__flag_number

    def statement_tokenize_to_sentence(self):
        self.__tokenStatment = re.split("(\.[^0-9]|,|\.$)", self.__normalized_statment)

    def sentence_tokenize_to_words(self):
        i = 0
        j = 0

        while i < len(self.__tokenStatment):
            temp = re.split(" ", self.__tokenStatment[i])
            while j < len(temp):
                if len(temp[j]) > 0:
                    self.__tokenWords.append(temp[j])
                j += 1
            i += 1
            j = 0
        print self.__tokenWords

    def number_to_word(self):
        if not self.__flag_number:
            j = 0;
            while j < len(self.__tokenWords):
                if not self.__tokenWords[j].isalpha():
                    num = self.__tokenWords[j]
                    if num[0] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                        number = wr.WriteNumber(str(num))
                        k = number.how_is_number()
                        if k == 1:
                            self.__tokenWords[j] = number.write_units()
                        elif k == 2:
                            self.__tokenWords[j] = number.write_tens()
                        elif k == 3:
                            self.__tokenWords[j] = number.write_hunderds()
                # print self.__tokenWords[j]
                j += 1

    def word_to_periodic_word(self):
        i = 1;
        self.__f_word=self.__tokenWords[0]
        print self.__f_word
        while i < len(self.__tokenWords):
            self.__f_word += self.__tokenWords[i]
            print self.__f_word
            i += 1


st = Statement("Ala ma 12 też. A ja mam 5 kóz")
# wyswietl wprowadzona wypowiedz
st.display_statement()
# normalizacja
st.normalized_statment()
# st.display_normalized_statment()
# podziel wypowiedz na zdania
st.statement_tokenize_to_sentence()
# podziel zdania na slowa
st.sentence_tokenize_to_words()
# jesli wystepuja liczby to zamien je na slowa
st.number_to_word()
st.word_to_periodic_word()
