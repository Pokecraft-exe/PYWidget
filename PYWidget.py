import os, subprocess, threading, sys

# check the widget folder for all widgets
widgets = []
path = sys.argv[0].replace('\\\\', '\\')
path = path[:path.rfind('\\')+1]
if os.path.exists(path+'widget'):
    for filename in os.listdir(path+'widget'):
        f = os.path.join(path+"widget\\", filename)
        # checking if it is a file
        if os.path.isfile(f):
            widgets.append(filename[:filename.rfind('.')])
else:
    print("Error: the folder 'widget' does not exist")
    exit()

def openfile(name):
    subprocess.Popen(name, shell=True)
    

thread = list()
# exeute the codeof all widgets
for j, i in enumerate(widgets):
    thread.append(threading.Thread(target=openfile, args=(f'python \"{path}widget\{i}.pyw\"',)))
    thread[j].start()
print("done")
