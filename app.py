import json

from flask import ( Flask , render_template , redirect , request ,
                    url_for , make_response , jsonify )

app= Flask(__name__)
def get_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError :
        data = {}
    return data

@app.route('/')
def index():
    return render_template("index.html" , saves=get_data())

@app.route('/responsive')
def responsive():
    data = get_data()
    return render_template("reply.html" , saves=get_data())


@app.route('/save' , methods = ['POST'])
def saved():
    response = make_response(redirect(url_for('responsive')))
    data = get_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character' ,  json.dumps(data))
    return response

app.run(debug = True)
