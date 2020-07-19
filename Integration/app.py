import toga
from toga.style.pack import *

# Importing sympy library
from sympy import *
import sympy


# Defining symbols

x, y, z = symbols('x y z')


def build(app):
    eq_box = toga.Box()
    integ_box = toga.Box()
    ans_box = toga.Box()
    box = toga.Box()


    eq_input = toga.TextInput()
    integ_input = toga.TextInput()
    ans_input = toga.TextInput(readonly=True)

    eq_label = toga.Label('Equation', style=Pack(text_align=CENTER))
    integ_label = toga.Label('With respect to?', style=Pack(text_align=RIGHT))
    ans_label = toga.Label('Result', style=Pack(text_align=CENTER))

    def integration(widget):
        try:
            ans_input.value = integrate(eq_input.value, x)
        except:
            ans_input.value = '???'

    button = toga.Button('Calculate', on_press=integration)


    eq_box.add(eq_label)
    eq_box.add(eq_input)

    integ_box.add(integ_label)
    integ_box.add(integ_input)

    ans_box.add(ans_label)
    ans_box.add(ans_input)


    box.add(eq_box)
    box.add(integ_box)
    box.add(button)
    box.add(ans_box)

    box.style.update(direction=COLUMN, padding_top=10)

    eq_box.style.update(direction=ROW, padding=5)
    integ_box.style.update(direction=ROW, padding=5)
    ans_box.style.update(direction=ROW, padding=5)

    ans_input.style.update(flex=1, padding_left=50, padding_right=50)
    integ_input.style.update(flex=1, padding_left=50, padding_right=50)
    eq_input.style.update(flex=1, padding_left=50, padding_right=50)
    ans_label.style.update(width=100, padding_left=30)
    integ_label.style.update(width=100, padding_left=30)
    eq_label.style.update(width=100, padding_left=30)

    button.style.update(padding=15, flex=1)

    return box


def main():
    return toga.App('Integration', 'org.beeware.integ', startup=build)


if __name__ == '__main__':
    main().main_loop()



