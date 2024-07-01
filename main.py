import gradio as gr
from forex_python.converter import CurrencyRates
from datetime import datetime

valid_currency=["USD", "EUR", "GBP", "ILS", "DKK", "CAD", "IDR", "BGN","JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "LTL", "NOK", "RUB","INR", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR"]
c_Rate=CurrencyRates()
def converter(currency1,currency2,box1,box2):
    if (currency1 is None and currency2 is None):
        return('Insert the currency','Insert the currency')
    elif (currency1 is None):
        return('Insert the currency',box2)
    elif (currency1 is None):
        return(box1,'Insert the currency')
    
    if box1!='':
        box1=box1.replace(',','.')
        try:
            c1=float(box1)
        except:
            return('Invalid input',box2)
        now = datetime.now()
        rate = c_Rate.exchange_rate(currency1,currency2, now)
        result = float(rate) * float(rate)
        return(box1, result)
    else:
        box2=box2.replace(',','.')
        try:
            c2=float(box2)
        except:
            return(box1,'Invalid input')
        
        now = datetime.now()
        rate = c_Rate.exchange_rate(c1,c2, now)
        result = float(rate) * float(rate)
        return(result, box2)

with gr.Blocks() as demo:
    gr.Markdown("# Currency converter")

    with gr.Row():
        with gr.Column():
            gr.Markdown('## From: ')
            currency1=gr.Dropdown(choices=valid_currency, label="Currency")
            box1=gr.Textbox(label="")
        with gr.Column():
            gr.Markdown('## To: ')        
            currency2=gr.Dropdown(choices=valid_currency, label="Currency")
            box2=gr.Textbox(label="")
    convert=gr.Button("Convert")
    convert.click(fn=converter, inputs=[currency1,currency2,box1,box2], outputs=[box1,box2])

demo.launch(share=False)