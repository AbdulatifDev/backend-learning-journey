from fastapi import FastAPI
app = FastAPI()
@app.get("/add/{number1}/{number2}")
def add(number1: int, number2: int):
    return  {'result': number1 + number2 }

@app.get("/subtract/{number1}/{number2}")
def subtract(number1: int, number2: int):
    return{'rusult': number1 - number2}

@app.get("/divide/{number1}/{number2}")
def divide(number1: int, number2: int):
    if(number2):
        return{'result': number1 / number2}
    else:
        return{'error': "0 ga bo‘lish mumkin emas"}

@app.get('/multiply/{num1}/{num2}')
def multiply(num1: int, num2: int):
    return{'rusult': num1 * num2}

@app.get('/power/{num1}/{num2}')
def power(num1: int, num2: int):
    return {'result': num1 ** num2}

@app.get('/max/{num1}/{num2}')
def max(num1: int, num2: int):
    if(num1>num2):
        return {'result': f'{num1} katta'}
    elif(num1<num2):
        return {'result': f'{num1} katta'}
    else:
        return {'result': 'sonlar teng'}
