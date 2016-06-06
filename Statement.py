# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
import re
import WriteNumber as wr
import Word as word


class Statement(object):
    def __init__(self, statement):
        self.__statemnt = statement
        self.__normalized_statment = " "
        self.__tokenStatment = []
        self.__tokenWords = []
        self.__p_word = " "
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
                    self.__tokenWords.append(unicode(temp[j], 'utf-8', 'ignore'))
                j += 1
            i += 1
            j = 0
        print self.__tokenWords

    def number_to_word(self):
        if not self.__flag_number:
            j = 0
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

    def words_to_prosodic_word(self):
        i = 1
        self.__p_word = self.__tokenWords[0]
        # print self.__p_word
        while i < len(self.__tokenWords):
            self.__p_word += self.__tokenWords[i]
            # print self.__p_word
            i += 1

    def tts(self):
        prosodic_word = word.Word(self.__p_word)
        prosodic_word.display_word()
        prosodic_word.phenom()
        prosodic_word.display_phenom()
        prosodic_word.double_i_on_end()
        prosodic_word.zmien_dzwiecznnosc()
        prosodic_word.syllable_with_i()
        prosodic_word.upodobnienia_postepowe()
        prosodic_word.display_phenom()
        prosodic_word.asynchronous_pronunciation_nasal()
        prosodic_word.display_phenom()
        prosodic_word.synchronous_pronunciation_nasal()
        prosodic_word.display_phenom()
        prosodic_word.softless()
        prosodic_word.denezalization()
        prosodic_word.change_to_diphone_word()
        prosodic_word.display_diphone()
        prosodic_word.complete_diphones()
        prosodic_word.text_to_speech()


st = Statement("Idzie Grześ Przez wieś, Worek piasku niesie, A przez dziurkę Piasek ciurkiem Sypie się za Grzesiem. "
               "Piasku mniej Nosić lżej. Cieszy się głuptasek. Do dom wrócił,Worek zrzucił Ale gdzie ten piasek. "
               "Wraca Grześ Przez wieś,Zbiera piasku ziarnka.Pomaluśku Zebrała się miarka.")
# st = Statement("Zapraszamy na AKADEMICKIE FIRMOWE EWOLUCJE. Biznesplan to element planowania strategicznego. Wytycza "
#                "cele, metody działania oraz pomaga dokonać właściwego wyboru spośród kilku wariantów inwestycyjnych.")
#st =Statement("Ala ma 2 koty, a Ola 13 tego ma urodziny. One się lubią.")
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
st.words_to_prosodic_word()
st.tts()
