import gradio as gr
from forex_python.converter import CurrencyRates
import requests
import tkinter as tk


def get_data():
    url = f'https://api.fastforex.io/fetch-all?api_key={api_key}&api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    rates=data['results']
    keys = list(data['results'].keys())
    return(keys, rates)

def converter(currency1,currency2,box1,box2):
    if (currency1 is None and currency2 is None):
        return('Insert the currency','Insert the currency')
    elif (currency1 is None):
        return('Insert the currency',box2)
    elif (currency2 is None):
        return(box1,'Insert the currency')

    if box1!='':
        box1=box1.replace(',','.')
        try:
            value=float(box1)
        except:
            return('Invalid input',box2)
        result=convert(currency1, currency2, value)
        return(box1, result)
    else:
        box2=box2.replace(',','.')
        try:
            c2=float(box2)
        except:
            return(box1,'Invalid input')
        result=convert(currency2, currency1, value)
        return(result, box2)

def convert(from_currency, to_currency, value):
    url = f'https://api.fastforex.io/convert?from={from_currency}&to={to_currency}&amount={value}&api_key={api_key}'
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    result = response.json()['result'][to_currency]
    return(response.status_code, result)
        
class CurrencyConverter:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Currency converter")
        self.root.geometry('400x200')
        self.root.minsize(400,200)
        self.col1 = tk.Frame(self.root)
        self.col2 = tk.Frame(self.root)
        self.col3 = tk.Frame(self.root)

        element_width=10

        self.from_var=tk.StringVar(self.root)
        self.from_var.set('USD')
        self.from_menu = tk.OptionMenu(self.root, self.from_var, *valid_currency)
        self.from_menu.config(width=element_width)
        self.from_menu.place(relx=0.1, rely=0.1)

        self.amount_label=tk.Label(self.root, text='Amount: ')
        self.amount_label.config(width=element_width)
        self.amount_label.place(relx=0.1, rely=0.4)

        self.amount_entry=tk.Entry(self.root, width=17)
        self.amount_entry.place(relx=0.1, rely=0.7)


        self.to_var=tk.StringVar(self.root)
        self.to_var.set('EUR')
        self.to_menu = tk.OptionMenu(self.root, self.to_var, *valid_currency)
        self.to_menu.config(width=element_width)
        self.to_menu.place(relx=0.65, rely=0.1)

        self.amount_label=tk.Label(self.root, text='Amount: ', width=element_width)
        self.amount_label.place(relx=0.65, rely=0.4)

        self.result_entry=tk.Entry(self.root, width=17)
        self.result_entry.place(relx=0.65, rely=0.7)

        self.convert_button=tk.Button(self.root, text='Convert', command=self.convert_currency)
        self.convert_button.place(relx=0.42, rely=0.8)

        self.convert_button=tk.Button(self.root, text='<->', command=self.switch_value)
        self.convert_button.place(relx=0.45, rely=0.5)

        

        self.root.mainloop()

    def convert_currency(self):
        from_currency=self.from_var.get()
        to_currency=self.to_var.get()

        if (self.amount_entry.get()==''):
            self.result_entry.delete(0, 'end')
            self.result_entry.insert(0,'Insert amount')

        try:
            amount=float(self.amount_entry.get().replace(',','.'))
        except:
            self.result_entry.delete(0, 'end')
            self.result_entry.insert(0,'Invalid input')
            return

        status_code,result=convert(from_currency, to_currency, amount)
        self.result_entry.delete(0, 'end')
        self.result_entry.insert(0,str(result))

    def switch_value(self):
        prev_from_var=self.from_var.get()
        prev_to_var=self.to_var.get()
        self.from_var.set(prev_to_var)
        self.to_var.set(prev_from_var)

        result=self.result_entry.get()
        self.amount_entry.delete(0, 'end')
        self.amount_entry.insert(0, result)
        self.result_entry.delete(0, 'end')

if __name__=='__main__':
    api_key = open ('api_key.txt', 'r').read()
    valid_currency, rates=get_data()
    c_Rate=CurrencyRates()
    CurrencyConverter()