from os.path import dirname, join
import quandl
quandl.ApiConfig.api_key = "x34ca9wEx9rCfwLF54px"

import bokeh
import pandas as pd
from bokeh.plotting import figure, output_file, show

def stock_plot(ticker,month):

    data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'close'] }, ticker = ['AAPL', 'MSFT'], date = { 'gte': '2016-01-01', 'lte': '2016-12-31' })

    data = data[data.ticker==ticker.upper()]
    data = data[data['date'].map(lambda x: x.month)==int(month)]
    # df['date'] = pd.to_datetime(df['date'])

    module_dir=dirname(__file__)	

    output_file(filename=join(module_dir,'templates',"stock.html"),title="Closing Price")
    # create a new plot with a datetime axis type
    p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")

    p.line(data['date'], data['close'], color='navy', alpha=0.5)

    show(p)
