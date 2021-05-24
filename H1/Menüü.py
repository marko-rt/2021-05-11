from H1.Toit import Toit


class Menüü(Toit):
    def __init__(self, pealkiri):
        self.pealkiri = pealkiri
        self.toidud = []

    def lisaToit(self, toit):
        self.toidud.append(toit)

    def kuvaToidudJaHinnad(self):
        for toit in self.toidud:
            print('Menüüs saadaval olevad toidud:', toit.nimetus, toit.hind)

    def kuvaPäevaEri(self):
        for toit in self.toidud:
            if toit.päevaEri:
                print('Päeva eripakkumine on:', toit.nimetus, toit.hind)

    def leiaKallimToit(self):
        suurimHind = 0
        for toit in self.toidud:
            if toit.hind > suurimHind:
                suurimHind = toit.hind
                kallimToit = toit
                print(kallimToit.nimetus, kallimToit.hind)


Kohvik1 = Menüü('Emadepäeva menüü')

Toit1 = Toit('Ühepaja toit', 3.75, False)
Toit2 = Toit('Sealiha guljašš', 4.25, False)
Toit3 = Toit('Pasta bolognese', 3.00, True)

Kohvik1.lisaToit(Toit1)
Kohvik1.lisaToit(Toit2)
Kohvik1.lisaToit(Toit3)
Kohvik1.kuvaToidudJaHinnad()
Kohvik1.kuvaPäevaEri()
Kohvik1.leiaKallimToit()
