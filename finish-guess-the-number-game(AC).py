class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
    def guess(self, n):
        if self.lives <= 0:
            raise Exception('Omae wa mo shindeiru')
        if n == self.number:
            return True
        if self.lives > 0:
            self.lives -= 1
        return False
