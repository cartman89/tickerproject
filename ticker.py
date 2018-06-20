from flask import Flask,render_template,request,redirect
from stockfunction import stock_plot
application = Flask(__name__)

application.vars={}


@application.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('userinfo.html')
    else:
        #request was a POST
        app.vars['ticker'] = request.form['ticker']
        app.vars['month'] = request.form['month']

	stock_plot(app.vars['ticker'],app.vars['month'])
	
        return redirect('/next')

@application.route('/next',methods=['GET'])
def next():  

    return render_template('stock.html') 

if __name__ == "__main__":
    application.run(host='0.0.0.0')
