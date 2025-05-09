import requests, os
code = 'aunh-89cs'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/main.py')
with open('main.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/main.pyxres')
with open('main.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "main.py"')
