from faker import Faker
fake_data = Faker()
class tel:
    def __init__(self,imie,nazwisko,mail):
        self.imie = imie
        self.nazwisko = nazwisko
        self.mail = mail
        
        self.length = 0
        @property
        def label_length(self):
            return self.length
        @label_length.setter
        def label_length(self):
            self.length = len(imie) + len(nazwisko)
class BaseContact(tel):
    def __init__(self, nrpryw, imie, nazwisko, mail):
        super().__init__(imie, nazwisko, mail)
        self.nrpryw = nrpryw
    def contact(self):
        print(f"Wybieram numer +48 {self.nrpryw} i dzwonię do {self.imie} {self.nazwisko}")
class BusinessContact(tel):
    def __init__(self, firma, stanowisko, nrsluz, imie, nazwisko, mail):
        super().__init__(imie, nazwisko, mail)
        self.firma = firma
        self.stanowisko = stanowisko
        self.nrsluz = nrsluz
    def contact(self):
        print(f"Wybieram numer +48{self.nrsluz} i dzwonię do {self.imie} {self.nazwisko}")

def create_contacts():
    n = int(input("Podaj liczbe generowanych danych: "))
    i=0
    while i<n:
        tel.imie = fake_data.first_name()
        tel.nazwisko = fake_data.last_name()
        tel.mail = fake_data.safe_email()
        BaseContact.nrpryw = fake_data.phone_number()
        BusinessContact.firma = fake_data.company()
        BusinessContact.stanowisko = fake_data.job()
        BusinessContact.nrsluz = fake_data.phone_number()
        i = i+1
create_contacts()