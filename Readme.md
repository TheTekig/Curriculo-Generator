# Gerador Curriculos

Um sistema simples em Python para criar, gerenciar e exportar currículos em PDF diretamente do terminal.

## 📌 Funcionalidades

    - Cadastro de currículos com:

        - Nome
        - Email
        - Telefone
        - Experiências profissionais
        - Texto de apresentação ("Sobre")
        - Listagem de currículos salvos
        - Busca por nome
        - Atualização de dados
        - Exportação do currículo em **PDF**
        - Armazenamento local em JSON
        - Backup automático de dados

## 🛠️ Tecnologias utilizadas

        - Python 3.x
        - [pdfkit](https://pypi.org/project/pdfkit/)
        - JSON para persistência de dados
        - HTML básico para estilização do PDF

## 🧱 Pré-requisitos

        - Python 3 instalado
        - Instalar dependência:
        - pip install pdfkit
        - Ter o wkhtmltopdf instalado no sistema:

Download para Windows/Linux/macOS

🚀 Como usar
        Clone o repositório:

        git clone https://github.com/seu-usuario/CurriculoMaker.git
        cd CurriculoMaker
        Execute o programa:

        python main.py
        Use o menu para cadastrar, buscar ou exportar currículos.

📁 Estrutura de pastas

        GERADORCURRICULOS/
        ├── Backup-Curriculos/       # Currículos salvos em formato JSON
        ├── Curriculos-PDF/          # Currículos exportados em PDF
        └── curriculo_maker.py       # Arquivo principal do sistema

📌 Observações

        Os arquivos são salvos localmente; não há uso de banco de dados.
        Validações básicas são feitas para nome, email, telefone e data.
        O nome do currículo deve ser único.


Desenvolvido por Diogo Teodoro Dias Lamas - Tekig 💼


