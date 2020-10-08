# ----------- função para selecionar o(os) caminho(os) do(os) arquivo(os) --------------------------------
def SelecionarArquivos():
	if entrynome.get() == "":
		preencher_nome = messagebox.showwarning("Alerta","Preencha o nome do arquivo.")
		if preencher_nome == "ok":
			return
	else:
		filepath = root.filename = filedialog.askopenfilenames(initialdir="./",title="Selecione",filetypes=(("pdf","*.pdf"),("texto","*.txt"),("all files","*.*")))
		if filepath == "":
			nenhum_selecionado = messagebox.showwarning("Alerta","Nenhum arquivo selecionado!")
			if nenhum_selecionado == "ok":
				return
		else:
			for i in filepath:
				filezip = zipfile.ZipFile(entrynome.get() + combobox_ext.get(), 'a') # Cria um novo arquivo ZIP.
				filezip.write (i, compress_type=zipfile.ZIP_DEFLATED) # adiciona o arquivo ao ZIP.
				filezip.close()
				print(i)
	entrynome.delete(0,END) # limpando o entrynome


try:
	from tkinter import *
	from tkinter import filedialog
	from tkinter import messagebox
	from tkinter import ttk
	import zipfile

	# ----------- Start bot -----------------------------------------------------------------------------------
	root = Tk()
	root.title("Compactador")
	# root.iconbitmap("ico_bot.ico")
	root.configure(bg="#C0C0C0")
	root.resizable(False,False) 
	# root.geometry("750x500") # WxH
	root.eval('tk::PlaceWindow . center')

	# ------------- widgets -------------------------
	lbtitulo = Label(root,text="Compactador", bg="#C0C0C0", bd=0.01, font="Broadway 20 bold")
	lbnome = Label(root,text="Nome do Arquivo:", font="Courier 10", bg="#C0C0C0")
	entrynome = Entry(root, width =30, bd=4)
	# selecionar zip ou rar
	combobox_ext = ttk.Combobox(root, width=5, values=".zip .rar", state="readonly") # adicionando um Combobox
	combobox_ext.set(".zip") # para o combobox iniciar com .zip
	btselecionar_arquivos = Button(root, text="Selecionar arquivos", borderwidth=5, bg="#C0C0C0", font="Courier 9 bold", command=SelecionarArquivos)
	# btselecionar_arquivos["state"] = "disabled"

	# ------------- layout --------------------------
	lbtitulo.grid(row=0, column=0, columnspan=3,padx=5, pady=10)
	lbnome.grid(row=1, column=0, sticky=W, padx=5)
	entrynome.grid(row=2, column=0, sticky=W, padx=5,ipady=3)
	combobox_ext.grid(row=2, column=1, sticky=W, padx=3,ipady=4)
	btselecionar_arquivos.grid(row=3, column=0, sticky=W, padx=5, pady=15)

	root.mainloop()

except ModuleNotFoundError as e:
	apilist = {"zipfile":"zipfile37"}
	st = str(e).split(" ")
	mnf = st[3].replace("'","")
	if mnf in apilist:
		os.system("pip install " + apilist[mnf])
	else:
		raise Exception("Modulo não na lista de APIs!")