import random

class Symbol:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Reel:
    def __init__(self, symbols):
        self.symbols = symbols

    def spin(self):
        return random.choice(self.symbols)

class SlotMachine:
    def __init__(self, reels=3):
        self.reels = reels

    def generate_random_result(self):
        return [random.choice(["🍒", "🍋", "🔔", "🍉", "⭐", "7️⃣"]) for _ in range(self.reels)]
    
    def play(self):
        return self.generate_random_result()

class Bet:
    def __init__(self, amount):
        self.amount = amount
