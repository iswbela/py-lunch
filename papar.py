import pywhatkit,time
from random import randint
from datetime import datetime

class Pasta():
        def __init__(self, path, max) -> None:
                self.path = path
                self.max = max

        def pickRandom(self):
                random = randint(1, self.max)
                return f"{self.path}\img{random}.jpeg"

lanche = Pasta("lanche", 3)
almoco = Pasta("almoco", 10)

def papar(arquivo):
        #manda grupo ti
        pywhatkit.sendwhats_image("D40Zhtd0nkk9i79WtwaRcV", arquivo)
        print("Imagem enviada com sucesso.")
        time.sleep(10000)

while True:
        data = datetime.now()
        hora = data.hour
        minuto = data.minute

        if hora >= 11 and hora < 13 or hora == 13 and minuto < 30:
                papar(almoco.pickRandom())
        elif hora >= 16 and minuto < 30:
                papar(lanche.pickRandom())
        else:
                print('(',hora,':',minuto,')','Ainda não é horário. Aguardando 60 segundos.')
        time.sleep(60)

