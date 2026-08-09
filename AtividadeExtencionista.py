# Refood App Desktop - Python com Tkinter
import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import sys

# Obter caminho absoluto para empacotamento com PyInstaller
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
    data_path = os.path.join(os.path.dirname(sys.executable), 'doacoes.json')
else:
    application_path = os.path.dirname(__file__)
    data_path = os.path.join(application_path, 'doacoes.json')

# Carregar dados existentes ou criar novo
if os.path.exists(data_path):
    with open(data_path, "r", encoding="utf-8") as f:
        doacoes = json.load(f)
else:
    doacoes = []

# Função para salvar os dados no arquivo JSON
def salvar_doacoes():
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(doacoes, f, ensure_ascii=False, indent=2)

# Tela de registro de doações
def registrar_doacao():
    alimentos = []

    def adicionar_alimento():
        alimento = entry_alimento.get()
        quantidade = entry_quantidade.get()
        unidade = unidade_medida.get()
        if alimento and quantidade and unidade:
            alimentos.append({"alimento": alimento, "quantidade": f"{quantidade} {unidade}"})
            listbox_alimentos.insert(tk.END, f"{alimento} - {quantidade} {unidade}")
            entry_alimento.delete(0, tk.END)
            entry_quantidade.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Preencha alimento, quantidade e unidade.")

    def remover_alimento():
        selecionado = listbox_alimentos.curselection()
        if selecionado:
            alimentos.pop(selecionado[0])
            listbox_alimentos.delete(selecionado)

    def salvar():
        validade = entry_validade.get()
        bairro = entry_bairro.get()
        contato = entry_contato.get()

        if alimentos and validade and bairro and contato:
            for item in alimentos:
                doacao = item.copy()
                doacao.update({"validade": validade, "bairro": bairro, "contato": contato})
                doacoes.append(doacao)
            salvar_doacoes()
            messagebox.showinfo("Sucesso", "Doações registradas com sucesso!")
            janela.destroy()
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos.")

    janela = tk.Toplevel(app)
    janela.title("Registrar Doação")
    janela.geometry("400x500")
    janela.configure(bg="#fdf6f0")

    fonte = ("Arial", 10)

    tk.Label(janela, text="Alimento:", bg="#fdf6f0", font=fonte).pack()
    entry_alimento = tk.Entry(janela)
    entry_alimento.pack(pady=2)

    tk.Label(janela, text="Quantidade:", bg="#fdf6f0", font=fonte).pack()
    entry_quantidade = tk.Entry(janela)
    entry_quantidade.pack(pady=2)

    tk.Label(janela, text="Unidade:", bg="#fdf6f0", font=fonte).pack()
    unidade_medida = ttk.Combobox(janela, values=["kg", "g", "L", "mL", "unidade(s)"])
    unidade_medida.set("kg")
    unidade_medida.pack(pady=2)

    tk.Button(janela, text="Adicionar Alimento", command=adicionar_alimento, bg="#c8e6c9", relief="flat").pack(pady=5)
    listbox_alimentos = tk.Listbox(janela, height=5)
    listbox_alimentos.pack(pady=5)
    tk.Button(janela, text="Remover Selecionado", command=remover_alimento, bg="#ffcdd2", relief="flat").pack(pady=5)

    tk.Label(janela, text="Validade (ex: 10/07/2025):", bg="#fdf6f0", font=fonte).pack()
    entry_validade = tk.Entry(janela)
    entry_validade.pack(pady=2)

    tk.Label(janela, text="Bairro:", bg="#fdf6f0", font=fonte).pack()
    entry_bairro = tk.Entry(janela)
    entry_bairro.pack(pady=2)

    tk.Label(janela, text="Contato (e-mail ou WhatsApp):", bg="#fdf6f0", font=fonte).pack()
    entry_contato = tk.Entry(janela)
    entry_contato.pack(pady=2)

    tk.Button(janela, text="Salvar Doação", command=salvar, bg="#a5d6a7", relief="flat").pack(pady=15)

# Tela de busca
def buscar_doacoes():
    def buscar():
        bairro = entry_busca.get()
        if not bairro:
            return
        resultados = [d for d in doacoes if d.get("bairro", "").lower() == bairro.lower()]
        if resultados:
            texto = "\n\n".join([
                f"Alimento: {d.get('alimento', '-') }\nQuantidade: {d.get('quantidade', '-') }\nValidade: {d.get('validade', '-') }\nContato: {d.get('contato', '-') }"
                for d in resultados
            ])
            messagebox.showinfo(f"Doações em {bairro}", texto)
        else:
            messagebox.showinfo("Resultado", "Nenhuma doação encontrada nesse bairro.")
        janela_busca.destroy()

    janela_busca = tk.Toplevel(app)
    janela_busca.title("Buscar Doações")
    janela_busca.geometry("300x150")
    janela_busca.configure(bg="#fdf6f0")

    tk.Label(janela_busca, text="Digite o bairro para buscar doações:", bg="#fdf6f0").pack(pady=5)
    entry_busca = tk.Entry(janela_busca)
    entry_busca.pack(pady=5)
    tk.Button(janela_busca, text="Buscar", command=buscar, bg="#c8e6c9", relief="flat").pack(pady=10)

