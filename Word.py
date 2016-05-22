# -*- coding: utf-8 -*-
import numpy as np
import PtBase
import PtAudio

u""" klasa przedstawiajaca slowo, slowo podawane w konstruktorze jest zapisywane w zmiennej __word
do zamiany na fonemy sluzy slownik __dictionaryF, kazdy fonem jest zapisany jako oddzielny string
w liscie ktora nazywa sie __tableF
przyklad: __word="dzban", tableF=['dz', 'b', 'a', 'n']
przejscie przez szereg metod umozliwia zapis zgodnie z fonetyka jezyka polskiego
na koniec zamiana na difony i odczytanie slow metoda text_to_speech"""


class Word(object):
    def __init__(self, word):
        self.__tableF = []
        self.__tableD = []
        self.__word = word.decode("utf-8")
        self.__dictionaryF = {'a': 'a', u'ą': 'an', 'b': 'b', 'c': 'c', u'ć': 'ci', 'd': 'd', 'e': 'e', u'ę': 'en',
                              'f': 'f', 'g': 'g', 'h': 'h', 'ch': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l',
                              u'ł': 'll', 'm': 'm', 'n': 'n', u'ń': 'ni', 'o': 'o', u'ó': 'u', 'p': 'p', 'r': 'r',
                              'rz': 'rz', 's': 's', u'ś': 'si', 't': 't', 'u': 'u', 'w': 'w', 'y': 'y',
                              'z': 'z', u'ź': 'zi', u'ż': 'rz', 'dz': 'dz', 'drz': 'drz', u'dż': 'drz', u'dź': 'dzi',
                              'cz': 'cz', 'sz': 'sz'}
        self.__dzwieczne = ['b', 'm', 'w', 'd', 'dz', 'z', 'n', 'zi', 'ni', 'drz', 'rz', 'r', 'g', 'a', 'an', 'o', 'e',
                            'en', 'y', 'i', 'u']
        self.__bezdzwieczne = ['p', 'f', 't', 'c', 's', 'cz', 'sz', 'si', 'k', 'h']
        self.__dz_bdz = {"b": "p", "dz": "c", "drz": "cz", "d": "t", "w": "f", "g": "k", "z": "s", "zi": "si",
                         "rz": "sz", "dzi": "ci"}
        self.__bdz_dz = {"p": "b", "c": "dz", "cz": "drz", "t": "d", "k": "g", "s": "z", "si": "zi", "ci": "dzi",
                         "f": "f", "sz": "sz"}
        self.__zwarteM = ['b', 'p']
        self.__zwarteN = ['t', 'd', 'c']
        self.__szczelinowe = ['v', 'w', 'f', 'z', 's', 'rz', 'sz', 'zi', 'si', 'ch']
        self.__samogloski = ['a', 'an', 'e', 'en', 'i', 'o', 'u', 'y']
        self.__spolgloski_nie_nosowe = ["b", "d", "g", "dz", "dzi", "drz", "p", "t", "k", "cz", "c", "ci", "w", "z",
                                        "zi", "rz", "f", "s", "si", "sz"]
        u"""w spółgłoskach nienosowych nie ma zawartego h, ponieważ nie ma swojego dźwięcznego odpowiednika"""

    def display_word(self):
        print self.__word

    def display_phenom(self):
        print self.__tableF

    def display_diphone(self):
        print self.__tableD

    def phenom(self):
        k = 0
        word1 = self.__word + "o"   u""" prywatny patent! :D o na koncu nie tworzy zadnego dwuznaku,
                                 powoduje dodanie ramki dzieki czemu nie trzeba bawić sie z
                                 dzieki temu mozemy w ifie iterowac po calym slowie, czyli do jego dlugosci"""

        for j in range(len(self.__word)):
            if k < (len(self.__word)):
                x = word1[k] + word1[k + 1]
                if x == 'ch' or x == 'cz' or x == 'dz' or x == u'dż' or x == u'dź' or x == 'rz' or x == 'sz':
                    a = self.__dictionaryF[x]
                    self.__tableF.append(a)
                    k += 1
                else:
                    a = self.__dictionaryF[self.__word[k]]
                    self.__tableF.append(a)
            k += 1

    def syllable_with_i(self):
        # print len(self.__tableF)
        for i in range(len(self.__tableF) - 1):
            if self.__tableF[i] == 'i':
                x = self.__tableF[i + 1]
                y = self.__tableF[i - 1]

                if (x == 'a' or x == 'an' or x == "e" or x == "en" or x == 'u' or x == 'o') and (
                                not (not (y != 's') or not (y != 'c') or not (
                                            y != 'n')) and y != 's' and y != 'dz'):
                    self.__tableF[i] = 'j'

    def upodobnienia_postepowe(self):
        __tab = list(self.__tableF)

        flag1 = 'rz' in __tab
        flag2 = 'w' in __tab

        while flag1:
            idx = __tab.index("rz")
            if idx > 0:
                if __tab[idx - 1] in self.__bezdzwieczne:
                    print("zamieniam rz na sz!")
                    self.__tableF[idx] = 'sz'
            __tab[idx] = " x"
            flag1 = "rz" in __tab

        while flag2:
            idx = __tab.index("w")
            if idx > 0:
                if __tab[idx - 1] in self.__bezdzwieczne:
                    print("zamieniam w na f!")
                    self.__tableF[idx] = 'f'
            __tab[idx] = "x"
            flag2 = "w" in __tab

        print self.__tableF

    def upodobnienia_wsteczne(self):
        i = len(self.__tableF)
        iterator = i - 1
        while iterator > 0:
            if self.__tableF[i] in self.__dzwieczne:
                if self.__tableF[i - 1] in self.__bezdzwieczne:
                    self.__tableF[i - 1] = self.__bdz_dz[self.__tableF[i - 1]]
            if self.__tableF[i] in self.__dzwieczne:
                if self.__tableF[i - 1] in self.__bezdzwieczne:
                    self.__tableF[i - 1] = self.__dz_bdz[self.__tableF[i - 1]]
            iterator -= 1
            i -= 1

    def zmien_dzwiecznnosc(self):
        __dz = ['b', 'dz', 'drz', 'd', 'w', 'g', 'z', 'zi', 'rz']
        length = len(self.__tableF)
        letter = self.__tableF[length - 1]
        if letter in __dz:
            self.__tableF[length - 1] = self.__dz_bdz[letter]

    def change_to_diphone_word(self):
        letter = self.__tableF[0]
        self.__tableD.append('_+' + letter)
        length = len(self.__tableF)
        for i in range(length - 1):
            self.__tableD.append(self.__tableF[i] + "+" + self.__tableF[i + 1])
        self.__tableD.append(self.__tableF[length - 1] + "+_")

    # Metody Karla
    # Poniżej wklej swoje metody

    def denezalization(self):
        i = 0
        # denezalizacja czyli obsluga koncowek typu ela, al, e
        for i in range(len(self.__tableF)):
            if self.__tableF[i] == "en" and i != len(self.__tableF) - 1:
                if self.__tableF[i + 1] == "ll":
                    if self.__tableF[i + 2] == "a":
                        self.__tableF[i] = "e"
                        self.__tableF[i + 1] = "ll"
                        self.__tableF[i + 2] = "a"
        if self.__tableF[i] == "an":
            if self.__tableF[i + 1] == "ll":
                self.__tableF[i] = "o"
                self.__tableF[i + 1] = "ll"
        if self.__tableF[len(self.__tableF) - 1] == "en":
            self.__tableF[len(self.__tableF) - 1] = "e"

    def softless(self):
        # obsluga wymowy glosek miekkich (c, z, n, s) i zmiekczonych (takich po ktorych "dodajemy" i)
        if "dz" in self.__tableF:
            for i in range(len(self.__tableF)):
                if self.__tableF[i] == "dz":
                    if self.__tableF[i + 1] == "j":
                        self.__tableF[i] = "dzi"
        elif "z" in self.__tableF:
            for i in range(len(self.__tableF)):
                if self.__tableF[i] == "z":
                    if self.__tableF[i + 1] == "m":
                        if self.__tableF[i + 2] == "j":
                            self.__tableF[i] += "i"
                    elif self.__tableF[i + 1] == "i":
                        self.__tableF[i] = "zi"
        elif "c" in self.__tableF:
            for i in range(len(self.__tableF)):
                if self.__tableF[i] == "c":
                    if self.__tableF[i + 1] == "i":
                        self.__tableF[i] = "ci"
        elif "s" in self.__tableF:
            for i in range(len(self.__tableF)):
                if self.__tableF[i] == "s":
                    if self.__tableF[i + 1] == "i":
                        self.__tableF[i] = "si"

    def double_i_on_end(self):
        # obsluga podwojnego i na koncu wyrazu
        if self.__tableF[len(self.__tableF) - 1] == "i" and self.__tableF[len(self.__tableF) - 2] == "i":
            self.__tableF.pop()

            # Metody Mateusza
            # Poniżej wklej swoje metody

    def asynchronous_pronunciation_nasal(self):
        __tab = list(self.__tableF)
        ann = "an" in __tab
        enn = "en" in __tab
        while ann:
            idx_an = __tab.index("an")
            if 0 < idx_an < len(__tab) - 1:
                if __tab[idx_an + 1] in self.__zwarteM:
                    self.__tableF[idx_an] = 'o'
                    self.__tableF.insert(idx_an + 1, 'm')
                if __tab[idx_an + 1] in self.__zwarteN:
                    self.__tableF[idx_an] = 'o'
                    self.__tableF.insert(idx_an + 1, 'n')
            else:
                self.__tableF[idx_an] = 'o'
                self.__tableF.append('ll')
            __tab[idx_an] = "x"
            ann = "an" in __tab
        while enn:
            idx_en = __tab.index("en")
            if 0 < idx_en < len(__tab) - 1:
                if __tab[idx_en + 1] in self.__zwarteM:
                    self.__tableF[idx_en] = 'e'
                    self.__tableF.insert(idx_en + 1, 'm')
                if __tab[idx_en + 1] in self.__zwarteN:
                    self.__tableF[idx_en] = 'e'
                    self.__tableF.insert(idx_en + 1, 'n')
            else:
                self.__tableF[idx_en] = 'e'
            __tab[idx_en] = "x"
            enn = "en" in __tab

    def synchronous_pronunciation_nasal(self):
        idx_an = 0
        __tab = list(self.__tableF)
        ann = "an" in __tab
        enn = "en" in __tab
        while ann:
            idx_an = __tab.index("an")
            if 0 < idx_an < len(__tab) - 1:
                if __tab[idx_an + 1] in self.__szczelinowe:
                    self.__tableF[idx_an] = 'on'
            else:
                self.__tableF[idx_an] = 'o'
                self.__tableF.append('ll')
            __tab[idx_an] = "x"
            ann = "an" in __tab

        while enn:
            idx_en = __tab.index("en")
            if 0 < idx_en < len(__tab) - 1:
                if __tab[idx_en + 1] in self.__zwarteM:
                    self.__tableF[idx_en] = 'en'
            else:
                self.__tableF[idx_an] = 'e'
            __tab[idx_en] = "x"
            enn = "en" in __tab

            # synteza, proste sklejanie wersja bardzo wstepna

    def complete_diphones(self):
        # metoda tworząca difony w przypadku ich braku, np gdy nie ma difonu o+t tworzy o+_, _+t
        # na sztywno wpisane reguly w przypadku gdy nie mozna stworzyc difonu,
        # np z+_ zamieniane jest na _+z, tak samo dla w

        diphonelist = open('confdata/diphonelist.txt', "r")
        availablediphones = diphonelist.readlines()
        diphonelist.close()

        missingdiphones = {"z+_": "_+z", "z+.": "_+z", "w+_": "_+w", "w+.": "f+."}
        for x in range(len(availablediphones)):
            availablediphones[x] = availablediphones[x].rstrip(
                '\n')  # usuwanie białych znaków z zaczytanego pliku z difonami

        for aa in range(len(self.__tableD)):
            # pętla która działa dopóki wszystkie difony nie będą znane

            while not (self.__tableD[aa] in availablediphones):
                for i in range(len(self.__tableD)):
                    if self.__tableD[i] in missingdiphones:
                        self.__tableD[i] = missingdiphones[self.__tableD[i]]
                    if not (self.__tableD[i] in availablediphones):
                        print "Brak difonu " + self.__tableD[i] + " w bazie, uzupelniam"

                        temp_word = self.__tableD[i]
                        pindex = self.__tableD[i].index("+")
                        if temp_word[0] == "_" and len(temp_word) > 3:
                            new_diphone = ['_+' + temp_word[pindex + 1], temp_word[pindex + 2:len(temp_word)] + "+."]
                        elif temp_word[len(temp_word) - 1] == "_":
                            new_diphone = [temp_word[0] + '+.', '_+' + temp_word[1]]
                        elif temp_word[len(temp_word) - 1] == ".":
                            new_diphone = [temp_word[0] + '+.', '_+' + temp_word[1]]
                        else:
                            new_diphone = [temp_word[0:pindex] + '+.', '_+' + temp_word[pindex + 1:len(temp_word)]]
                        print new_diphone
                        self.__tableD.insert(i, new_diphone[0])
                        self.__tableD.insert(i + 1, new_diphone[1])
                        self.__tableD.remove(temp_word)

    def text_to_speech(self):
        length = len(self.__tableD)
        wave = []
        for i in range(length):
            x = PtBase.DiphonBase.db[self.__tableD[i]].wav
            wave = np.append(wave, x)
        px = PtAudio.Play(0)
        px.run(wave)

    def create_table_diphone():
        wrd.display_word()
        wrd.phenom()
        wrd.display_phenom()
        wrd.double_i_on_end()
        wrd.zmien_dzwiecznnosc()
        wrd.syllable_with_i()
        wrd.upodobnienia_postepowe()
        wrd.display_phenom()
        wrd.asynchronous_pronunciation_nasal()
        wrd.display_phenom()
        wrd.synchronous_pronunciation_nasal()
        wrd.display_phenom()
        wrd.softless()
        wrd.denezalization()
        wrd.change_to_diphone_word()
        wrd.display_diphone()
        wrd.complete_diphones()

    create_table_diphone = staticmethod(create_table_diphone)


wrd = Word('chrząszczbrzmiwtrzciniewszczebrzeszynie')
wrd.create_table_diphone()
wrd.text_to_speech()
