from prod.input_number import input_number
import matplotlib.pyplot as plt
import numpy as np



print("To end this app enter: .")
while True:
    symbol = input("Operation sing (+, -, *, /): ")
    if symbol == '.':
        break
    if symbol in ('+', '-', '*', '/'):
        a = input_number("a")
        b = input_number("b")
        if symbol == '+':
            print(a+b)
        elif symbol == '-':
            print(a-b)
        elif symbol == '*':
            print(a*b)
        elif symbol == '/':
            try:
                print(a/b)
            except:
                print("Please, don't divide by zero to avoid the collapse of Universe!")
    else:
        print("Hey, write a supported sign!")


print("Check this out!")

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()