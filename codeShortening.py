from js import document


def encode(code):
    code = code.replace('\t', ' ')
    code = code.replace('    ', ' ')
    try:
        res = code.encode('u8').decode('u16')
    except UnicodeDecodeError:
        code+="#"
        res = code.encode('u8').decode('u16')
    return "exec(bytes('" + res + "','u16')[2:])"

def display_length(code, res):
    code_length = len(code)
    result_length = len(res)
    if result_length < code_length:
        pyscript.write("code_length", 'length: ' + str(code_length)) 
        pyscript.write("result_length", 'length: ' + str(result_length))
    else:
        pyscript.write("code_length", '') 
        pyscript.write("result_length", '') 

def shorten(*ags, **kws):
    code = document.getElementById('code').value
    if len(code)==0:
        code="print('Hello World')"
    res = encode(code)
    pyscript.write("result", res) 
    display_length(code, res)





