import gradio as gr
from forex_python.converter import CurrencyRates
import requests
import tkinter as tk

def get_data():
    api_key = open ('api_key.txt', 'r').read()
    print(api_key)

    url = f'https://api.fastforex.io/fetch-all?api_key={api_key}'
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
    if from_currency=='USD':
        return round(value*rates[to_currency],2)
    elif (to_currency=='USD'):
        return round(value/rates[from_currency], 2)
    else:
        return round((value/rates['USD'])*rates[to_currency],2)
        
class CurrencyConverter:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Currency converter")
        self.root.geometry('400x400')

        self.









if __name__=='__main__':

    valid_currency, rates=get_data()
    c_Rate=CurrencyRates()

#     with gr.Blocks() as demo:
#         gr.Markdown("# Currency converter")

#         with gr.Row():
#             with gr.Column():
#                 gr.Markdown('## From: ')
#                 currency1=gr.Dropdown(choices=valid_currency, label="Currency")
#                 box1=gr.Textbox(label="")
#             with gr.Column():
#                 gr.Markdown('## To: ')        
#                 currency2=gr.Dropdown(choices=valid_currency, label="Currency")
#                 box2=gr.Textbox(label="")
#         c=gr.Button("Convert")
#         c.click(fn=converter, inputs=[currency1,currency2,box1,box2], outputs=[box1,box2])

#     demo.launch(share=False)