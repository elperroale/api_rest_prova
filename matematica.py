import math 

def triangolo_ipotenusa(cateto_a, cateto_b):
    somma_quadrati = (cateto_a ** 2) + (cateto_b ** 2)
    return math.sqrt(somma_quadrati)

def area_triangolo(base, altezza):
    return (base * altezza) / 2

def cerchio(raggio):
    area = math.pi * (raggio ** 2)
    circonferenza = 2 * math.pi * raggio
    return {
        "area": round(area, 2),
        "circonferenza": round(circonferenza, 2)
    }

def quadrato(lato):
    return lato ** 2