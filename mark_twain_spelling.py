# http://community.topcoder.com/stat?c=problem_statement&pm=1876&rd=4650


class Twain(object):

    def year1(self, word):
        return word 

    def year2(self, word):
        return word

    def year3(self, word):
        return word

    def year4(self, word):
        return word

    def year5(self, word):
        return word

    def year6(self, word):
        return word

    def year7(self, word):
        return ''.join(word)

    def getNewSpelling(self, year, phrase):
        for i in range(1, min(year+1, 7+1)):
            func = getattr(self, "year%s" % i)
            words = map(lambda word: func(list(word)), phrase.split())
            phrase = ' '.join(words)
        return phrase


twain = Twain()
# 1
print twain.getNewSpelling(2, "I fixed the chrome xerox by the cyclical church")
# 3
print twain.getNewSpelling(7, "sch kn x xschrx cknnchc cyck xxceci")
# 6
print twain.getNewSpelling(7, "cck xzz aaaaa")
