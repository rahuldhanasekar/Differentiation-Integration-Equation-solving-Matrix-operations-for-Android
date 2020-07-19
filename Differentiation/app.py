import toga
from toga.style.pack import *

# Importing sympy library
from sympy import *
import sympy


# Defining symbols

x, y, z = symbols('x y z')


def build(app):
    var_box = toga.Box()
    eq_box = toga.Box()
    diff_box = toga.Box()
    ans_box = toga.Box()
    box = toga.Box()

    var_input = toga.TextInput()
    eq_input = toga.TextInput()
    diff_input = toga.TextInput()
    ans_input = toga.TextInput(readonly=True)

    var_label = toga.Label('No. of variables', style=Pack(text_align=CENTER))
    eq_label = toga.Label('Equation', style=Pack(text_align=CENTER))
    diff_label = toga.Label('With respect to?', style=Pack(text_align=RIGHT))
    ans_label = toga.Label('Result', style=Pack(text_align=CENTER))

    def differentiation(widget):
        try:
            ans_input.value = sympy.diff(eq_input.value, x)
        except:
            ans_input.value = '???'

    button = toga.Button('Calculate', on_press=differentiation)

    var_box.add(var_label)
    var_box.add(var_input)

    eq_box.add(eq_label)
    eq_box.add(eq_input)

    diff_box.add(diff_label)
    diff_box.add(diff_input)

    ans_box.add(ans_label)
    ans_box.add(ans_input)

    box.add(var_box)
    box.add(eq_box)
    box.add(diff_box)
    box.add(button)
    box.add(ans_box)

    box.style.update(direction=COLUMN, padding_top=10)
    var_box.style.update(direction=ROW, padding=5)
    eq_box.style.update(direction=ROW, padding=5)
    diff_box.style.update(direction=ROW, padding=5)
    ans_box.style.update(direction=ROW, padding=5)

    var_input.style.update(flex=1, padding_left=50, padding_right=50)
    ans_input.style.update(flex=1, padding_left=50, padding_right=50)
    diff_input.style.update(flex=1, padding_left=50, padding_right=50)
    eq_input.style.update(flex=1, padding_left=50, padding_right=50)
    var_label.style.update(width=100, padding_left=30)
    ans_label.style.update(width=100, padding_left=30)
    diff_label.style.update(width=100, padding_left=30)
    eq_label.style.update(width=100, padding_left=30)

    button.style.update(padding=15, flex=1)

    return box


def main():
    return toga.App('Differentiation', 'org.beeware.diff', startup=build)


if __name__ == '__main__':
    main().main_loop()


