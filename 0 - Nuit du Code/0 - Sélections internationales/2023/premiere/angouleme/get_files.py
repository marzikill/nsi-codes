import requests, os
code = 'bqp5-7zaj'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/ndc.py')
with open('ndc.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/theme.pyxres')
with open('theme.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "ndc.py"')
