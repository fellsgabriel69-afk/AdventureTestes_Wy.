# Web Scraper Simples — títulos de notícias do G1
from datetime import datetime

import requests
from bs4 import BeautifulSoup

URL_G1 = "https://g1.globo.com/"
ARQUIVO_SAIDA = "titulos_noticias.txt"
SELETOR_TITULOS = "a.feed-post-link"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def buscar_pagina(url):
    """
    Faz uma requisição HTTP GET à URL informada e retorna o HTML da página.
    Usa timeout e cabeçalhos para simular um navegador e evitar bloqueios.
    """
    resposta = requests.get(url, headers=HEADERS, timeout=15)
    resposta.raise_for_status()
    return resposta.text


def extrair_titulos(html):
    """
    Analisa o HTML com BeautifulSoup e coleta os títulos das notícias.
    Busca links com a classe 'feed-post-link' e remove duplicatas.
    """
    soup = BeautifulSoup(html, "html.parser")
    titulos = []

    for link in soup.select(SELETOR_TITULOS):
        texto = link.get_text(strip=True)
        if texto and texto not in titulos:
            titulos.append(texto)

    return titulos


def salvar_titulos(titulos, caminho, data_coleta):
    """
    Grava os títulos em um arquivo de texto, incluindo fonte, data/hora
    da coleta e a quantidade de notícias encontradas.
    """
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Fonte: {URL_G1}\n")
        arquivo.write(f"Coleta realizada em: {data_coleta}\n")
        arquivo.write(f"Total de títulos: {len(titulos)}\n")
        arquivo.write("-" * 60 + "\n\n")
        for indice, titulo in enumerate(titulos, start=1):
            arquivo.write(f"{indice}. {titulo}\n")


def main():
    """
    Orquestra o scraper: baixa a página, extrai títulos, salva no arquivo
    e exibe o resultado no terminal. Trata erros de rede e HTTP.
    """
    print("\n--- Web Scraper Simples (G1) ---\n")
    print(f"Buscando notícias em {URL_G1} ...")

    try:
        html = buscar_pagina(URL_G1)
        titulos = extrair_titulos(html)

        if not titulos:
            print("Nenhum título encontrado. O layout do site pode ter mudado.")
            return

        data_coleta = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        salvar_titulos(titulos, ARQUIVO_SAIDA, data_coleta)
        print(f"{len(titulos)} título(s) extraído(s) e salvos em '{ARQUIVO_SAIDA}'.")
        print(f"Data da coleta: {data_coleta}\n")

        for indice, titulo in enumerate(titulos, start=1):
            print(f"{indice}. {titulo}")

    except requests.exceptions.ConnectionError:
        print("Erro de conexão: não foi possível conectar ao site. Verifique sua internet.")
    except requests.exceptions.Timeout:
        print("Erro de conexão: o site demorou demais para responder (timeout).")
    except requests.exceptions.HTTPError as erro:
        print(f"Erro HTTP: o servidor retornou um status inválido ({erro}).")
    except requests.exceptions.RequestException as erro:
        print(f"Erro na requisição: {erro}")


if __name__ == "__main__":
    main()
