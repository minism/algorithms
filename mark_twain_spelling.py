# http://community.topcoder.com/stat?c=problem_statement&pm=1876&rd=4650


class Twain(object):
    def year0(self, word):
        return ''.join(word)

    def year1(self, word):
        out = [word[0] == 'x' and 'z' or word[0]]
        for char in word[1:]:
            if char == 'x':
                out.extend(['ks'])
            else:
                out.append(char)
        return ''.join(out)

    def year2(self, word):
        return ''.join(word).replace('y', 'i')

    def year3(self, word):
        out = []
        for i, char in enumerate(word):
            if char == 'c' and i + 1 < len(word) and word[i+1] in ('e', 'i'):
                out.append('s')
            else:
                out.append(char)
        return ''.join(out)

    def year4(self, word):
        i = 0
        while i < len(word):
            char = word[i]
            if char == 'k':
                j = i - 1
                while j >= 0 and word[j] == 'c':
                    word[j] = None
                    j -= 1
            i += 1
        return ''.join(filter(bool, word))

    def year5(self, word):
        out = []
        i = 0
        if len(word) > 2 and word[0] == 's' and word[1] == 'c' and word[2] == 'h':
            out.extend(['sk'])
            i = 3
        while i < len(word):
            char = word[i]
            if char == 'c' and i + 2 < len(word) and word[i+1] == 'h' and word[i+2] == 'r':
                out.append('k')
                i += 2
            else:
                out.append(char) 
                i += 1
        for i, char in enumerate(out):
            if char == 'c' and (i + 1 >= len(out) or out[i+1] != 'h'):
                out[i] = 'k'
        return ''.join(out)

    def year6(self, word):
        if len(word) > 1 and word[0] == 'k' and word[1] == 'n':
            return ''.join(['n'] + word[2:])
        return ''.join(word)

    def year7(self, word):
        i = 0
        while i < len(word):
            char = word[i]
            if char not in ('a', 'e', 'i', 'o', 'u'):
                j = i - 1
                while j >= 0 and word[j] == char:
                    word[j] = None
                    j -= 1
            i += 1
        return ''.join(filter(bool, word))

    def getNewSpelling(self, year, phrase):
        for i in range(min(year+1, 7+1)):
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
