from flask import Flask,render_template,request,redirect
from stockfunction import stock_plot
ticker = Flask(__name__)

ticker.vars={}


@ticker.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('userinfo.html')
    else:
        #request was a POST
        ticker.vars['ticker'] = request.form['ticker']
        ticker.vars['month'] = request.form['month']

	stock_plot(ticker.vars['ticker'],ticker.vars['month'])
	
        return redirect('/next')

@ticker.route('/next',methods=['GET'])
def next():  

    return render_template('stock.html') 

if __name__ == "__main__":
    ticker.run(host='0.0.0.0')
