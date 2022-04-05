import subprocess


import glob

for file in glob.glob("./*.md"):
    fname = file[file.find("\\")+1:file.rfind('.')]
    subprocess.run(["pandoc", file, "--self-contained", "--css=style.css", "-o", fname + ".html"])