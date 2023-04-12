import os
directory = os.getcwd()
files = os.listdir(directory)
for file in files:
    if file.endswith(".jack"):
        path = os.path.join(directory, file)
        os.system("JackCompiler.bat " + path)
os.system("pause")
