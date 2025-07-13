import tkinter as tk
from tkinter import ttk
from calculate import TempAnalyzer

def centralizar_janela(janela, largura, altura):
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    x = (tela_largura // 2) - (largura // 2)
    y = (tela_altura // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

def analisar():
    analisador = TempAnalyzer()
    resultados = analisador.analyze()

    texto_resultado.delete("1.0", tk.END) #limpa o texto anterior

    for pasta, (arquivos, tamanho) in resultados.items():
        tamanho_formatado = analisador.format_size(tamanho)
        linha = f"{pasta}: {arquivos} arquivos, {tamanho_formatado}\n"
        texto_resultado.insert(tk.END, linha)

    # linhas = []
    # for pasta, (arquivos, tamanho) in resultados.items():
    #     tamanho_formatado = analisador.format_size(tamanho)
    #     linhas.append(f"{pasta}: {arquivos} arquivos, {tamanho_formatado}")

    # texto = "\n".join(linhas)
    # resultado_var.set(texto)

# Cria a janela principal
root = tk.Tk()
root.title("CleancalC")
centralizar_janela(root, 600, 400)
root.configure(bg='#f5f5f5')

# frame principal
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Texto título
titulo = tk.Label(frame, text="CleancalC – Analisador de arquivos temporários do Windows", 
                  font=("Segoe UI", 14, "bold"), bg="#f5f5f5", fg="#3d518d")
titulo.pack(pady=(0, 10))

# Botão analisar
btn_analisar = tk.Button(root, text="Analisar", command=analisar)
btn_analisar.pack(pady=5)

# Área de texto com scrollbar
text_frame = tk.Frame(frame)
text_frame.pack(fill="both", expand=True)

texto_resultado = tk.Text(text_frame, height=10, font=("Consolas", 11), wrap="word")
scrollbar = ttk.Scrollbar(text_frame, command=texto_resultado.yview)
texto_resultado.configure(yscrollcommand=scrollbar.set)

texto_resultado.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# # Label para resultado, usando StringVar para atualizar texto
# resultado_var = tk.StringVar()
# resultado = tk.Label(root, textvariable=resultado_var, font=("Lucida Console", 12))
# resultado.pack(pady=10)

# Inicia o loop da interface
root.mainloop()
