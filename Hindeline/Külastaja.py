from Hindeline.Raamat import Raamat


class Külastaja:
    def __init__(self, eesNimi, perekonnaNimi):
        self.eesNimi = eesNimi
        self.perekonnaNimi = perekonnaNimi
        self.laenutatudRaamatud = []

    def laenutaRaamat(self, raamat):
        if not raamat.laenutatud:
            raamat.laenutatud = True
            self.laenutatudRaamatud.append(raamat)
        else:
            print('Raamat on juba laenutatud!')

    def tagastaRaamat(self, raamat):
        if raamat in self.laenutatudRaamatud:
            raamat.laenutatud = False
            self.laenutatudRaamatud.remove(raamat)
        else:
            print('Raamat pole veel laenutatud!')

    def kuvaLaenutatudRaamatud(self):
        if self.laenutatudRaamatud:
            for raamat in self.laenutatudRaamatud:
                print(raamat.tiitel)
        else:
            print('Hetkel pole laenutatud raamatuid!')


Külastaja1 = Külastaja('Joosep', 'Joosepson')

Raamat1 = Raamat('Mingi vahva raamat', 'Keegi kaval autor', 305)
Raamat2 = Raamat('Parimad koka road', 'Kuulus Ekspert', 275)

Külastaja1.laenutaRaamat(Raamat1)
Külastaja1.laenutaRaamat(Raamat2)
Külastaja1.tagastaRaamat(Raamat1)
Külastaja1.laenutaRaamat(Raamat2)
Külastaja1.kuvaLaenutatudRaamatud()
