from config import app,jsonify
import requests

@app.route('/classify-number/<int:number>')
def classify_number(number):
    
    if str(number).isalpha:
        return jsonify({
            "number": "alphabet",
            "error": True
            }),400
    
    properties=[]
    if check_armstrong(number):
        properties.append("armstrong")
    
    properties.append(check_odd_even(number))
    
    return jsonify({
        "number": number,
        "is_prime": check_prime(number)=="prime",
        "is_perfect": check_prime(number)=="perfect",
        "properties": f"{properties}",
        "digit_sum": digit_sum(number),
        "fun_fact": requests.get(f"http://numbersapi.com/{number}/math?callback=showNumber").text
        
    }),200
    
    
    
def check_odd_even(num):
    if num%2!=0:
        return "odd"
    else:
        return "even"

    
def check_prime(num):
    if num%2!=0 or num==2:
        return "prime"
    else:
        return "perfect"
    
def digit_sum(num):
    add=0
    for i in range (len(str(num))):
        add+=int(str(num)[i])
    return add

def check_armstrong(num):
    add=0
    for i in range (len(str(num))):
        add+=int(str(num)[i])**int(str(num)[0])
    
    if add==num:
        return True
    return False
    
    
app.run(debug=True)
