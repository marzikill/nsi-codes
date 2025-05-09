import requests, os
code = 'x9tr-rayk'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/nuit_du_code.py')
with open('nuit_du_code.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/arthur_mathis.pyxres')
with open('arthur_mathis.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "nuit_du_code.py"')
