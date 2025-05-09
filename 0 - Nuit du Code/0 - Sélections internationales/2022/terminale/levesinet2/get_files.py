import requests, os
code = 'aunh-kwcz'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/star captain.py')
with open('star captain.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/2.pyxres')
with open('2.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "star captain.py"')
