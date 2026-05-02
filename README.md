# ♟️ Jogo de Xadrez Online

Este é um projeto de um jogo de xadrez funcional com interface web, desenvolvido com **Flask (Python)** no backend e **JavaScript puro** no frontend.

O objetivo do projeto foi praticar integração entre frontend e backend usando uma API REST.

---

## 🚀 Demonstração

🔗 Acesse o jogo funcionando aqui:  
https://xadrez-python-1.onrender.com

---

## ⚙️ Tecnologias utilizadas

- Python (Flask)
- JavaScript (Vanilla JS)
- HTML5
- CSS3
- API REST
- CORS (Flask-CORS)
- Deploy no Render

---

## 🎮 Funcionalidades

- Tabuleiro de xadrez interativo
- Clique para selecionar e mover peças
- Validação de turnos
- Captura de peças
- Reset do jogo
- Comunicação em tempo real com backend via API

---

## 🧠 Arquitetura do projeto

O projeto é dividido em duas partes:

### Backend (Flask)
- Responsável pela lógica do jogo
- Controla o estado do tabuleiro
- Valida movimentos
- Expõe API endpoints:
  - `/board`
  - `/move`
  - `/reset`

### Frontend (JavaScript)
- Renderiza o tabuleiro
- Captura cliques do usuário
- Envia jogadas para o backend via `fetch`
- Atualiza o estado do jogo em tempo real

---

## 📦 Como executar localmente

```bash
git clone https://github.com/SEU_USUARIO/xadrez-python.git
cd xadrez-python
pip install -r requirements.txt
python app.py
