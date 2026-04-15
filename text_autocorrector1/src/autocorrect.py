from collections import Counter

class AutoCorrector:
    def __init__(self, word_list):
        self.WORDS = Counter(word_list)

    def probability(self, word):
        return self.WORDS[word] / sum(self.WORDS.values())

    def correction(self, word):
        return max(self.candidates(word), key=self.probability)

    def candidates(self, word):
        return (
            self.known([word]) or
            self.known(self.edits1(word)) or
            [word]
        )

    def known(self, words):
        return set(w for w in words if w in self.WORDS)

    def edits1(self, word):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]

        deletes = [L + R[1:] for L, R in splits if R]
        inserts = [L + c + R for L, R in splits for c in letters]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]

        return set(deletes + inserts + replaces)

    def correct_sentence(self, sentence):
        return " ".join(self.correction(word.lower()) for word in sentence.split())