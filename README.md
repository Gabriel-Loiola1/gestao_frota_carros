# 🚗 Sistema de Gestão de Frotas

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)

Sistema web desenvolvido como requisito da disciplina de **Programação para Internet II** (ADS - IFPI). O projeto visa controlar o fluxo de veículos de uma empresa, gerenciando saídas, retornos e quilometragem, com controle de acesso diferenciado por perfis.

---

## 📋 Funcionalidades

### 🔐 Controle de Acesso e Perfis
O sistema possui três níveis de hierarquia:
* **Gestor:** Responsável pelo cadastro de veículos e pessoas. Tem acesso a um painel administrativo exclusivo.
* **Motorista:** Perfil operacional. Pode apenas visualizar carros disponíveis, registrar saídas e devoluções.
* **Admin (Superusuário):** Acesso total ao sistema e ao Django Admin.

### 🚘 Gestão de Frota
* **CRUD de Veículos:** Cadastro, edição e inativação (Manutenção) de carros.
* **Monitoramento:** Painel em tempo real mostrando quais carros estão na rua e quais estão na garagem.
* **Controle de KM:** Validação inteligente que impede a devolução de um veículo com quilometragem menor que a de saída.

### 📝 Regras de Negócio
* Veículos em uso ficam bloqueados para novas saídas.
* Apenas Gestores podem cadastrar novos Motoristas e Veículos.
* Histórico completo de quem utilizou cada carro.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3.13.4, Django 5
* **Banco de Dados:** SQLite3 (Padrão do Django)
* **Frontend:** HTML5, Bootstrap 5 (CDN), Django Widget Tweaks
* **Controle de Versão:** Git / GitHub

---

## 🚀 Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar o ambiente de desenvolvimento.

### 1. Clone o repositório
```
git clone [https://github.com/Gabriel-Loiola1/gestao_frota_carros.git](https://github.com/Gabriel-Loiola1/gestao_frota_carros.git)
cd gestao_frota_carros
```

### 2. Crie e ative o ambiente virtual
Windows
```
python -m venv .venv
.venv\Scripts\activate
```
Linux/Mac
```
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências.
```
pip install -r requirements.txt
```

### 4. Configure o banco de dados.
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário.
```
python manage.py createsuperuser
```

### 6. ⚠️ Configuração Importante (Primeiro Acesso)
O superusuário criado via terminal não possui o "Perfil de Gestor" automaticamente vinculado. Para corrigir isso e acessar todas as funções:

1 - Rode o servidor: python manage.py runserver

2 - Acesse o Admin: http://127.0.0.1:8000/admin

3 - Vá em Users > Clique no seu usuário.

4 - Role até o final da página e preencha a seção Gestor (Departamento e Telefone).

5 - Salve. Agora você tem acesso total ao Dashboard.

### 📂 Estrutura do Projeto
- settings/: Configurações globais (settings.py, urls.py).
- contas/: App responsável pela autenticação e modelos de usuários (Motorista, Gestor).
- core/: App principal com a lógica de negócio (Veiculo, Movimentacao).
- templates/: Arquivos HTML do projeto.
- assets/: Pasta com o PNG do Diagrama ER

### Diagrama ER

<img src="assets/Diagrama Gestão Frotas.png" alt="Diagrama ER" width="600">

### 🤝 Colaboradores
Gabriel Loiola - Desenvolvedor
