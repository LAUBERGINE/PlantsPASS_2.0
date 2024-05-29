class Stockage:
    def __init__(self, site, identifiant, password):
        self.site = site
        self.identifiant = identifiant
        self.password = password

    def view_stockage(self):
        print(f"Site : {self.site}")
        print(f"Identifiant : {self.identifiant}")
        print(f"Password : {self.password}")

    def save(self):
        fichier = open('plantPass.egplt', 'a')
        fichier.write(f"{self.site};{self.identifiant};{self.password}\n")
        fichier.close()

def genVar():
    site = input("Site: ")
    identifiant = input("Identifiant: ")
    password = input("Password: ")
    return Stockage(site, identifiant, password)

def load(stock):
    try:
        fichier = open('plantPass.egplt', 'r')
        for ligne in fichier:
            site, identifiant, password = ligne.strip().split(';')
            stock.append(Stockage(site, identifiant, password))
        fichier.close()
    except FileNotFoundError:
        pass 