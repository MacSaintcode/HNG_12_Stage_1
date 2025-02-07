from config import Flask,jsonify,request,CORS,requests,app


@app.route('/api/classify-number')
def classify_number():
    
    number = request.args.get('number')
        
    if not (str(number).isdigit()):
        return jsonify({
            "number": f"{number}",
            "error": True
            }),400
   

    number = int(number)
    
    properties=[]
    if check_armstrong(number):
        properties.append("armstrong")
    
    properties.append(check_odd_even(number))
    
    return jsonify({
        "number": number,
        "is_prime": check_prime(number)=="prime",
        "is_perfect": check_prime(number)=="perfect",
        "properties":properties,
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
        add+=int(str(num)[i])**(len(str(num)))
        print(add)
    if add==num:
        return True
    return False
    
if __name__ == "__main__":
    app.run(debug=True)
