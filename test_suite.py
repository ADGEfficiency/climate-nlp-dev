import polarity_analyser

def test_polarity_without_shifter():
    model = polarity_analyser.polarity_without_shifter("Das hier ist der erste Testsatz")


def test_polarity_with_shifter():
    model = polarity_analyser.polarity_with_shifter("Das hier ist der erste Testsatz")




def text_polarity_with_shifter_other_lexicon():
    model = polarity_analyser.polarity_with_shifter("Das hier ist der erste Testsatz",
                                                     1)



