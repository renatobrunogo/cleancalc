import tkinter as tk
from calculate import TempAnalyzer

def analisar():
    analisador = TempAnalyzer()
    resultados = analisador.analyze()

    linhas = []
    for pasta, (arquivos, tamanho) in resultados.items():
        tamanho_formatado = analisador.format_size(tamanho)
        linhas.append(f"{pasta}: {arquivos} arquivos, {tamanho_formatado}")

    texto = "\n".join(linhas)
    resultado_var.set(texto)

# Cria a janela principal
root = tk.Tk()
root.title("CleancalC")
root.geometry("500x200")

# Texto título
titulo = tk.Label(root, text="Analisador de memória temporária do Windows", font=("Helvetica", 14))
titulo.pack(pady=10)

# Botão analisar
btn_analisar = tk.Button(root, text="Analisar", command=analisar)
btn_analisar.pack(pady=5)

# Label para resultado, usando StringVar para atualizar texto
resultado_var = tk.StringVar()
resultado = tk.Label(root, textvariable=resultado_var, font=("Lucida Console", 12))
resultado.pack(pady=10)

# Inicia o loop da interface
root.mainloop()
