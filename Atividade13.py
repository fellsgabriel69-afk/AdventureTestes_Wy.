# Registro de Logs
from datetime import datetime

ARQUIVO_LOG = "app.log"
TIPOS_VALIDOS = ("INFO", "WARNING", "ERROR")


def registrar_log(tipo, mensagem):
    if tipo not in TIPOS_VALIDOS:
        print(f"Tipo inválido. Use: {', '.join(TIPOS_VALIDOS)}")
        return

    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    registro = f"[{timestamp}] [{tipo}] {mensagem}\n"

    with open(ARQUIVO_LOG, "a", encoding="utf-8") as arquivo:
        arquivo.write(registro)

    print(f"Log registrado: {registro.strip()}")


print("\n--- Registro de Logs ---")
print(f"As mensagens serão salvas em '{ARQUIVO_LOG}'")
print(f"Tipos disponíveis: {', '.join(TIPOS_VALIDOS)}")
print("Digite 'sair' na mensagem para encerrar.\n")

while True:
    tipo = input("Tipo do log (INFO/WARNING/ERROR): ").strip().upper()
    mensagem = input("Mensagem do log: ").strip()

    if mensagem.lower() == "sair":
        print("\nEncerrando o programa.")
        break

    if not mensagem:
        print("A mensagem não pode estar vazia.\n")
        continue

    registrar_log(tipo, mensagem)
    print()
