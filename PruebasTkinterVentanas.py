from tkinter import * 

class Welcome():

	def __init__(self, master):


		self.master = master
		self.master.geometry('300x300')
		self.master.title('VAPOR')

		self.label1=Label(self.master, text="Bienvenido a mi bot", fg='red').grid(row=0, column=2)
		self.button1=Button(self.master,text="Dashboard", fg='blue', command=self.gotoDashboard).grid(row=6, column=2)
		self.button1=Button(self.master,text="Quit", fg='blue', command=self.finish).grid(row=6, column=3)

		

	def gotoDashboard(self):

		root2=Toplevel(self.master)
		myGUI=dashboard(root2)




	def finish(self):

		self.master.destroy()


class dashboard():

	def __init__(self, master):

		self.nhours=DoubleVar()
		self.salaryh=DoubleVar()
		self.Tk.withdraw()
		
		self.master = master
		self.master.geometry('400x400')
		self.master.title('Dashboard')


		self.label1=Label(self.master, text="Bienvenido al Dashboard").grid(row=0, column=2)
		self.label2=Label(self.master, text="Precio moneda").grid(row=3, column=0)
		self.label3=Label(self.master, text="Monedas").grid(row=4, column=0)

		self.mysalary=Entry(self.master, textvariable=self.salaryh).grid(row=3, column=2)
		self.myhours=Entry(self.master, textvariable=self.nhours).grid(row=4, column=2)
		self.button1=Button(self.master, text="Calcula tu estimado", fg='blue', command=self.calculateSalary).grid(row=5,column=2)
		self.button2=Button(self.master, text="Volver", fg='blue', command=self.myQuit).grid(row=5,column=3)

 
	def calculateSalary(self):

		hours=self.nhours.get()
		print(hours)

		hsal=self.salaryh.get()
		salary= hours*hsal
		print(salary)

		self.labelresult=Label(self.master, text="Tu valor estimado es: %.2f BTC" % salary).grid(row=7, column=2)


	def myQuit(self):
	
		self.master.destroy()	

	



def main():

	root=Tk()
	myGUIWelcome=Welcome(root)
	root.mainloop()

if __name__ == '__main__':

	main()



