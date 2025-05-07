import requests, os
code = '29yv-n3le'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/pioche bonome leo lola.py')
with open('pioche bonome leo lola.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/bonome.pyxres')
with open('bonome.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "pioche bonome leo lola.py"')
