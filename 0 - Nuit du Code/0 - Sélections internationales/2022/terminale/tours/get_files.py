import requests, os
code = 'nprk-3d6c'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/NuitducodeLyceeChoiseulTours.py')
with open('NuitducodeLyceeChoiseulTours.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/5.pyxres')
with open('5.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "NuitducodeLyceeChoiseulTours.py"')
