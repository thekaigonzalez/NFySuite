import subprocess


import os

for path, subtdir, files in os.walk("."):
    for file in files:
        if file.endswith(".md"):
            
            fname = file[file.find("\\")+1:file.rfind('.')]
            print(path + fname)
            subprocess.run(["pandoc", path + "\\" + file, "--self-contained", "--css=style.css", "-o", path + '\\' + fname + ".html"])