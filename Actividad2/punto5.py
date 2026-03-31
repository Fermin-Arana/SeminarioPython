from abc import ABC, abstractmethod

class Zones(ABC):

    @abstractmethod
    def final_price(self,kg):
        pass

class Local(Zones):
    def final_price(self,kg):
        price = 0
        if(kg < 1):
            price = 500
        if (kg >= 1 and kg <= 5):
            price = 1000
        if (kg > 5):
            price = 2000
        print(f"El precio final es ${price}")
    
class Regional(Zones):
    def final_price(self,kg):
        price = 0
        if(kg < 1):
            price = 1000
        if (kg >= 1 and kg <= 5):
            price = 2500
        if (kg > 5):
            price = 4500
        print(f"El precio final es ${price}")
    
class Nacional(Zones):
    def final_price(self,kg):
        price = 0
        if(kg < 1):
            price = 2000
        if (kg >= 1 and kg <= 5):
            price = 4500
        if (kg > 5):
            price = 8000
        print(f"El precio final es ${price}")
    
class Other(Zones):
    def final_price(self, kg):
        print(f"Esta zona no es valida y sus {kg} kilos no pueden ser calculados")

delivery_kg = int(input("Ingrese los KG de su pedido "))
delivery_zone = input("Ingrese la zona de su pedido (Local, Regional y Nacional) ").lower()
while True:
    match delivery_zone:
        case "local":
            zona = Local()
        case "regional":
            zona = Regional()
        case "nacional":
            zona = Nacional()
        case _:
            zona = Other()

    zona.final_price(delivery_kg)
    opcion = input ("Desea calcular otro pedido? (S/N) ")
    if (opcion.lower() != "s"):
        print(f"Hasta la proxima")
        break
    delivery_kg = int(input("Ingrese los KG de su pedido "))
    delivery_zone = input("Ingrese la zona de su pedido (Local, Regional y Nacional) ").lower()

        

    