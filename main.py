import os
import json
import pdfkit
import time
from datetime import datetime

#region /salvamento/
def save(nome_arquivo, dados):
    try:
        os.makedirs("Backup-Curriculos", exist_ok=True)
        nome_arquivo = os.path.join("Backup-Curriculos", nome_arquivo)

        with open(nome_arquivo, 'w') as file:
            json.dump(dados, file, indent=4)
            print("Currículos salvos com sucesso!")
            time.sleep(1)


    except Exception as e:
        print(f"Erro ao salvar os currículos: {e}")
        time.sleep(1)

def load(nome_arquivo):
    try:
        nome_arquivo = os.path.join("Backup-Curriculos", nome_arquivo)
        with open(nome_arquivo, 'r') as file:
            return json.load(file)

    except FileNotFoundError:
        return {}
#endregion

#region /Funções do Programa/
def preencher_curriculo(vCurriculos, nome):
    email = validar_email()
    telefone = validar_telefone()
    sobre = input("Digite uma breve descrição sobre você: ")
    experiencias = []
    while True:
        empresa = input("Digite o nome da empresa (ou 'sair' para encerrar): ")
        if empresa.lower() == 'sair':
            break
        cargos = input("Digite o cargo na empresa: ")
        data_inicio = validar_data()
        experiencias.append({"empresa": empresa, "cargo": cargos, "data_inicio": data_inicio})

    vCurriculos[nome] = {

        "nome": nome,
        "email": email,
        "telefone": telefone,
        "experiencias": experiencias,

        "sobre": sobre
    }

    save("curriculos.json", vCurriculos)

def curriculo_pdf(vCurriculos,nome):
    chave = procurar_curriculo(vCurriculos,nome)
    if chave == -1:
        print("Currículo não encontrado.")
        return 0;

    curriculo = vCurriculos[chave]

    texto = f"<h1>Nome: {curriculo['nome']}</h1>"
    texto += f"<h2>Email: {curriculo['email']}</h2>"
    texto += f"<h2>Telefone: {curriculo['telefone']}</h2>"
    texto += f"<h2>Sobre</h2><p>{curriculo['sobre']}</p>"
    texto += "<h2>Experiências Profissionais</h2>"

    for experiencia in curriculo['experiencias']:
        texto += f"<p>Empresa: {experiencia['empresa']}</p>"
        texto += f"<p>Cargo: {experiencia['cargo']}</p>"
        texto += f"<p>Data de Início: {experiencia['data_inicio']}</p>"

    texto += "<br>"
    print("Convertendo para pdf...")
    time.sleep(3)
    os.makedirs("Curriculos-PDF", exist_ok=True)
    caminho_arquivo = os.path.join("Curriculos-PDF", f"Curriculo-{curriculo['nome']}.pdf")
    pdfkit.from_string(texto, caminho_arquivo)
    print("Currículo gerado com sucesso!")
    print("O arquivo foi salvo em:" + os.getcwd())
    time.sleep(1)

def procurar_curriculo(vCurriculos,nome):
    if nome in vCurriculos:
        return nome
    else:
        return -1

def atualizar_curriculo(vCurriculos,nome):
    chave = procurar_curriculo(vCurriculos,nome)
    if chave == -1:
        print("Currículo não encontrado.")
        return 0;
    else:
        print("Currículo encontrado.")
        print("Você deseja alterar:\n\t 1 - Nome\n\t 2 - Email\n\t 3 - Telefone\n\t 4 - Sobre\n\t 5 - Experiência")
        opcao = opcoes()

        if opcao == "1":
            vCurriculos[chave]["nome"] = validar_nome(vCurriculos)
            print("Nome alterado com sucesso!")
            save("curriculos.json", vCurriculos)
            time.sleep(1)

        if opcao == "2":
            vCurriculos[chave]["email"] = validar_email(vCurriculos)
            print("Email alterado com sucesso!")
            save("curriculos.json", vCurriculos)
            time.sleep(1)

        if opcao == "3":
            vCurriculos[chave]["telefone"] = validar_telefone(vCurriculos)
            print("Telefone alterado com sucesso!")
            save("curriculos.json", vCurriculos)
            time.sleep(1)

        if opcao == "4":
            vCurriculos[chave]["sobre"] = input("Digite uma breve descrição sobre você: ")
            print("Sobre alterado com sucesso!")
            save("curriculos.json", vCurriculos)
            time.sleep(1)


        if opcao == "5":
            experiencias = []
            while True:
                empresa = input("Digite o nome da empresa (ou 'sair' para encerrar): ")
                if empresa.lower() == 'sair':
                    break
                cargos = input("Digite o cargo na empresa: ")
                data_inicio = validar_data()
                experiencias.append({"empresa": empresa, "cargo": cargos, "data_inicio": data_inicio})

            vCurriculos[chave]["experiencias"] = experiencias

            print("Experiencia Alterada com sucesso!")
            save("curriculos.json", vCurriculos)
            time.sleep(1)


