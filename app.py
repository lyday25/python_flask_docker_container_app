from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello():
   return "Hello, Welcome on board Flight A768!"
 
@app.route('/create')
def create():
   a=9
   b=5
   c=7
   d=a*b*c
   return "This is the result " + str(d)
 
if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5006, debug =True)