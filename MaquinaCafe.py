import unittest

class Maquinita:
    def __init__(self):
        self.money = 0
        self.cafe = 30
        self.leche = 50
        self.azucar = 20
        self.chocolate = 50
        self.matrizTodoPoderosa =  [[1 ,10,0 ,0 ,0 ],
                                    [2 ,20,0 ,0 ,0 ],
                                    [5 ,10,30,0 ,0 ],
                                    [6 ,20,30,0 ,0 ],
                                    [10,0 ,0 ,5 ,50],
                                    [15,20,0 ,5 ,50],
                                    [4 ,0 ,0 ,0 ,0 ]]

    def pedir(self, opcion, coins):
        # Verificaciones de que la maquina tiene todos los ingredientes...
        if self.matrizTodoPoderosa [opcion][0] != coins:
            raise Exception("Needs {} coins".format(self.matrizTodoPoderosa [opcion][0]))
        elif self.matrizTodoPoderosa[opcion][1] > self.cafe:
            raise Exception("Machine needs more coffe")
        elif self.matrizTodoPoderosa[opcion][2] > self.leche:
            raise Exception("Machine needs more milk")
        elif self.matrizTodoPoderosa[opcion][3] > self.azucar:
            raise Exception("Machine needs more sugar")
        elif self.matrizTodoPoderosa[opcion][4] > self.chocolate:
            raise Exception("Machine needs more chocolate")
        # Si los tiene, procede a hacer el pedido
        else:
            self.cafe -= self.matrizTodoPoderosa[opcion][1]
            self.leche -= self.matrizTodoPoderosa[opcion][2]
            self.azucar -= self.matrizTodoPoderosa[opcion][3]
            self.chocolate -= self.matrizTodoPoderosa[opcion][4]
            self.money += coins
            return True

    def ponerAzucar(self, cant, coins):
        if cant > 30:
            raise Exception("Exced limit of sugar")
        elif cant > self.azucar:
            raise Exception("Machine needs more sugar")
        elif 5*coins < cant:
            raise Exception("Needs more coins, one each 5g of sugar")
        else:
            self.azucar -= cant
            self.money += coins
            return True
    
    def opciones(self):
        opciones = {0: "CafeSolo", 1: "CafeDoble", 2: "CafeLecheSolo", 3: "CafeLecheDoble", 4: "Chocolate", 5: "Capuchino", 6: "Te"}
        return opciones


