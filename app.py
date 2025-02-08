from config import Flask,jsonify,request,CORS,requests,app


@app.route('/api/classify-number')
def classify_number():
    
    number = request.args.get('number')
        
    if number is None or number.strip() == "":
        return jsonify({"error": True, "number": ""}), 400

    try:
        number = int(number)
    except ValueError:
        return jsonify({"error": True, "number": number}), 400
    
    values={
         "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties":[],
        "digit_sum": digit_sum(number),
        "fun_fact": fun_facts(number)
    }
    
    if check_armstrong(number):
        values["properties"].append("armstrong")
    
    values["properties"].append(check_odd_even(number))
    
    
    return jsonify(values),200
        
    
def fun_facts(num):
    try:
        facts=requests.get(f"http://numbersapi.com/{num}/math?callback=showNumber")
        if facts.status_code==200:
            return facts.text
        else:
            return f"Fun fact Unavailable for {num}"
    except requests.RequestException:
        return f"Fun fact Unavailable!"
        
    
    
def check_odd_even(num):
    if num%2!=0:
        return "odd"
    else:
        return "even"

    
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Skipping numbers divisible by 2 and 3
    
    return True

def is_perfect(n):
    if n < 2:
        return False
    
    total = 1
    sqrt_n = int(n ** 0.5)

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Avoid adding the square root twice
                total += n // i
    
    return total == n

    
def digit_sum(num):
    add=0
    num=abs(num)
    for i in range (len(str(num))):
        add+=int(str(num)[i])
    return add

def check_armstrong(num):
    add=0
    num=abs(num)
    for i in range (len(str(num))):
        add+=int(str(num)[i])**(len(str(num)))
    if add==num:
        return True
    return False
    
if __name__ == "__main__":
    app.run(debug=True)
