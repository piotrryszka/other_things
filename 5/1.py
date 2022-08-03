class Zwierzak:

    def __init__(self, imie="Brak imienia", wiek=1):
        self.imie = imie
        self.wiek = wiek
        self.rasa = ["canis lupus"]

    def ruszaj(self):
        print("Zwierzak o imieniu", self.imie, "idzie na spacer")


azor = Zwierzak("Azor", 1)
azor.rasa = "burek"
# azor.imie = "Azor"
print(azor.rasa)
azor.ruszaj()

fifi = Zwierzak("Fifi", 2)
fifi.rasa += ["wulf"]
# fifi.imie = "Fifi"
print(fifi.rasa)
fifi.ruszaj()
print(azor.rasa)

gapcio = Zwierzak(wiek=2, imie="Gapcio")
gapcio.rasa = "chomik"
gapcio.ruszaj()
print(gapcio.wiek)

