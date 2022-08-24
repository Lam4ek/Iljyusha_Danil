class Vehicle:

    def __init__(self, manufacturer, model, engine, seats, topSpead):
        self.manufacturer = manufacturer
        self.model = model
        self.engine = engine
        self.seats = seats
        self.topSpead = topSpead

    def get_info(self):
        str1 = self.manufacturer
        str2 = self.model
        str3 = self.engine
        str5 = self.seats
        str6 = self.topSpead

        return f'{self.manufacturer}{self.model}{self.engine}{self.seats}{self.topSpead}'


if __name__ == "__main__":
    person = Vehicle('Volvo', '7900', "2.4", "154", "70")
    print(f""""Автобус {person.manufacturer} {person.model} с объёмом двигателя 
{person.engine} количество мест {person.seats} имеет максимальную скорость - {person.topSpead} км/ч""")

    person = Vehicle('Hyundai', 'Universe', "12.3", "47", "142")
    print(f""""Автобус {person.manufacturer} {person.model} с объёмом двигателя 
{person.engine} количество мест {person.seats} имеет максимальную скорость - {person.topSpead} км/ч""")

    person = Vehicle('Scania', 'Irizar i6', "9", "67", "100")
    print(f""""Автобус {person.manufacturer} {person.model} с объёмом двигателя 
{person.engine} количество мест {person.seats} имеет максимальную скорость - {person.topSpead} км/ч""")

    person = Vehicle('mercedes-benz', 'sprinter ii', "3", "19", "170")
    print(f""""Автобус {person.manufacturer} {person.model} с объёмом двигателя 
{person.engine} количество мест {person.seats} имеет максимальную скорость - {person.topSpead} км/ч""")
