from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

from alpha_vantage.timeseries import TimeSeries
api_key = 'YOUR_API_KEY'

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        symbol = request.form['symbol']
        chart_type = request.form['chart_type']
        
        ts = TimeSeries(key=api_key)
        data, meta_data = ts.get_daily(symbol=symbol)

        fig = visualize(data, chart_type)
        
        img = io.BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        
        plot_url = base64.b64encode(img.getvalue()).decode()
        
    with open('stocks.csv') as f:
        symbols = f.read().splitlines()
        
    return render_template('index.html', symbols=symbols, plot_url=plot_url)
    
def visualize(data, chart_type):
    fig, ax = plt.subplots() 
    
    return fig
    
if __name__ == '__main__':
   app.run()