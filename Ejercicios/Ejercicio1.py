class ParserEx1:
    def __init__(self, tokens):
        self.tokens = tokens[:]  
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

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
        p = self.save()
        if self.A() and self.B() and self.C():
            return True
        self.restore(p)
        if self.D() and self.E():
            return True
        self.restore(p)
        return False

    def A(self):
        if self.peek() == 'dos':
            self.match('dos')
            if not self.B(): return False
            if not self.match('tres'): return False
            return True
        return True

    def B(self):
        return self.Bp()

    def Bp(self):
        
        while self.peek() == 'cuatro':
            if not self.match('cuatro'): return False
            if not self.C(): return False
            if not self.match('cinco'): return False
        return True

    def C(self):
        if self.peek() == 'seis':
            self.match('seis')
            if not self.A(): return False
            if not self.B(): return False
            return True
        return True

    def D(self):
        p = self.save()
        if self.peek() == 'uno':
            if not self.match('uno'): self.restore(p); return False
            if not self.A(): self.restore(p); return False
            if not self.E(): self.restore(p); return False
            return True
        if self.B():
            return True
        self.restore(p)
        return False

    def E(self):
        return self.match('tres')

    def parse(self):
        ok = self.S()
        return ok and self.pos == len(self.tokens)


if __name__ == "__main__":
    tests = [
        ['dos','cuatro','seis','dos','cinco','tres'],  # ejemplo arbitrario
        ['uno','tres']  
    ]
    for t in tests:
        p = ParserEx1(t)
        print("Tokens:", t, "=>", "ACCEPT" if p.parse() else "REJECT")

