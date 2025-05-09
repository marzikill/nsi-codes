import requests, os
code = 'cm2d-dzp3'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/Jeu_v4.py')
with open('Jeu_v4.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/1v12.pyxres')
with open('1v12.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "Jeu_v4.py"')
