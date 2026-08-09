
# ReFood - App Desktop de Doações de Alimentos 🍲

Um aplicativo desktop desenvolvido em Python para facilitar o registro, gerenciamento e busca de doações de alimentos, conectando solidariedade e evitando o desperdício. O sistema utiliza uma interface gráfica amigável e armazena os dados localmente.

---

## 📸 Demonstração do Sistema
<img width="224" height="172" alt="resultadopesquisa" src="https://github.com/user-attachments/assets/a344ecd6-d17e-4d43-a2de-75954fad541a" />
<img width="302" height="182" alt="pesquisa" src="https://github.com/user-attachments/assets/5867bcd4-7cbf-41b9-a580-a0844369c562" />
<img width="502" height="432" alt="pesquisatotal" src="https://github.com/user-attachments/assets/588b02b6-c87a-41e5-ba18-e9a6723f9b88" />
<img width="602" height="512" alt="telainicial pnh" src="https://github.com/user-attachments/assets/074a44d0-7929-43b1-a006-9cb922a1be88" />
<img width="402" height="532" alt="doacao" src="https://github.com/user-attachments/assets/5c6f2658-d462-413c-b4e3-e42a06b0f249" />
<img width="402" height="532" alt="registrodoacao" src="https://github.com/user-attachments/assets/9eabf776-1faa-41f3-9e77-eb2ea3280b33" />

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Linguagem:** Python 3
* **Interface Gráfica (GUI):** Tkinter / ttk
* **Persistência de Dados:** JSON (Manipulação de arquivos locais)
* **Empacotamento:** Estrutura preparada para gerar executáveis via PyInstaller (`sys._MEIPASS`).

---

## ⚙️ Funcionalidades

1. **Registrar Doação:** Adição de múltiplos alimentos em uma única doação, com definição de quantidade, unidade de medida, validade, bairro e contato do doador.
2. **Buscar por Bairro:** Filtro rápido para localizar doações disponíveis em regiões específicas.
3. **Gerar Relatório Completo:** Visualização em lista de todo o histórico de doações ativas cadastradas no sistema.
4. **Excluir Doação:** Remoção segura de doações que já foram coletadas ou que passaram da validade.
5. **Persistência Local:** Todos os dados são salvos automaticamente no arquivo `doacoes.json`.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python instalado na máquina.

### Executando pelo Código-Fonte

1. Clone este repositório:
   ```bash
   git clone [https://github.com/seu-usuario/refood-desktop.git](https://github.com/seu-usuario/refood-desktop.git)
   cd refood-desktop
Execute o script principal:

Bash
python main.py
(O arquivo doacoes.json será gerado automaticamente na mesma pasta na primeira execução).

Como Gerar um Executável (.exe)
O código já está adaptado para caminhos absolutos. Para compilar um executável que roda em qualquer computador sem precisar do Python instalado:

Instale o PyInstaller:

Bash
pip install pyinstaller
Gere o executável (sem o console de fundo):

Bash
pyinstaller --noconsole --onefile main.py
