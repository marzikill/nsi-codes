import requests, os
code = 'x83p-36dg'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/4.pyxres')
with open('4.pyxres', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/ndc.py')
with open('ndc.py', 'wb') as file:
    file.write(pyxres.content)
# print(py.content.decode())
os.system('pyxel run "ndc.py"')
