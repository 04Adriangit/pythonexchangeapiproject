from  tkinter import *   
from turtle import width 
import requests
import datetime 

payload = {}
key = {"apikey" : "RzIJXHIoW1aQjRG7tdOMqXGspGCgkUFv" }

programm = Tk()
programm.geometry("500x500")
programm.title("Currency converter")
txt1 = Label(programm, text="Currency converter", font= 50)  # type: ignore
txt1.grid(row=0, column=1, padx=150, pady= 20)
from_currencies = ['EUR', 'USD', 'CAD', 'JPY', 'RON']
to_currencies = ['EUR', 'USD', 'CAD', 'JPY', 'RON']
first_currency = StringVar(programm)
first_currency.set("EUR")
second_currency = StringVar(programm)
second_currency.set("USD")
#url = f'https://api.apilayer.com/exchangerates_data/latest?symbols={second_currency.get()}&base={first_currency.get()}'
currency_menu = OptionMenu(programm,  first_currency, *from_currencies)
currency_menu.grid(row=1, column=1)
currency_menu.config(width= 10, borderwidth=0.5)
currency_menu2 = OptionMenu(programm, second_currency, *to_currencies)
currency_menu2.grid(row=2, column=1,pady= 10)
currency_menu2.config(width= 10, borderwidth=0.5)
txt3 = Label(programm, text="Enter amount:", font=50)  # type: ignore
txt3.grid(row=3, column =1,pady= 20)


def validate(input):
	try:
		float(input)
	except:
		return False
	return True


e = Entry(programm, width=30, validate='key', vcmd=(programm.register(validate), '%P'))
e.grid(row=4, column=1,pady= 10)
button_convert = Button(programm, text="Convert")
button_convert.grid(row=5, column=1,pady= 10)
txt4 = Label(programm, text="", font=50)  # type: ignore
txt4.grid(row=6, column=1)
sign = ""
time = datetime.datetime.now();
day = time.strftime("%d")
month = time.strftime("%B")
year = time.strftime("%Y")
hour = time.strftime("%H")
minutes = time.strftime("%M")
seconds = time.strftime("%S")
txt5 = Label(programm, text="", font=50)
txt5.grid(row=7, column=1)


def convert(currency):
	amount = float(e.get())
	url = f'https://api.apilayer.com/exchangerates_data/latest?symbols={second_currency.get()}&base={first_currency.get()}'
	response = requests.request("GET", url, headers=key, data= payload)
	currency_data = response.json()
	exchange_rate = currency_data["rates"][second_currency.get()]
	amount = amount * exchange_rate
	amount = format(amount, '.2f')
	if second_currency.get() == "EUR":
		sign = "€ "
	elif second_currency.get() == "USD":
		sign = "$ "
	elif second_currency.get() == "CAD":
		sign = "C$ "
	elif second_currency.get() == "JPY":
		sign = "¥ "
	elif second_currency.get() == "RON":
		sign = "lei "

	amount = str(amount)
	print(currency_data)
	return sign + amount  # type: ignore

def onClick():
	txt4.config(text=convert(e))
	txt5.config(text=day + " " + month + " " + year + " at " + hour + ":" + minutes + ":" + seconds, fg='red')
	



button_convert.config(command=onClick)
programm.mainloop()

