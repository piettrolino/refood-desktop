# ReFood - App Desktop de Doações de Alimentos 🍲

Um aplicativo desktop desenvolvido em Python para facilitar o registro, gerenciamento e busca de doações de alimentos, conectando solidariedade e evitando o desperdício. O sistema utiliza uma interface gráfica amigável e armazena os dados localmente.

---

## 📸 Demonstração do Sistema

*(Nota: Quando subir para o GitHub, arraste e solte suas imagens aqui para substituir estes textos)*
* `![Menu Principal](link_da_imagem_do_menu)`
* `![Tela de Registro](link_da_imagem_de_registro)`
* `![Busca e Relatórios](link_da_imagem_do_relatorio)`

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
