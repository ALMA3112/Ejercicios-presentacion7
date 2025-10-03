
class ParserEx2:
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
        p = self.save()
        if self.try_B_uno():
            return True
        self.restore(p)
        if self.peek() == 'dos':
            self.match('dos')
            if not self.C(): return False
            return True
        self.restore(p)
        return True

    def try_B_uno(self):
        p = self.save()
        if self.B():
            if self.match('uno'):
                return True
        self.restore(p)
        return False

    def A(self):
        p = self.save()
        if self.S():
            if self.match('tres') and self.B() and self.C():
                return True
        self.restore(p)
        if self.peek() == 'cuatro':
            self.match('cuatro')
            return True
        # epsilon
        return True

    def B(self):
        p = self.save()
        if self.A():
            if self.match('cinco') and self.C() and self.match('seis'):
                return True
        self.restore(p)
        # epsilon
        return True

    def C(self):
        if self.peek() == 'siete':
            self.match('siete')
            return self.B()
        return True

    def parse(self):
        ok = self.S()
        return ok and self.pos == len(self.tokens)

if __name__ == "__main__":
    tests = [
        ['dos','siete','cuatro'], # ejemplo arbitrario
        ['cuatro','cinco','siete']  # ejemplo
    ]
    for t in tests:
        p = ParserEx2(t)
        print("Tokens:", t, "=>", "ACCEPT" if p.parse() else "REJECT")
