# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = list(word)
        self.mask = list("_" * len(self.word))

    def guess(self, char):
        if self.remaining_guesses < 0:
            raise ValueError("Out of guesses")

        if self.remaining_guesses <= 0:
            self.status = STATUS_LOSE

        if char in self.word:
            i = self.word.index(char)
            self.mask[i] = self.word[i]
        else:
            self.remaining_guesses -= 1

    def get_masked_word(self):
        return "".join(self.mask)

    def get_status(self):
        return self.status
