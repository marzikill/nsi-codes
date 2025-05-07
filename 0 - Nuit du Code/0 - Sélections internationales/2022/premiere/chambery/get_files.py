import requests, os
code = 'pcjb-kdwh'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/aim_training.py')
with open('aim_training.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/2.pyxres')
with open('2.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "aim_training.py"')
