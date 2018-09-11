import pyperclip

path = pyperclip.paste()
path = path.replace('\\', '//')


# name = 'zhouhuili'
pyperclip.copy(path)


# text = pyperclip.paste()
# print(text)
