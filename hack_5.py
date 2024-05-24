"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    tabla_traduccion = str.maketrans({
        'o': '0',
        'i': '1',
        'a': '@'
    })
    return result.translate(tabla_traduccion)
  