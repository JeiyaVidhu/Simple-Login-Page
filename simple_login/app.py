from flask import Flask, render_template, request

app = Flask(
    __name__,
    template_folder='client/templates',

)

@app.route("/",methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['nm']
        return "Hello "+ name +""



if __name__ == '__main__':
    app.run(debug=True)