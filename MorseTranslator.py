import MorseCode


class MorseTranslator:
    dictionary = MorseCode.translator_code

    def text_to_morse(self, text):
        return " ".join(self.dictionary[i]
                        for i in " ".join(text.split()).upper() if i in self.dictionary)

    def morse_to_text(self, text):
        text = text.split()
        new = []
        for symbol in text:
            for i in self.dictionary:
                if symbol == self.dictionary[i]:
                    new.append(i)

        return "".join(new)
