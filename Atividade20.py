# Jogo da Forca (POO)
import random

PALAVRAS_PADRAO = (
    "python",
    "programacao",
    "orientacao",
    "objetos",
    "algoritmo",
    "estrutura",
    "variavel",
    "funcao",
    "classe",
    "metodo",
)


class Palavra:
    def __init__(self, texto):
        self._texto = texto.strip().lower()
        self._letras_descobertas = set()

    @property
    def texto(self):
        return self._texto

    @property
    def completa(self):
        return all(letra in self._letras_descobertas for letra in self._texto)

    def tentar_letra(self, letra):
        letra = letra.lower()
        if len(letra) != 1 or not letra.isalpha():
            return None
        if letra in self._letras_descobertas:
            return None
        self._letras_descobertas.add(letra)
        return letra in self._texto

    def exibir(self):
        partes = []
        for letra in self._texto:
            if letra in self._letras_descobertas:
                partes.append(letra.upper())
            else:
                partes.append("_")
        return " ".join(partes)


class Jogador:
    def __init__(self, nome):
        self.nome = nome.strip() or "Jogador"
        self._tentativas = []

    @property
    def tentativas(self):
        return list(self._tentativas)

    def registrar_tentativa(self, letra):
        letra = letra.lower()
        if len(letra) != 1 or not letra.isalpha():
            return False
        if letra in self._tentativas:
            return False
        self._tentativas.append(letra)
        return True

    def ja_tentou(self, letra):
        return letra.lower() in self._tentativas


class Jogo:
    MAX_ERROS = 6

    def __init__(self, palavra, jogador):
        self.palavra = palavra
        self.jogador = jogador
        self._erros = 0
        self._encerrado = False
        self._venceu = False

    @property
    def erros(self):
        return self._erros

    @property
    def tentativas_restantes(self):
        return self.MAX_ERROS - self._erros

    @property
    def encerrado(self):
        return self._encerrado

    @property
    def venceu(self):
        return self._venceu

    def processar_letra(self, letra):
        if self._encerrado:
            return "encerrado"

        if not self.jogador.registrar_tentativa(letra):
            if len(letra.strip()) != 1 or not letra.strip().isalpha():
                return "invalida"
            return "repetida"

        acertou = self.palavra.tentar_letra(letra)
        if acertou is None:
            return "invalida"

        if not acertou:
            self._erros += 1

        if self.palavra.completa:
            self._encerrado = True
            self._venceu = True
            return "vitoria"

        if self._erros >= self.MAX_ERROS:
            self._encerrado = True
            self._venceu = False
            return "derrota"

        return "acerto" if acertou else "erro"

    def exibir_forca(self):
        etapas = [
            "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
        ]
        indice = min(self._erros, len(etapas) - 1)
        return etapas[indice]

    def exibir_estado(self):
        print(f"\nJogador: {self.jogador.nome}")
        print(f"Palavra: {self.palavra.exibir()}")
        print(f"Tentativas: {', '.join(t.upper() for t in self.jogador.tentativas) or '(nenhuma)'}")
        print(f"Erros: {self._erros}/{self.MAX_ERROS} | Restantes: {self.tentativas_restantes}")
        print(self.exibir_forca())


def escolher_palavra():
    print("\nPalavras disponíveis:")
    for indice, palavra in enumerate(PALAVRAS_PADRAO, start=1):
        print(f"  {indice}. {'_' * len(palavra)} ({len(palavra)} letras)")

    while True:
        opcao = input("\nEscolha o número da palavra (ou Enter para aleatória): ").strip()
        if not opcao:
            return random.choice(PALAVRAS_PADRAO)
        if opcao.isdigit() and 1 <= int(opcao) <= len(PALAVRAS_PADRAO):
            return PALAVRAS_PADRAO[int(opcao) - 1]
        print("Opção inválida. Tente novamente.")


def main():
    print("\n--- Jogo da Forca (POO) ---\n")

    nome = input("Digite seu nome: ").strip()
    jogador = Jogador(nome)

    texto = escolher_palavra()
    palavra = Palavra(texto)
    jogo = Jogo(palavra, jogador)

    print(f"\nBem-vindo(a), {jogador.nome}! Você tem {Jogo.MAX_ERROS} tentativas.")
    print("Digite uma letra por vez. Digite 'sair' para encerrar.\n")

    while not jogo.encerrado:
        jogo.exibir_estado()
        entrada = input("\nDigite uma letra: ").strip().lower()

        if entrada == "sair":
            print("\nJogo encerrado pelo jogador.")
            print(f"A palavra era: {palavra.texto.upper()}")
            return

        resultado = jogo.processar_letra(entrada)

        if resultado == "invalida":
            print("Entrada inválida. Informe apenas uma letra do alfabeto.")
        elif resultado == "repetida":
            print("Você já tentou essa letra.")
        elif resultado == "acerto":
            print("Boa! Letra correta.")
        elif resultado == "erro":
            print("Letra incorreta.")
        elif resultado == "vitoria":
            jogo.exibir_estado()
            print(f"\nParabéns, {jogador.nome}! Você venceu!")
            print(f"A palavra era: {palavra.texto.upper()}")
            return
        elif resultado == "derrota":
            jogo.exibir_estado()
            print(f"\nFim de jogo, {jogador.nome}. Você perdeu.")
            print(f"A palavra era: {palavra.texto.upper()}")
            return


if __name__ == "__main__":
    main()
