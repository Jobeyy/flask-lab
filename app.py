from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def mainPage():
    name = "Jobey Farias"
    return render_template('base.html', name=name, aboutMe=readDetails('static\content.txt'))
    
def readDetails(filepath):
        with open(filepath, 'r') as f:
            return [line for line in f]
        
@app.route('/form', methods=['GET', 'POST'])
def formDemo():
     name= None
     if request.method == 'POST':
          name = request.form['name']
          return render_template('base.html', name=name, aboutMe=readDetails('static\moreContent.txt'))
          
     
     return render_template('form.html', name=name)

@app.route('/user/<name>')
def greet(name):
     return f"Hello {name}"
if __name__ == "__main__":
    app.run(debug=True)