# Tela de relatório completo
def gerar_relatorio():
    if not doacoes:
        messagebox.showinfo("Relatório", "Nenhuma doação registrada.")
        return

    relatorio_window = tk.Toplevel(app)
    relatorio_window.title("Relatório Completo")
    relatorio_window.geometry("500x400")
    relatorio_window.configure(bg="#fffde7")

    texto = "\n\n".join([
        f"Alimento: {d.get('alimento', '-') }\nQuantidade: {d.get('quantidade', '-') }\nValidade: {d.get('validade', '-') }\nBairro: {d.get('bairro', '-') }\nContato: {d.get('contato', '-') }"
        for d in doacoes
    ])
    texto_box = tk.Text(relatorio_window, wrap="word", bg="#fffde7", font=("Arial", 10))
    texto_box.insert(tk.END, texto)
    texto_box.config(state="disabled")
    texto_box.pack(expand=True, fill="both", padx=10, pady=10)

# Tela de exclusão
def excluir_doacao():
    janela_excluir = tk.Toplevel(app)
    janela_excluir.title("Excluir Doações")
    janela_excluir.geometry("400x300")
    janela_excluir.configure(bg="#fdf6f0")

    tk.Label(janela_excluir, text="Selecione a doação que deseja excluir:", bg="#fdf6f0").pack(pady=5)
    listbox = tk.Listbox(janela_excluir)

    for d in doacoes:
        item = f"{d.get('alimento', '-')} - {d.get('quantidade', '-')} - {d.get('bairro', '-')}"
        listbox.insert(tk.END, item)
    listbox.pack(padx=10, pady=10, fill="both", expand=True)

    def excluir_selecionado():
        selecionado = listbox.curselection()
        if selecionado:
            doacoes.pop(selecionado[0])
            salvar_doacoes()
            listbox.delete(selecionado)
            messagebox.showinfo("Sucesso", "Doação excluída com sucesso.")

    tk.Button(janela_excluir, text="Excluir Selecionado", command=excluir_selecionado, bg="#ffcdd2", relief="flat").pack(pady=10)

# Interface principal
app = tk.Tk()
app.title("ReFood - Doações de Alimentos")
app.geometry("600x480")
app.minsize(600, 480)
app.configure(bg="#fdf6f0")

# Canvas fixo para não distorcer elementos com redimensionamento
canvas = tk.Canvas(app, bg="#fdf6f0", highlightthickness=0)
canvas.place(relx=0.5, rely=0.5, anchor="center", width=600, height=480)
canvas.create_text(300, 100, text="REFOOD", font=("Arial Black", 80), fill="#ffe0b2")
canvas.create_text(580, 460, text="Piettro Lino Lorenzon RU:4566806", anchor="se", font=("Arial", 8), fill="#999999")

frame = tk.Frame(canvas, bg="#fdf6f0")
frame.place(relx=0.5, rely=0.55, anchor="center")

label = tk.Label(frame, text="ReFood - Conectando Sobra e Solidariedade", font=("Arial", 14), bg="#fdf6f0")
label.pack(pady=10)

btn_registrar = tk.Button(frame, text="Registrar Doação", command=registrar_doacao, width=30, bg="#aed581", relief="flat")
btn_registrar.pack(pady=5)

btn_buscar = tk.Button(frame, text="Buscar Doações por Bairro", command=buscar_doacoes, width=30, bg="#81d4fa", relief="flat")
btn_buscar.pack(pady=5)

btn_relatorio = tk.Button(frame, text="Gerar Relatório Completo", command=gerar_relatorio, width=30, bg="#fff176", relief="flat")
btn_relatorio.pack(pady=5)

btn_excluir = tk.Button(frame, text="Excluir Doação", command=excluir_doacao, width=30, bg="#e57373", relief="flat")
btn_excluir.pack(pady=5)

btn_sair = tk.Button(frame, text="Sair", command=app.quit, width=30, bg="#d7ccc8", relief="flat")
btn_sair.pack(pady=20)

app.mainloop()
