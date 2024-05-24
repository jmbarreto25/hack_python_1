"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result= result.upper()
    tabla_traduccion = str.maketrans({
        'O': '0',
        'I': '1',
        'A': '@'
    })
    
    result_trad = result.translate(tabla_traduccion)

    lista_result=[]

    for char in result_trad:
        # Agrega cada carácter a la lista_resultado
        lista_result.append(char)
    result=lista_result
    return result


    