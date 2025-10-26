import os
import json
import pdfkit
import time
from datetime import datetime
from termcolor import colored

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

    sobre = input(colored("Digite uma breve descrição sobre você: ", "light_red", attrs=['bold']))

    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored("Preencimento de Curriculo - Experiencia Profissional", "magenta", attrs=['bold']).center(90))

    experiencias = []

    while True:
        empresa = input(colored("\nDigite o nome da empresa (""/toleave): ", "light_red", attrs=['bold']))

        if empresa.strip() != "":
            cargos = input(colored("Digite o cargo na empresa: ", "light_red", attrs=['bold']))
            print(colored("Digite a data de início da experiência:", "yellow", attrs=['bold']))
            data_inicio = validar_data()
            print(colored("Digite a data de término da experiência (ou deixe em branco se ainda estiver trabalhando lá):", "yellow", attrs=['bold']))
            data_saida = validar_data()
            descricao = input(colored("Descreva suas responsabilidades e conquistas nessa empresa: ", "light_red", attrs=['bold']))
            experiencias.append({"empresa": empresa, "cargo": cargos, "data_inicio": data_inicio, "data_fim": data_saida, "descricao": descricao})

        else:
            break

    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored("Preencimento de Curriculo - Cursos e Formações", "magenta", attrs=['bold']).center(90))

    formacao = []
    while True:
        curso = input(colored("\nDigite sua formacao ou curso realizado: ", "light_red", attrs=['bold']))
        if curso.strip() != "":

            instituicao = input(colored("Digite a instituição onde realizou o curso: ", "light_red", attrs=['bold']))

            try:
                ano_conclusao = int(input(colored("Digite o ano de conclusão do curso (ou deixe em branco se ainda estiver cursando): ", "light_red", attrs=['bold'])))
            except ValueError:
                ano_conclusao = ""

            formacao.append({"curso": curso, "instituicao": instituicao, "ano_fim": ano_conclusao})

        
        else:
            break

    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored("Preencimento de Curriculo - Habilidades", "magenta", attrs=['bold']).center(90))

    habilidades = []
    while True:
        habilidades = input(colored("Digite suas habilidades (separadas por vírgula): ", "light_red", attrs=['bold']))
        if habilidades.strip() != "":
            habilidades = [habilidade.strip() for habilidade in habilidades.split(",")]
            break
        else:
            print(colored("As habilidades não podem estar vazias.", "red"))

    vCurriculos[nome] = {

        "nome": nome,
        "email": email,
        "telefone": telefone,
        "experiencias": experiencias,

        "sobre": sobre,
        "formacao": formacao,
        "habilidades": habilidades
    }

    save("curriculos.json", vCurriculos)
    print(colored("Currículo preenchido com sucesso!", "green"))
    time.sleep(1)

def curriculo_pdf(vCurriculos,nome):
    chave = procurar_curriculo(vCurriculos,nome)
    if chave == -1:
        print("Currículo não encontrado.")
        return 0;

    curriculo = vCurriculos[chave]

