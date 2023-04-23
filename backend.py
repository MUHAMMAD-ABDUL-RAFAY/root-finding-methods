from math import *
import numpy as np
import os
import glob
import re
import string
import re
from flask import Flask, request, render_template,jsonify
import sympy as smp
from scipy.misc import derivative

def calcrootbissection(e,a,b,epsilon,count):
    result = []
    i = 1
    while True:
        mid_val = float((a+b)/2)
        x = mid_val
        func_c = eval(e)
        if func_c == 0 or abs(float(func_c)) <= float(epsilon):
            result.append([round(a,count+2),round(b,count+2),round(mid_val,count+2),round(func_c,count+2)])
            #print(round(a,count)," ",round(b,count)," ",round(mid_val,count)," ",round(func_c,count))
            break
        if func_c < 0:
            result.append([round(a,count+2),round(b,count+2),round(mid_val,count+2),round(func_c,count+2)])
            #print(round(a,count)," ",round(b,count)," ",round(mid_val,count)," ",round(func_c,count))
            a = mid_val
            i = i + 1
            continue
        if func_c > 0:
            result.append([round(a,count+2),round(b,count+2),round(mid_val,count+2),round(func_c,count+2)])
            #print(round(a,count)," ",round(b,count)," ",round(mid_val,count)," ",round(func_c,count))
            b = mid_val
            i = i + 1
            continue
    #print("THE ROOT IS : ",round(mid_val,count)," AFTER ",i," ITERATIONS")
    return (result,round(mid_val,count+2),i)

def calcrootregulafalsi(e,a,b,epsilon,count):
    print(e)
    i = 1
    result = []
    while True:
        x = a
        f_a = eval(e)
        x = b
        f_b = eval(e)
        if (f_b - f_a) == 0:
            break
        num = float(((a)*(f_b) - (b)*(f_a)))
        den = float(((f_b) - (f_a)))
        mid_val = float(num/den)
        x = mid_val
        func_c = eval(e)
        if func_c == 0 or abs(float(func_c)) <= float(epsilon):
            result.append([round(a,count+2),round(b,count+2),round(mid_val,count+2),round(func_c,count+2)])
            #print(round(a,count)," ",round(b,count)," ",round(mid_val,count)," ",round(func_c,count))
            break
        if func_c < 0:
            result.append([round(a,count+2),round(b,count+2),round(mid_val,count+2),round(func_c,count+2)])
            #print(round(a,count)," ",round(b,count)," ",round(mid_val,count)," ",round(func_c,count))
            a = mid_val
            i = i + 1
            continue
        if func_c > 0:
            result.append([round(a,count+2),round(b,count+2),round(mid_val,count+2),round(func_c,count+2)])
            #print(round(a,count)," ",round(b,count)," ",round(mid_val,count)," ",round(func_c,count))
            b = mid_val
            i = i + 1
            continue
    #print(result,round(mid_val,count),i)
    return (result,round(mid_val,count+2),i)
    #print("THE ROOT IS : ",round(mid_val,count)," AFTER ",i," ITERATIONS")

def calcrootsecant(e,a,b,epsilon,count):
    result = []
    i = 1
    while True:
        x = a
        f_a = eval(e)
        x = b
        f_b = eval(e)
        if (f_b - f_a) == 0:
          break
        num = float(((a)*(f_b) - (b)*(f_a)))
        den = float(((f_b) - (f_a)))
        mid_val = float(num/den)
        x = mid_val
        func_c = eval(e)
        if func_c == 0 or abs(float(func_c)) <= float(epsilon):
          i = i + 1
          result.append([round(a,count+2),round(b,count+2),round(mid_val,count+2),round(func_c,count+2)])
          #print(format(a,".4f")," ",format(b,".4f")," ",format(mid_val,".4f")," ",format(func_c,".4f"))
          break
        result.append([round(a,count+2),round(b,count+2),round(mid_val,count+2),round(func_c,count+2)])
        #print(format(a,".4f")," ",format(b,".4f")," ",format(mid_val,".4f")," ",format(func_c,".4f"))
        a = b
        b = mid_val
        i = i + 1
    return (result,round(mid_val,count+2),i)
    #print("THE ROOT IS : ",round(mid_val,count)," AFTER ",i," ITERATIONS")


