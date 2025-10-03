class ParserEx3:
    def __init__(self, tokens):
        self.tokens = tokens[:]
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def match(self, tk):
        if self.peek() == tk:
            self.pos += 1
            return True
        return False

    def save(self):
        return self.pos

    def restore(self, p):
        self.pos = p

    def S(self):
        if not self.A(): return False
        if not self.B(): return False
        if not self.C(): return False
        if not self.Sp(): return False
        return True

    def Sp(self):
        while self.peek() == 'uno':
            self.match('uno')
        return True


    def A(self):
        if self.peek() == 'dos':
            self.match('dos')
            if not self.B(): return False
            if not self.C(): return False
            return True
        return True

    def B(self):
        p = self.save()
        if self.C():
            if self.match('tres'):
                return True
            else:
                self.restore(p)
                return True
        self.restore(p)
        return True

    def C(self):
        if self.peek() == 'cuatro':
            self.match('cuatro')
            return self.B()
        return True

    def parse(self):
        ok = self.S()
        return ok and self.pos == len(self.tokens)

# --- Ejemplo de uso:
if __name__ == "__main__":
    tests = [
        ['dos','cuatro','tres','uno','uno'],  # S -> A B C Sp posible
        ['cuatro','tres']  # A->ε, B->C tres when C->cuatro B (here C->cuatro ...), etc.
    ]
    for t in tests:
        p = ParserEx3(t)
        print("Tokens:", t, "=>", "ACCEPT" if p.parse() else "REJECT")
