import toga
from toga.style.pack import *

# Importing sympy library
import sympy as sym
from sympy import *


# Defining symbols
x, y, z = symbols('x y z')

def build(app):
    eq1_box = toga.Box()
    eq2_box = toga.Box()
    eq3_box = toga.Box()
    ans1_box = toga.Box()
    ans2_box = toga.Box()
    ans3_box = toga.Box()
    box = toga.Box()


    eq1_input = toga.TextInput()
    eq2_input = toga.TextInput()
    eq3_input = toga.TextInput()
    ans1_input = toga.TextInput(readonly=True)
    ans2_input = toga.TextInput(readonly=True)
    ans3_input = toga.TextInput(readonly=True)

    
    eq1_label = toga.Label('Equation 1', style=Pack(text_align=RIGHT))
    eq2_label = toga.Label('Equation 2', style=Pack(text_align=RIGHT))
    eq3_label = toga.Label('Equation 3', style=Pack(text_align=RIGHT))
    ans1_label = toga.Label('Value of x', style=Pack(text_align=CENTER))
    ans2_label = toga.Label('Value of y', style=Pack(text_align=CENTER))
    ans3_label = toga.Label('Value of z', style=Pack(text_align=CENTER))
        
    
        
    def equation(widget):
        if(eq1_input.value is not None):
            l=[]
            ans1_input.value = sym.solveset(eq1_input.value,var)
        if(eq2_input.value is not None):
            solution = sym.solve((eq1_input.value,eq2_input.value),(var))
            ans1_input.value = solution[x]
            ans2_input.value = solution[y]
        if(eq3_input.value is not None):
            solution = sym.solve((eq1_input.value,eq2_input.value,eq3_input.value),(var))
            ans1_input.value = solution[x]
            ans2_input.value = solution[y]
            ans3_input.value = solution[z]
            
            
        

    button = toga.Button('Solve', on_press=equation)


        
    eq1_box.add(eq1_label)
    eq1_box.add(eq1_input)
    eq2_box.add(eq2_label)
    eq2_box.add(eq2_input)
    eq3_box.add(eq3_label)
    eq3_box.add(eq3_input)
        

    ans1_box.add(ans1_label)
    ans1_box.add(ans1_input)
    ans2_box.add(ans2_label)
    ans2_box.add(ans2_input)
    ans3_box.add(ans3_label)
    ans3_box.add(ans3_input)



    box.add(eq1_box)
    box.add(eq2_box)
    box.add(eq3_box)
    box.add(button)
    box.add(ans1_box)
    box.add(ans2_box)
    box.add(ans3_box)


    box.style.update(direction=COLUMN, padding_top=10)

    eq1_box.style.update(direction=ROW, padding=5)
    eq2_box.style.update(direction=ROW, padding=5)
    eq3_box.style.update(direction=ROW, padding=5)
    ans1_box.style.update(direction=ROW, padding=5)
    ans2_box.style.update(direction=ROW, padding=5)
    ans3_box.style.update(direction=ROW, padding=5)

    eq1_input.style.update(flex=1, padding_left=50, padding_right=50)
    eq2_input.style.update(flex=1, padding_left=50, padding_right=50)
    eq3_input.style.update(flex=1, padding_left=50, padding_right=50)
    ans1_input.style.update(flex=1, padding_left=50, padding_right=50)
    ans2_input.style.update(flex=1, padding_left=50, padding_right=50)
    ans3_input.style.update(flex=1, padding_left=50, padding_right=50)
    ans1_label.style.update(width=100, padding_left=30)
    ans2_label.style.update(width=100, padding_left=30)
    ans3_label.style.update(width=100, padding_left=30)
    eq1_label.style.update(width=100, padding_left=30)
    eq2_label.style.update(width=100, padding_left=30)
    eq3_label.style.update(width=100, padding_left=30)

    button.style.update(padding=15, flex=1)
    return box


def main():
    return toga.App('Equation Solving', 'org.beeware.eq', startup=build)


if __name__ == '__main__':
    main().main_loop()





