import tkinter as tk
from tkinter import messagebox

class Entregador:
    def __init__(self, nome):
        self.nome = nome
        self.entregas = 0

    def registrar_entrega(self, quantidade_entregas):
        self.entregas += quantidade_entregas

    def calcular_pagamento(self, valor_por_entrega):
        return self.entregas * valor_por_entrega

class EntregadorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Pagamento de Entregadores")

        self.entregadores = {}

        # Widgets de entrada
        self.label_nome = tk.Label(master, text="Nome do Entregador:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(master)
        self.entry_nome.grid(row=0, column=1)

        self.label_entregas = tk.Label(master, text="Quantidade de Entregas:")
        self.label_entregas.grid(row=1, column=0)
        self.entry_entregas = tk.Entry(master)
        self.entry_entregas.grid(row=1, column=1)

        self.label_cidade = tk.Label(master, text="Cidade:")
        self.label_cidade.grid(row=2, column=0)
        self.cidade_var = tk.StringVar(master)
        self.cidade_var.set("Barra")  # Valor padrão
        self.optionmenu_cidade = tk.OptionMenu(master, self.cidade_var, "Barra", "Igaraçu")
        self.optionmenu_cidade.grid(row=2, column=1)

        # Botões
        self.registrar_button = tk.Button(master, text="Registrar Entregas", command=self.registrar_entregas)
        self.registrar_button.grid(row=3, columnspan=2)

        self.calcular_button = tk.Button(master, text="Calcular Pagamento", command=self.calcular_pagamento)
        self.calcular_button.grid(row=4, columnspan=2)

    def registrar_entregas(self):
        nome = self.entry_nome.get()
        try:
            quantidade_entregas = int(self.entry_entregas.get())
        except ValueError:
            messagebox.showerror("Erro", "Quantidade de entregas deve ser um número inteiro")
            return

        if nome in self.entregadores:
            self.entregadores[nome].registrar_entrega(quantidade_entregas)
        else:
            entregador = Entregador(nome)
            entregador.registrar_entrega(quantidade_entregas)
            self.entregadores[nome] = entregador

        messagebox.showinfo("Sucesso", "Entregas registradas com sucesso!")
        self.entry_nome.delete(0, tk.END)
        self.entry_entregas.delete(0, tk.END)

    def calcular_pagamento(self):
        cidade = self.cidade_var.get()
        valor_por_entrega = 8 if cidade == "Igaraçu" else 10

        resultados = []
        for nome_entregador, entregador in self.entregadores.items():
            pagamento = entregador.calcular_pagamento(valor_por_entrega)
            resultados.append(f"{nome_entregador} deve receber R${pagamento:.2f}")

        if resultados:
            messagebox.showinfo("Resultado", "\n".join(resultados))
        else:
            messagebox.showinfo("Resultado", "Nenhum entregador registrado.")

root = tk.Tk()
app = EntregadorApp(root)
root.mainloop()
