import requests, os
code = 'cm2d-ut36'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/Nuit du c0de 2022V1.py')
with open('Nuit du c0de 2022V1.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/graphisme.pyxel.pyxres')
with open('graphisme.pyxel.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "Nuit du c0de 2022V1.py"')
