class Poly:
    def __init__(self, c=0, n=0):
        if n < 0:
            raise ValueError("Poly(int, int) constructor: n must be >= 0")
        self.trms = {}
        if c != 0:
            self.trms[n] = c

    def degree(self):
        if len(self.trms) > 0:
            return next(reversed(self.trms.keys()))
        return 0

    def coeff(self, d):
        if d < 0:
            raise ValueError("Poly.coeff: d must be >= 0")
        return self.trms.get(d, 0)

    def sub(self, q):
        if q is None:
            raise ValueError("Poly.sub: q is None")
        return self.add(q.minus())

    def minus(self):
        result = Poly()
        for n, c in self.trms.items():
            result.trms[n] = -c
        return result

    def add(self, q):
        if q is None:
            raise ValueError("Poly.add: q is None")
        
        non_zero = set(self.trms.keys()).union(q.trms.keys())
        result = Poly()
        for n in non_zero:
            new_coeff = self.coeff(n) + q.coeff(n)
            if new_coeff != 0:
                result.trms[n] = new_coeff
        return result

    def mul(self, q):
        if q is None:
            raise ValueError("Poly.mul: q is None")
        
        result = Poly()
        for n1, c1 in self.trms.items():
            for n2, c2 in q.trms.items():
                result = result.add(Poly(c1 * c2, n1 + n2))
        return result

    def __str__(self):
        r = "Poly:"
        if len(self.trms) == 0:
            r += " 0"
        for n, c in self.trms.items():
            if c < 0:
                r += f" - {-c}x^{n}"
            else:
                r += f" + {c}x^{n}"
        return r

if __name__ == "__main__":
    mp = Poly()
    print(f"1. Poly mp = {mp}")
    mp = mp.add(Poly(3, 5))
    print(f"2. Poly mp = {mp}")
    mp = mp.add(Poly(-3, 5))
    print(f"3. Poly mp = {mp}")
    mp = mp.add(Poly(-3, 5))
    print(f"4. Poly mp = {mp}")
    mp = mp.add(Poly(-2, 2))
    print(f"5. Poly mp = {mp}")
    print(f"6. Poly -mp = {mp.minus()}")
    print(f"7. Poly mp*mp = {mp.mul(mp)}")

    mp1 = Poly(1,2)
    print(f"8. Poly mp1 = {mp1}")
    mp1 = mp1.add(Poly(2,5))
    print(f"9. Poly mp1 = {mp1}")
    mp1  = mp1.add(mp)
    print(f"10. Poly mp1 = {mp1}")