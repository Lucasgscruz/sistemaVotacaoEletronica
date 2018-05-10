import eel


@eel.expose
def my_python_function(a, b, input):
    print("Chamada de função funcionandoo...")
    print(a, b, a + b)
    print(input)

eel.init('mesario_gui')
eel.start('index.html')
