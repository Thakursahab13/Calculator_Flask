from flask import Flask,request,render_template,jsonify

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome Guys"


@app.route('/calculator',methods=['GET'])
def math_operation():
    operation=request.json['operation']
    number1=request.json['number1']
    number2=request.json['number2']

    if operation=='addition':
        result = int(number1)+int(number2)
    elif operation=='multiplication':
        result = int(number1)*int(number2)
    elif operation=='division':
        result = int(number1)/int(number2)
    else:
        result = int(number1)-int(number2)
    return jsonify(result)




if __name__=='__main__':
    app.run(debug=True)