from flask import Flask, render_template,send_file

app1 = Flask(__name__)

@app1.route('/')
def home():
    return render_template("home.html")

@app1.route('/about')
def about():
    return render_template("about.html")

@app1.route('/contact')
def contact():
    return render_template("contact.html")

@app1.route('/resume')
def resume():
    return send_file('static/Resume.pdf', as_attachment=True)

if __name__ =="__main__":
    app1.run(debug=True)