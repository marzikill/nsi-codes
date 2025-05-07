import requests, os
code = 'xf38-q42m'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/images.pyxres')
with open('images.pyxres', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/jeux fischou.py')
with open('jeux fischou.py', 'wb') as file:
    file.write(pyxres.content)
# print(py.content.decode())
os.system('pyxel run "jeux fischou.py"')
