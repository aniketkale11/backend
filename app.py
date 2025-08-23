from flask import Flask , request ,     jsonify


app = Flask(__name__)

@app.route("/",methods = ['GET'])
def home ():
    return "hello World"


@app.route('/api', methods = ['GET','POST'])
def api ():
    if request.method == 'POST':

            name = request.form.get('name')
            password = request.form.get('password')
            gmail =request.form.get('gmail')  
 
              
        
            return  jsonify ( {
                 'meassage':'User Registerd Successfully',
                 'Name':name,
                 'Password':password,
                 'Gamil':gmail


            })
    return "Data is not Come"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3000,debug=True)