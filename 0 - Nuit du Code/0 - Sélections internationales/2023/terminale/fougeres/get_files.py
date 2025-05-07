import requests, os
code = 'zrnl-82lw'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/main.py')
with open('main.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/my_resource.pyxres')
with open('my_resource.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "main.py"')
