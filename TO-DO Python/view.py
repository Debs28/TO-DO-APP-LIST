import tkinter as tk
import query
from tkinter import messagebox


tela_principal = tk.Tk()
tela_principal.title('TO-DO')
tela_principal.configure(bg='#F8F8FF')
tela_principal.geometry('660x510')


titulo = tk.Label(tela_principal, text='TO-DO APP', anchor='center', font=('Arial 16 bold'), bg='#F8F8FF')
titulo.place(x=270, y=20)

tarefa = tk.Entry(tela_principal, width=54, relief='solid', font=('Arial 12'))
tarefa.place(x=100, y=70)

lista_tarefas = tk.Listbox(tela_principal, width=80, height=15)
lista_tarefas.place(x=100, y=100)

#btn inserir
def inserir_to_to():
    #tarefa.delete(0, tk.END)
    tarefas = tarefa.get()
    query.create_to_do([tarefas])
    lista_tarefas.insert(tk.END, tarefas)
    tarefa.delete(0, tk.END)
    messagebox.showinfo('Adicionada', 'Tarefa adicionada com sucesso!')
       
    listar_todos()    
bt_inserir = tk.Button(tela_principal,text='ADICIONAR',anchor='center' , command=inserir_to_to, width=10, font=('Ivy 9 bold'), bg='#CCCCFF', relief='raised', overrelief='ridge')
bt_inserir.place(x=120, y=360)

#Btn Atualizar
def atualizar_tarefa(): 
    selecionada = lista_tarefas.curselection()[0]
    tarefa_selecionada = lista_tarefas.get(selecionada)
    tarefa.insert(tk.END, tarefa_selecionada)
    tarefas = query.listar_to_do()
    
    def update():
        for dever in tarefas:
            if tarefa_selecionada == dever[1]:
                nova_tarefa = [tarefa.get(), dever[0]]
                query.update_to_do(nova_tarefa)
                tarefa.delete(0, tk.END)
                messagebox.showinfo('Atualizado', 'Tarefa atualizada com sucesso!')  
        listar_todos()
             
    bt_confirmar = tk.Button(tela_principal,text='CONFIRMAR',command=update, width=10, font=('Ivy 9 bold'), bg='#40E0D0', relief='raised', overrelief='ridge')
    bt_confirmar.place(x=220, y=390)
    
bt_atualizar = tk.Button(tela_principal,text='ATUALIZAR',command=atualizar_tarefa, width=10, font=('Ivy 9 bold'), bg='#40E0D0', relief='raised', overrelief='ridge')
bt_atualizar.place(x=220, y=360)

#Btn Deletar
def deletar_tarefa():
    tarefa_selecionada = lista_tarefas.curselection()[0]
    deletar_tarefa_selecionada = lista_tarefas.get(tarefa_selecionada)
    tarefas = query.listar_to_do()
    
    for dever in tarefas:
       if deletar_tarefa_selecionada == dever[1]:
           query.delete_to_do([dever[0]])
           messagebox.showinfo('Deletado', 'Tarefa deletada com sucesso!')  
    
    listar_todos()
bt_deletar = tk.Button(tela_principal,text='DELETAR',command=deletar_tarefa, width=10, font=('Ivy 9 bold'), bg='#DE3163', relief='raised', overrelief='ridge')
bt_deletar.place(x=320, y=360)

def deletar_concluido():
    count = 0
    while count < lista_tarefas.size():
        if lista_tarefas.itemcget(count, "fg") == '#00FF7F':
            lista_tarefas.delete(lista_tarefas.index(count))
        else:
            count +=1
        # tarefa_concluida =  lista_tarefas.itemcget(count, "fg") == '#00FF7F'
        # #deletar_tarefa_concluida = lista_tarefas.get(tarefa_concluida)

        # tarefas = query.listar_to_do()

        # for dever in tarefas:
        #     if tarefa_concluida == dever[0]:
        #         query.delete_to_do([dever[0]])
    messagebox.showinfo('Deletado', 'Tarefa deletada com sucesso!')
      



bt_deletar = tk.Button(tela_principal,text='DEL CONCLUIDO',command=deletar_concluido, width=15, font=('Ivy 9 bold'), bg='#DE3163', relief='raised', overrelief='ridge')
bt_deletar.place(x=310, y=390)

def deletar_tudo():
    lista_tarefas.delete(0, tk.END)
    query.delete_all()
    messagebox.showinfo('Sucesso', 'Todas as tarefas foram deletadas!')  
    listar_todos()
bt_deletar = tk.Button(tela_principal,text='DEL ALL',command=deletar_tudo, width=15, font=('Ivy 9 bold'), bg='#DE3163', relief='raised', overrelief='ridge')
bt_deletar.place(x=310, y=420)

def marcar_concluidas():
    lista_tarefas.itemconfig(
        lista_tarefas.curselection(), fg='#00FF7F'
    )
    lista_tarefas.selection_clear(0, tk.END)
           
    bt_listar = tk.Button(tela_principal,text='NÃO CONCLUIDO',command=desmarcar_concluidas,  width=15, font=('Ivy 9 bold'), bg='#8B008B', relief='raised', overrelief='ridge')
    bt_listar.place(x=520, y=390)

def desmarcar_concluidas():
    lista_tarefas.itemconfig(
        lista_tarefas.curselection(), fg='#000000'
    )

    lista_tarefas.selection_clear(0, tk.END)

    
bt_listar = tk.Button(tela_principal,text='CONCLUIDOS',command=marcar_concluidas,  width=10, font=('Ivy 9 bold'), bg='#8B008B', relief='raised', overrelief='ridge')
bt_listar.place(x=520, y=360)

def tarefas_concluidas():
    count = 0
    while count < lista_tarefas.size():
        if lista_tarefas.itemcget(count, "fg") == '#00FF7F':
            lista_tarefas.see(lista_tarefas.index(count))


def tarefas_pendentes():
    count = 0
    while count < lista_tarefas.size():
        if lista_tarefas.itemcget(count, "fg") == '#000000':
            lista_tarefas.bbox(lista_tarefas.index(count))
        else:
          count += 1  

def botoes_adicionais_listar():         
    bt_listar = tk.Button(tela_principal,text='CONCLUIDOS',command=tarefas_concluidas, width=10, font=('Ivy 9 bold'), bg='#FFB6C1', relief='raised', overrelief='ridge')
    bt_listar.place(x=430, y=390)   
        
    bt_listar = tk.Button(tela_principal,text='PENDENTES',command=botoes_adicionais_listar, width=10, font=('Ivy 9 bold'), bg='#FFB6C1', relief='raised', overrelief='ridge')
    bt_listar.place(x=430, y=420)
    

bt_listar = tk.Button(tela_principal,text='LISTAR',command=botoes_adicionais_listar, width=10, font=('Ivy 9 bold'), bg='#FFB6C1', relief='raised', overrelief='ridge')
bt_listar.place(x=430, y=360)

def listar_todos():
    lista_tarefas.delete(0, tk.END)
    listar_todos = query.listar_to_do()
    for tarefas in listar_todos:
        lista_tarefas.insert(tk.END, tarefas[1])

listar_todos()   
tela_principal.mainloop()