app = Flask(__name__)
app.debug = True
@app.route('/')
def index():
    #returning the index.html page on '/' request
    return render_template('/index.html')

@app.route('/HomePage')
def home_page():
    return render_template('/index.html')

@app.route('/BissectionPage')
def bissection_page():
    return render_template('/bissect.html')

@app.route('/RegulaFasliPage')
def regulafalsi_page():
    return render_template('/regulafalsi.html')

@app.route('/NewtonPage')
def newton_page():
    return render_template('/newton.html')

@app.route('/SecantPage')
def secant_page():
    return render_template('/secant.html')


@app.route('/bissectionmethod',methods=["POST"])
def bissection_calc():
    data = request.get_json()
    e = data['expression']
    a = float(data['first_interval'])
    b = float(data['second_interval'])
    epsilon = float(data['tolerance_value'])
    e = e.replace("sin" , "np.sin")
    e = e.replace("cos" , "np.cos")
    e = e.replace("exp" , "np.exp")
    e = e.replace("tan" , "np.tan")
    e = e.replace("sqrt" , "np.sqrt")
    e = e.replace("ln","np.log")
    e = e.replace("pi","np.pi")
    print(e)
    x = a
    ans1 = eval(e)
    x = b
    ans2 = eval(e)
    if (ans1*ans2) >= 0:
        response_data = {'message': 'error',
                         'error': 'Wrong interval entered'}
        return jsonify(response_data)
        #print("WRONG INTERVAL ENTERED : ")
    roundoff = epsilon
    count = 0
    if epsilon != '':
        while(True):
            if roundoff >= 1:
                break;
            else:
                roundoff = roundoff * 10
                count = count + 1;
    else:
        count = 3
    if ans1 < 0:
        table, ans, iterations = calcrootbissection(e,a,b,epsilon,count)
    else:
        table, ans, iterations = calcrootbissection(e,b,a,epsilon,count)
    #sending results back to front-end to display to user
    response_data = {'message': 'ok',
                     'table': table,
                     'ans': ans,
                     'iterations': iterations}
    return jsonify(response_data)


@app.route('/regulafalsimethod',methods=["POST"])
def regulafalsi_calc():
    data = request.get_json()
    e = data['expression']
    a = float(data['first_interval'])
    b = float(data['second_interval'])
    epsilon = float(data['tolerance_value'])
    e = e.replace("sin" , "np.sin")
    e = e.replace("cos" , "np.cos")
    e = e.replace("exp" , "np.exp")
    e = e.replace("tan" , "np.tan")
    e = e.replace("sqrt" , "np.sqrt")
    e = e.replace("ln","np.log")
    e = e.replace("pi","np.pi")
    x = a
    ans1 = eval(e)
    x = b
    ans2 = eval(e)
    if (ans1*ans2) >= 0:
        response_data = {'message': 'error',
                         'error': 'Wrong interval entered'}
        return jsonify(response_data)
        #print("WRONG INTERVAL ENTERED : ")
    roundoff = epsilon
    count = 0
    if epsilon != '':
        while(True):
            if roundoff >= 1:
                break;
            else:
                roundoff = roundoff * 10
                count = count + 1;
    else:
        count = 3
    if ans1 < 0:
        table, ans, iterations = calcrootregulafalsi(e,a,b,epsilon,count)
    else:
        table, ans, iterations = calcrootregulafalsi(e,b,a,epsilon,count)
    #sending results back to front-end to display to user
    response_data = {'message': 'ok',
                     'table': table,
                     'ans': ans,
                     'iterations': iterations}
    return jsonify(response_data)

