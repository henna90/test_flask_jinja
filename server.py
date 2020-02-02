from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route('/')
# def index_page():
#     return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def greet_person():
    if request.method == 'GET':
        return render_template('index.html')

    else :
        # person = request.args.get("person")
        person = request.form['person'] 

        return render_template('index.html', person=person)  


if __name__ == '__main__':
    app.run(debug=True)