from H2.Kodutöö import Kodutöö


class Õpilane:
    def __init__(self, nimi, kursuseNimetus):
        self.nimi = nimi
        self.kursuseNimetus = kursuseNimetus
        self.tegemataKodutööd = []
        self.tehtudKodutööd = []

    def lisaKodutöö(self, kodutöö):
        self.tegemataKodutööd.append(kodutöö)

    def tagastaTegemataKodutööd(self):
        for kodutöö in self.tegemataKodutööd:
            print('Tegemata on:', kodutöö.pealkiri)

    def märgiKodutööTehtud(self, kodutöö):
        self.tegemataKodutööd.remove(kodutöö)
        self.tehtudKodutööd.append(kodutöö)

    def tagastaTehtudKodutööd(self):
        for kodutöö in self.tehtudKodutööd:
            print('Tehtud on:', kodutöö.pealkiri)

    def tagastaHindelisedKodutööd(self):
        for kodutöö in self.tegemataKodutööd:
            if kodutöö.hindeline:
                print('Hindeline kodutöö on:', kodutöö.pealkiri)


Õpilane1 = Õpilane('Joosep Joosepson', 'ABC21')

Kodutöö1 = Kodutöö('Kirjand mingil teemal', True)
Kodutöö2 = Kodutöö('Essee mingil teemal', False)

Õpilane1.lisaKodutöö(Kodutöö1)
Õpilane1.lisaKodutöö(Kodutöö2)
Õpilane1.tagastaTegemataKodutööd()
Õpilane1.tagastaHindelisedKodutööd()
Õpilane1.märgiKodutööTehtud(Kodutöö1)
Õpilane1.tagastaTehtudKodutööd()