@app.route('/newtonmethod',methods=["POST"])
def newton_calc():
    result = []
    data = request.get_json()
    e = data['expression']
    a = float(data['first_interval'])
    b = float(data['second_interval'])
    epsilon = float(data['tolerance_value'])
    x = smp.Symbol('x')
    e1 = smp.diff(e,x)
    e2 = str(e1)
    e = e.replace("sin" , "np.sin")
    e = e.replace("cos" , "np.cos")
    e = e.replace("exp" , "np.exp")
    e = e.replace("tan" , "np.tan")
    e = e.replace("sqrt" , "np.sqrt")
    e = e.replace("ln","np.log")
    e = e.replace("pi","np.pi")
    e2 = e2.replace("sin" , "np.sin")
    e2 = e2.replace("cos" , "np.cos")
    e2 = e2.replace("exp" , "np.exp")
    e2 = e2.replace("tan" , "np.tan")
    e2 = e2.replace("sqrt" , "np.sqrt")
    e2 = e2.replace("ln","np.log")
    e2 = e2.replace("pi","np.pi")
    x = a
    ans1 = eval(e)
    x = b
    ans2 = eval(e)
    if (ans1*ans2) >= 0:
        response_data = {'message': 'error',
                         'error': 'Wrong interval entered'}
        return jsonify(response_data)
        #print("WRONG INTERVAL ENTERED : ")
    x = (a+b)/2
    point = x
    roundoff = epsilon
    count = 0
    while(True):
        if roundoff >= 1:
            break;
        else:
            roundoff = roundoff * 10
            count = count + 1
    i = 1
    while True:
        num = eval(e)
        den = eval(e2)
        if den == 0:
            break
        else:
            prev_val_x = x
            x_new = x - (num/den)
            if abs(float(prev_val_x) - float(x_new)) <= float(epsilon):
                result.append([round(x,count+2),round(x_new,count+2)])
                #print(format(x,".4f")," ",format(x_new,".4f"))  
                break
            result.append([round(x,count+2),round(x_new,count+2)])
            #print(format(x,".4f")," ",format(x_new,".4f"))
            x = x_new
            i = i + 1
            continue
    #print("THE ROOT IS : ",round(x_new,count)," AFTER ",i," ITERATIONS AT POINT : ",round(point,count))
    response_data = {'message': 'ok',
                     'table': result,
                     'ans': round(x_new,count+2),
                     'point':round(point,count+2),
                     'iterations': i}
    return jsonify(response_data)




@app.route('/secantmethod',methods=["POST"])
def secant_calc():
    data = request.get_json()
    e = data['expression']
    a = float(data['first_interval'])
    b = float(data['second_interval'])
    epsilon = float(data['tolerance_value'])
    e = e.replace("sin" , "np.sin")
    e = e.replace("cos" , "np.cos")
    e = e.replace("exp" , "np.exp")
    e = e.replace("tan" , "np.tan")
    e = e.replace("sqrt" , "np.sqrt")
    e = e.replace("ln","np.log")
    e = e.replace("pi","np.pi")
    x = a
    ans1 = eval(e)
    x = b
    ans2 = eval(e)
    if (ans1*ans2) >= 0:
        response_data = {'message': 'error',
                         'error': 'Wrong interval entered'}
        return jsonify(response_data)
        #print("WRONG INTERVAL ENTERED : ")
    roundoff = epsilon
    count = 0
    while(True):
        if roundoff >= 1:
            break;
        else:
            roundoff = roundoff * 10
            count = count + 1;
    if ans1 < 0:
      table,ans,iterations = calcrootsecant(a,b,epsilon,count)
    else:
      table,ans,iterations = calcrootsecant(b,a,epsilon,count)
    

if __name__ == '__main__':
    #starting the app
    app.run(debug=True)