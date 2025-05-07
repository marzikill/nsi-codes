import requests, os
code = '8cls-ymhp'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/NUIT DU CODE.py')
with open('NUIT DU CODE.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/tokyores.pyxres')
with open('tokyores.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "NUIT DU CODE.py"')
