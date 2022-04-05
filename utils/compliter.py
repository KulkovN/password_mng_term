class MyCompleter(object):  # кастомный комплитер с переделанным инициализирующим методом

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # на первый тригер накидывается первое возможное совпадение
            if text:  # совпадения в кэше (записи, начинающиеся с введенного текста)
                self.matches = [s for s in self.options 
                                    if s and s.startswith(text)]
            else:  # если не находит кокнретное совпадение выводить перечен подходящих
                self.matches = self.options[:]

        # return match indexed by state
        try: 
            return self.matches[state]
        except IndexError:
            return None
