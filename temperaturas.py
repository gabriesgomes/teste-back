from flask import Flask
from flask import request


temp = Flask(__name__)

@temp.route('/')
def my_form():
    site = '''
<!DOCTYPE html>
<html>
<body>
    <h1>Conversor de Temperatura</h1>
    <p>Insira o valor de acordo com a unidade que deseja converter</p>
    <form action="Conversor" method="POST">
        <h5>C = Celsius / F = Fahrenheit / K = Kelvin </h5>
        <p>Unidade Origem:</p>
        <input type="text" name="origem">
        <p>Unidade Origem:</p>
        <input type="text" name="destino">
        <p>Valor para conversão</p>
        <input type="text" name="valor">
        <input type="submit" value="Convert">        
    </form>
</body>
</html>'''
    return site

@temp.route('/Conversor', methods=['POST'])
def post_cel_fahr():
    orig = request.form['origem']
    dest = request.form['destino']
    vlr = request.form['valor']
    try:
        vlr = float(vlr)
        tempConv = 0
        
        if orig == 'c'   and dest == 'f':
           tempConv = ((9*vlr)/5)+32
			
        elif orig == 'c' and dest == 'k':
           tempConv = vlr + 273.15
			
        elif orig == 'f' and dest == 'c':
           tempConv = (vlr - 32)*(5/9)
			
        elif orig == 'f' and dest == 'k':
           tempConv = ((vlr-32) * (5/9)) + 273.15
			
        elif orig == 'k' and dest == 'f':
           tempConv = ((vlr - 273.15)*(9/5)) + 32
			
        elif orig == 'k' and dest == 'c':
           tempConv = 273.15 - vlr
           
        return str(tempConv)	
    except:
        return "Não é um numero válido!"
        
if __name__ == '__main__':
    temp.run()