#region HTML Template

    texto = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Currículo - {curriculo['nome']}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f9;
            color: #333;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #2980b9;
            padding-bottom: 5px;
        }}
        h2 {{
            color: #2980b9;
            margin-top: 30px;
        }}
        p {{
            margin: 5px 0;
        }}
        .section {{
            margin-bottom: 20px;
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .experiencia {{
            margin-bottom: 15px;
        }}
        .skills, .formacao {{
            list-style: none;
            padding: 0;
        }}
        .skills li, .formacao li {{
            background: #eaf2f8;
            margin: 5px 0;
            padding: 8px;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <h1>{curriculo['nome']}</h1>
    <h3>{curriculo['email']} | {curriculo['telefone']}</h3>

    <div class="section">
        <h2>Sobre</h2>
        <p>{curriculo['sobre']}</p>
    </div>

    <div class="section">
        <h2>Experiências Profissionais</h2>"""

    for exp in curriculo['experiencias']:
        texto += f"""
        <div class="experiencia">
            <p><strong>Empresa:</strong> {exp['empresa']}</p>
            <p><strong>Cargo:</strong> {exp['cargo']}</p>
            <p><strong>Período:</strong> {exp['data_inicio']} - {exp.get('data_fim', 'Atual')}</p>
            <p><strong>Descrição:</strong> {exp.get('descricao', '—')}</p>
        </div>"""

    texto += """
    </div>
    <div class="section">
        <h2>Formação Acadêmica</h2>
        <ul class="formacao">"""
    for curso in curriculo.get('formacao', []):
        texto += f"<li>{curso['curso']} - {curso['instituicao']} ({curso.get('ano_fim', 'Cursando')})</li>"
    texto += """</ul>
    </div>
    <div class="section">
        <h2>Habilidades</h2>
        <ul class="skills">"""
    for skill in curriculo.get('habilidades', []):
        texto += f"<li>{skill}</li>"
    texto += """</ul>
    </div>
</body>
</html>"""

#endregion
#region PDF Generation
    
    print("Convertendo para pdf...")
    time.sleep(3)
    try:
        os.makedirs("Curriculos-PDF", exist_ok=True)
        caminho_arquivo = os.path.join("Curriculos-PDF", f"Curriculo-{curriculo['nome']}.pdf")
        config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
        pdfkit.from_string(texto, caminho_arquivo, configuration=config)

        print(colored("Currículo gerado com sucesso!", "green"))
        print(colored("O arquivo foi salvo em:" + os.getcwd(), "yellow"))
        time.sleep(1)

    except Exception as e:
        print(colored(f"Erro ao gerar Curriculo!{e}", "red"))
        time.sleep(1)

#endregion

def procurar_curriculo(vCurriculos,nome):
    if nome in vCurriculos:
        return nome
    else:
        return -1

def atualizar_curriculo(vCurriculos,nome):
    chave = procurar_curriculo(vCurriculos,nome)
    if chave == -1:
        print(colored("Currículo não encontrado.", "red"))
        return 0;
    else:
        print(colored("Currículo encontrado.", "green"))
        print("Você deseja alterar:\n\t 1 - Nome\n\t 2 - Email\n\t 3 - Telefone\n\t 4 - Sobre\n\t 5 - Experiência")
        opcao = opcoes()

        if opcao == "1":
            vCurriculos[chave]["nome"] = validar_nome(vCurriculos)
            print(colored("Nome alterado com sucesso!", "green"))
            save("curriculos.json", vCurriculos)
            time.sleep(1)

        if opcao == "2":
            vCurriculos[chave]["email"] = validar_email(vCurriculos)
            print(colored("Email alterado com sucesso!", "green"))
            save("curriculos.json", vCurriculos)
            time.sleep(1)

        if opcao == "3":
            vCurriculos[chave]["telefone"] = validar_telefone(vCurriculos)
            print(colored("Telefone alterado com sucesso!", "green"))
            save("curriculos.json", vCurriculos)
            time.sleep(1)

        if opcao == "4":
            vCurriculos[chave]["sobre"] = input(colored("Digite uma breve descrição sobre você: ", "light_red", attrs=['bold']))
            print(colored("Sobre alterado com sucesso!", "green"))
            save("curriculos.json", vCurriculos)
            time.sleep(1)


        if opcao == "5":
            experiencias = []
            while True:
                empresa = input(colored("Digite o nome da empresa (ou 'sair' para encerrar): ", "light_red", attrs=['bold']))
                if empresa.lower() == 'sair':
                    break
                cargos = input(colored("Digite o cargo na empresa: ", "light_red", attrs=['bold']))
                data_inicio = validar_data()
                experiencias.append({"empresa": empresa, "cargo": cargos, "data_inicio": data_inicio})

            vCurriculos[chave]["experiencias"] = experiencias

            print("Experiencia Alterada com sucesso!")
            save("curriculos.json", vCurriculos)
            time.sleep(1)


def listar_curriculos(vCurriculos):
    for nome, curriculo in vCurriculos.items():
        print(colored("Nome: ", "magenta"), colored(f"{curriculo['nome']}", "cyan", attrs=['bold']))

    input(colored("\nPressione Enter para continuar...", "yellow"))

#endregion

#region  /Validações/

def validar_nome(vCurriculos):
    while True:
        nome = input(colored("Digite o nome completo: ", "light_red", attrs=['bold']))
        if nome.replace(" ", "").isalpha() and nome not in vCurriculos:
            return nome
        else:
            if nome in vCurriculos:
                print(colored("Nome já existe.", "red"))
            print(colored("O nome deve conter apenas letras.", "red"))

def validar_nome_busca():
    while True:
        nome = input(colored("Digite o nome completo: ", "light_red", attrs=['bold']))
        if nome.replace(" ", "").isalpha():
            return nome
        else:
            print(colored("O nome deve conter apenas letras.", "red"))

def validar_email():
    while True:
        email = input(colored("Digite o email: ", "light_red", attrs=['bold']))
        if "@" in email and "." in email:
            return email
        else:
            print(colored("O email deve conter '@' e '.'.", "red"))

def validar_telefone():
    while True:
        telefone = input(colored("Digite o telefone: ", "light_red", attrs=['bold'])).strip()
        if telefone.isdigit() and len(telefone) == 11:
            telefone = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
            return telefone
        else:
            print(colored("O telefone deve conter apenas números.", "red"))

def validar_data():
    while True:
        data = input(colored("Digite a data (DD/MM/AAAA): ", "light_red", attrs=['bold']))
        try:
            hoje = datetime.now().date()
            data_nascimento = datetime.strptime(data, "%d/%m/%Y").date()
            if data_nascimento > hoje:
                print(colored("Data inválida. A data não pode ser no futuro.", "red"))

            else:
                return str(data_nascimento)

        except ValueError:
            print(colored("Data inválida. Use o formato DD/MM/AAAA.", "red"))



#endregion

#region /Funções de Menu/
def menu():
   
    print(colored("Sistema de Currículos\n", "magenta", "on_black", attrs=['bold']).center(110))

    print("1. Preencher Currículo".center(90))
    print("2. Listar Currículos".center(90))
    print("3. Procurar Currículos".center(90))
    print("4. Atualizar Currículos".center(90))
    print("5. Gerar PDF do Currículo".center(90))
    print("6. Sair".center(90))

def opcoes():
    opcao = input(colored(">> ", "light_red", attrs=['bold']))
    while opcao not in ["1","2","3","4","5","6"]: opcao = input(colored("Invalid Input\n>> ", "red", attrs=['bold']))
    return opcao

#endregion

def main():
    vCurriculos = load("curriculos.json")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        menu()
        opcao = opcoes()

        match opcao:
            case "1":
                    
                os.system('cls' if os.name == 'nt' else 'clear')
                print(colored("Preencimento de Curriculo - Dados Pessoais", "magenta", attrs=['bold']).center(90))
                nome = validar_nome(vCurriculos)
                preencher_curriculo(vCurriculos, nome)



            case "2":
                
                print(colored("Lista de Currículos", "magenta", attrs=['bold']).center(90))
                print("\n")
                listar_curriculos(vCurriculos)
 

            case "3":
                print(colored("Procurar Currículo", "magenta", attrs=['bold']).center(90))
                print("\n")
                nome = validar_nome_busca()
                codigo = procurar_curriculo(vCurriculos,nome)
                if codigo != -1:
                    print(colored(f"Nome:", "light_red", attrs=['bold']), colored(f"{vCurriculos[codigo]['nome']}", "cyan", attrs=['bold']))
                    print(colored(f"Email:", "light_red", attrs=['bold']), colored(f"{vCurriculos[codigo]['email']}", "cyan", attrs=['bold']))
                    print(colored(f"Telefone:", "light_red", attrs=['bold']), colored(f"{vCurriculos[codigo]['telefone']}", "cyan", attrs=['bold']))
                else:
                    print(colored("Currículo não encontrado.", "red"))


                op = input("Deseja Gerar um PDF do Curriculo? (S/N)")
                while op.upper() != "S" and op.upper() != "N": op = input(colored("Deseja Gerar um PDF do Curriculo? (S/N)", "yellow"))

                if op.upper() == "S":
                    curriculo_pdf(vCurriculos,nome)
                else:
                    print(colored("Voltando ao menu...", "yellow"))

            case "4":
                print(colored("Atualizar Currículo", "magenta", attrs=['bold']).center(90))
                print("=" * 30)
                nome = validar_nome_busca()
                atualizar_curriculo(vCurriculos,nome)

            case "5":
                print(colored("Gerar PDF do Currículo", "magenta", attrs=['bold']).center(90))

                nome = validar_nome_busca()
                codigo = procurar_curriculo(vCurriculos,nome)

                if codigo != -1:
                    curriculo_pdf(vCurriculos,nome)
                else:
                    print(colored("Currículo não encontrado.", "red"))

            case "6":
                print(colored("Saindo do programa...", "yellow"))
                break

main()
