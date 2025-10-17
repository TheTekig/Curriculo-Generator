<h1 align="center">🧾 Curriculo Generator</h1>

<p align="center">
  <b>Aplicação em Python para criar, editar e exportar currículos em PDF.</b><br>
  Sistema completo de cadastro, busca e atualização com armazenamento em JSON e geração de PDF via HTML.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white"/>
  <img src="https://img.shields.io/badge/PyDF-FFD43B?style=for-the-badge&logo=adobeacrobatreader&logoColor=black"/>
  <img src="https://img.shields.io/badge/CLI%20Application-2E3440?style=for-the-badge&logo=gnu-bash&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

---

## 📘 Descrição

O **Gerador de Currículos** é um sistema de console desenvolvido em **Python** que permite ao usuário **criar, visualizar, editar e exportar currículos em formato PDF**.  
Os dados são salvos automaticamente em arquivos **JSON**, garantindo persistência entre sessões.  
O PDF é gerado com **HTML dinâmico**, utilizando a biblioteca `pydf`.

---

## ⚙️ Funcionalidades Principais

- 🧾 Criar currículos com nome, e-mail, telefone e experiências profissionais  
- 💾 Salvar automaticamente os dados em JSON  
- 🔍 Buscar, listar e atualizar currículos existentes  
- 📄 Gerar arquivos PDF personalizados  
- ✅ Validação de entradas (nome, e-mail, telefone, datas)  
- 🧠 Organização modular e fácil manutenção  

---

## 🧰 Tecnologias Utilizadas

| Tecnologia | Função |
|-------------|--------|
| 🐍 **Python 3** | Linguagem principal |
| 🧩 **JSON** | Armazenamento e persistência de dados |
| 📄 **PyDF** | Conversão de HTML para PDF |
| 🕓 **Datetime / OS / Time** | Manipulação de arquivos e datas |

---

## 🏗️ Estrutura do Projeto

    📁 GeradorCurriculos/
    ┣ 📜 main.py # Código principal
    ┣ 📂 Backup-Curriculos/ # JSON com currículos salvos
    ┣ 📂 Curriculos-PDF/ # PDFs gerados automaticamente
    ┗ 📜 README.md


---

## 🚀 Como Executar

1️⃣ Certifique-se de ter o **Python 3** instalado  

2️⃣ Instale a dependência `pydf`:
pip install pydf

3️⃣ Execute o programa:
python main.py

4️⃣ Utilize o menu interativo:

 <p align="center">
   
      ================================
          Sistema de Currículos
      ================================
      1. Preencher Currículo
      2. Listar Currículos
      3. Procurar Currículo
      4. Atualizar Currículo
      5. Sair 
      
 </p>
   
5️⃣ Escolha “Procurar Currículo” para gerar um PDF personalizado automaticamente 🧾

---

## 📈 Aprendizados Técnicos
Uso de arquivos JSON para persistência de dados

Criação de HTML dinâmico para conversão em PDF

Implementação de validações robustas para entradas do usuário

Organização modular de funções

Prática de tratamento de exceções e fluxo de execução

---

## 💡 Melhorias Futuras
Interface gráfica (Tkinter ou PyQt)

Integração com banco de dados (SQLite ou PostgreSQL)

Exportação em outros formatos (DOCX, Markdown)

Sistema multiusuário com autenticação

---

## 👨‍💻 Autor

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/TheTekig) Diogo Teodoro Dias Lamas

<p align="center"> Feito em Python &nbsp;|&nbsp; <b>#SoftwareEngineering</b> 🧠 </p> 