def listar_curriculos(vCurriculos):
    for nome, curriculo in vCurriculos.items():
        print(f"Nome: {curriculo['nome']}")
#endregion

#region  /Validações/

def validar_nome(vCurriculos):
    while True:
        nome = input("Digite o nome completo: ")
        if nome.replace(" ", "").isalpha() and nome not in vCurriculos:
            return nome
        else:
            if nome in vCurriculos:
                print("Nome já existe.")
            print("O nome deve conter apenas letras.")

def validar_nome_busca():
    while True:
        nome = input("Digite o nome completo: ")
        if nome.replace(" ", "").isalpha():
            return nome
        else:
            print("O nome deve conter apenas letras.")

def validar_email(vCurriculos):
    while True:
        email = input("Digite o email: ")
        if "@" in email and "." in email:
            return email
        else:
            print("O email deve conter '@' e '.'.")

def validar_telefone(vCurriculos):
    while True:
        telefone = input("Digite o telefone: ").strip()
        if telefone.isdigit() and len(telefone) == 11:
            telefone = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
            return telefone
        else:
            print("O telefone deve conter apenas números.")

def validar_data():
    while True:
        data = input("Digite a data (DD/MM/AAAA): ")
        try:
            hoje = datetime.now().date()
            data_nascimento = datetime.strptime(data, "%d/%m/%Y").date()
            if data_nascimento > hoje:
                print("Data inválida. A data não pode ser no futuro.")

            else:
                return data_nascimento

        except ValueError:
            print("Data inválida. Use o formato DD/MM/AAAA.")



#endregion

#region /Finções de Menu/
def menu():
    print("Sistema de Currículos")
    print("1. Preencher Currículo")
    print("2. Listar Currículos")
    print("3. Procurar Currículos")
    print("4. Atualizar Currículos")
    print("5. Sair")

def opcoes():
    opcao = input("Escolha uma opção: ")
    while opcao not in ["1","2","3","4","5"]: opcao = input("Opção Invalida\nEscolha uma opção: ")
    return opcao

#endregion

def main():
    vCurriculos = load("curriculos.json")

    while True:
        print("\n", "=" * 30)
        menu()
        print("=" * 30)
        opcao = opcoes()

        if opcao == "1":
            print("\n\t-=-Cadastro de Curriculo-=-")
            print("=" * 30)
            nome = validar_nome(vCurriculos)
            preencher_curriculo(vCurriculos, nome)
            print("=" * 30)

            continue

        if opcao == "2":
            print("\n\t-=-Lista de Currículos-=-")
            print("=" * 30)
            listar_curriculos(vCurriculos)
            print("=" * 30)

            continue

        if opcao == "3":
            print("\n\t-=-Procurar Currículo-=-")
            print("=" * 30)
            nome = validar_nome_busca()
            codigo = procurar_curriculo(vCurriculos,nome)
            if codigo != -1:
                print(f"Nome: {vCurriculos[codigo]['nome']}")
                print(f"Email: {vCurriculos[codigo]['email']}")
                print(f"Telefone: {vCurriculos[codigo]['telefone']}")
            else:
                print("Currículo não encontrado.")
            print("=" * 30)

            op = input("Deseja Gerar um PDF do Curriculo? (S/N)")
            while op.upper() != "S" and op.upper() != "N": op = input("Deseja Gerar um PDF do Curriculo? (S/N)")

            if op.upper() == "S":
                curriculo_pdf(vCurriculos,nome)
            else:
                print("Voltando ao menu...")
                time.sleep(1)

            continue

        if opcao == "4":
            print("\n\t-=-Atualizar Currículo-=-")
            print("=" * 30)
            nome = validar_nome_busca()
            atualizar_curriculo(vCurriculos,nome)
            print("=" * 30)

            continue

        if opcao == "5":
            print("Saindo do programa...")
            break

main()
