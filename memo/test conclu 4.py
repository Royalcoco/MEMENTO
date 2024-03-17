-@__file__?, '.join(os.listdir('.'))
    print 'files in current directory:', files
    
    # get the list of directories that contain a file with the extension ".py" 
    dirs_with_python = [d for d in os.listdir('.') if any([f.endswith(".py") for f in os.listdir(d)])]
    print '\ndirectories containing python files:\n', dirs_with_python
     # create a new folder named "newfolder" and add it to the list of directories
    os.mkdir("newfolder")
    dirs_with_python.append("newfolder")
    print 'directories including newly created folder ' + '"newfolder":\n', dirs_with_python
    
    # iterate over all subfolders (recursively), printing out their full paths
    for path in [os.path.join('.', d, s) for d in dirs_with_python for s in os.listdir(os.path.join('.', d))] :
    def show_subfolders(startpath):
        """Print out the full path of every subfolder within startpath."""
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count('/')
            indent = ' ' * (level * 2)
            print '{:>6}PATH: {}'.format(' ', root)
            
    show_subfolders('./' + dirs_with_python[ -1 ])   # start from the last directory added to dirs_with_python that was added before  the first
    print '\nshowing subfolders recursively from current directory:'
    show_subfolders('.')

if __name__ == "__main__":
    main() relpath *dirs_with_python* is not working properly. It returns relative paths instead of absolute ones. I tried using absp
    main() relpath *dirs_with_python* is not working as expected when I run this script from another location on my system
    main() relpath *dirs_with_python* is not working properly? I tried using absp instead of abs but still no luck..
    main() relpath *dirs_with_python* are relative to the script's location</ s> **Upload.MAJ_'-SystemExit.code;function °)
    main() °)(__loader__.try _to_load_module(__name__)).main
    @cont))]cont]inue('" = models.EmailField()  is not defined
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax
import os

def read_html(filename):
    with open(filename, 'r') as f:
        html = f.read()
    return html

def find_paragraphs(html):
    start = html.find('<p>')
    while start != -1:
        end = html.find('</p>', start) + len('</p>')
        yield html[start:end]
        start = html.find('<p>', end)
pyFilesDict = {}
    for d in dirs_with_python:
        fullpath = os.path.abspath(d)
        relpath = '/'.join(fullpath.split('/')[1:])   # remove the first "/", which is always empty because we're working on unix-like systems
        relpath = os.path.relpath(fullpath)
        pyFilesDict[relpath] = [(f, open(fullpath + '/' + f).read()) for f in os.listdir(fullpath) if f.endswith(".py")]
        pyFilesDict[relpath] = [(f, open(os.path.join(fullpath, f)).read()) for f in os.listdir(full path)]
print(pyFilesDict)
#for key, value in sorted(pyFilesDict.items(), key=lambda item:item[0]):
    #print "{}: \n{}".format(key, "\n".join([i[:50]+'...' if len(i)>53 else i for i in value]))

from bs4 import BeautifulSoup

def process_file(filecontent, filename):
    soup = BeautifulSoup(filecontent, 'html.parser')
    paragraphs = list(find_paragraphs(str(soup)))
    numParas = len(paragraphs)
    if numParas > 0:
        print("{}: {} paragraphs".
        format(filename, numParas))
    else:
        print("{}: no paragraphs".format(filename))

for k, v in pyFilesDict.items():? import    TypeError'********************************  '  ********************************    return {'numParas': numParas    return {'numParas': numParas
for k, v in pyFilesDict.items():
    for file in v:
        process_file(v[file], file)
\
    for fileinfo in v:
        name, content = fileinfo
        process_file(content, name)
\
    '''
    This script reads all the Python files in a given directory (or directories), and prints out how many paragraphs are in each one. It also prints out
    This script reads the HTML from a given set of Python source files and prints out how many paragraph tags are present in each file. It uses the following
    This script reads all the Python files in a given directory (or directories), and prints out how many paragraphs are in each one. It
    This script reads all the Python source files in a given directory (or directories), and prints out how many paragraphs are contained within each one
    This script reads the HTML files listed in the provided text file and prints out a summary of each paragraph
    This script reads all the Python files in a given directory (or directories), and prints out how many paragraphs are in each one. It
    This function takes a string containing HTML and uses the Beautiful Soup library to parse it into a document object. It then finds all of the </p> elements
if __name__ == "__main__":
    filename = 'example.html'
    html = read_html(filename)
    for para in find_paragraphs(html):
        print(para)
        
    # create a dictionary where keys are directories and values are lists of tuples (filename, filecontent).
    # only consider .py files from the directories listed above. This is done by filtering out all other files. 
    # Each tuple contains the filename and its content as string.
    