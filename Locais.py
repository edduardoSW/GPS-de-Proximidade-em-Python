from geopy.distance import geodesic
from gerar_mapa import gerar_rota

print("GPS de Proximidade")

lugares = {
    "padaria": (-20.1885852, -40.2612495),
    "praca": (-20.1876121, -40.2579621),
    "shopping": (-20.1931374, -40.2663088),
    "faculdade": (-20.1923158, -40.2619206),
    "supermercado": (-20.1928536, -40.2651829),
    "terminal": (-20.1936359, -40.2554279)
}

while True:
    local = input("Onde você está? ").lower().strip()

    if local == "sair":
        break

    if local in lugares:
        posicao = lugares[local]
        menor_distancia = float("inf")
        lugar_mais_proximo = ""

        for lugar, coord in lugares.items():
            if lugar != local:
                distancia = geodesic(posicao, coord).km
                print(f"Distância até {lugar}: {distancia:.2f} km")

                if distancia < menor_distancia:
                    menor_distancia = distancia
                    lugar_mais_proximo = lugar

        print("-" * 30)
        print(f"O lugar mais próximo de você é: {lugar_mais_proximo}")


        gerar_rota(lugares, local, lugar_mais_proximo)
    else:
        print("Local não encontrado")