import tkinter as tk
import sys
import os
from tkinter import ttk
from calculate import TempAnalyzer

def recurso_caminho(rel_path):
    """
    Retorna o caminho absoluto para recursos, mesmo quando empacotado com PyInstaller.
    """
    try:
        base_path = sys._MEIPASS  # Quando empacotado
    except Exception:
        base_path = os.path.abspath(".")  # Quando rodando normalmente

    return os.path.join(base_path, rel_path)

def centralizar_janela(janela, largura, altura):
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    x = (tela_largura // 2) - (largura // 2)
    y = (tela_altura // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

# Função atualizada para preencher a tabela
def analisar():
    analisador = TempAnalyzer()
    resultados = analisador.analyze()

    # Limpa linhas antigas
    for item in tree.get_children():
        tree.delete(item)

    # Insere novas linhas
    for pasta, (arquivos, tamanho) in resultados.items():
        tamanho_formatado = analisador.format_size(tamanho)
        tree.insert("", "end", values=(pasta, arquivos, tamanho_formatado))

# Cria a janela principal
root = tk.Tk()
root.title("CleancalC")
centralizar_janela(root, 600, 400)
root.configure(bg='#f5f5f5')
root.iconbitmap(recurso_caminho("assets/icon-log-off.ico"))

# frame principal
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Texto título
titulo = tk.Label(frame, text="CleancalC – Analisador de arquivos temporários do Windows", 
                  font=("Segoe UI", 14, "bold"), bg="#f5f5f5", fg="#3d518d")
titulo.pack(pady=(0, 10))

# Botão analisar com estilo
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 11), padding=6)
btn_analisar = ttk.Button(root, text="Analisar", command=analisar)
btn_analisar.pack(pady=10)

# Área de resultado em forma de tabela (Treeview)
colunas = ("Pasta", "Arquivos", "Tamanho")
tree = ttk.Treeview(frame, columns=colunas, show="headings", height=8)
tree.pack(fill="both", expand=True)

# Definindo os nomes das colunas
tree.heading("Pasta", text="Pasta")
tree.heading("Arquivos", text="Arquivos")
tree.heading("Tamanho", text="Tamanho")

# Definindo a largura das colunas
tree.column("Pasta", width=250)
tree.column("Arquivos", width=80, anchor="center")
tree.column("Tamanho", width=100, anchor="center")

# Inicia o loop da interface
root.mainloop()
