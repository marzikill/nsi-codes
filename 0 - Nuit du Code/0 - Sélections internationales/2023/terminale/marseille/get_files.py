import requests, os
code = 'pt4u-x2dz'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/2.pyxres')
with open('2.pyxres', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/ndc.py')
with open('ndc.py', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "2.pyxres"')
