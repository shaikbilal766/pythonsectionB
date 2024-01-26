class Mtca:
    chairman='Mr. kasif'
    location='palamaner'
    college='Mtca'

    def __init__(self,name,mobile):
        self.name = name
        self.mobile = mobile
class Mca(Mtca):
    principal='Mr. giri'
    strength=240
    staff = 35
class Btech(Mtca):
    principal='Mr. prashanth'
    strength=500
    staff = 50
bilal=Mca('bilal',7827487528)
siddiq=Mca('siddiq',837249827)

