import requests, os
code = 'tbxc-m6sv'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/nuit du code.finalpy.py')
with open('nuit du code.finalpy.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/perso.pyxres')
with open('perso.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "nuit du code.finalpy.py"')
