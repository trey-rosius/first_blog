from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', name='Rosius')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    #return '<h1 style="color:green; text-align:center;"> Contact Page</h1>'


if __name__ =="__main__":
    app.run(port=5000,debug=True)