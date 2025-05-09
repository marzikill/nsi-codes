import requests, os
code = '6z5e-9gmz'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/GrowyGardens.py')
with open('GrowyGardens.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/GrowyGardens.pyxres')
with open('GrowyGardens.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "GrowyGardens.py"')
