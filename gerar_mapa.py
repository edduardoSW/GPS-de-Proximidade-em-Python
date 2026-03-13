import folium
import webbrowser
import os


def gerar_rota(lugares, local, lugar_mais_proximo):
    posicao_inicial = lugares[local]
    mapa = folium.Map(location=posicao_inicial, zoom_start=16)

    folium.Marker(
        posicao_inicial,
        popup=f"Você está aqui: {local.capitalize()}",
        icon=folium.Icon(color='blue', icon='user')
    ).add_to(mapa)

    posicao_destino = lugares[lugar_mais_proximo]
    folium.Marker(
        posicao_destino,
        popup=f"Local Mais Próximo: {lugar_mais_proximo.capitalize()}",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(mapa)

    caminho = [posicao_inicial, posicao_destino]
    folium.PolyLine(caminho, color="blue", weight=5, opacity=0.7).add_to(mapa)

    for l, coord in lugares.items():
        if l != local and l != lugar_mais_proximo:
            folium.Marker(coord, popup=l.capitalize()).add_to(mapa)

    nome_arquivo = "mapa.html"
    mapa.save(nome_arquivo)
    webbrowser.open('file://' + os.path.realpath(nome_arquivo))