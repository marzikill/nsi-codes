import requests, os
code = 'tbxc-vw2d'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/jeu_nuit_code.py')
with open('jeu_nuit_code.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/1.pyxres')
with open('1.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "jeu_nuit_code.py"')
