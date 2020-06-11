import os, shutil, json
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove

def createStringDict():
    try:
        strings = {}
        cwd = os.getcwd()
        repo_dir = cwd + '/test/'
        file = 'sample-pipelines.yml'
        file_path = repo_dir + file
        config_file = "config.json"

        configs = readConfig(config_file)
        new_branch = (configs['Client'] + "-" + configs['Destination-Environment']).lower()
        Commit_MSG = "Adding branch for %s with updated pipeline." % new_branch
        function = 'Whatchamacallit'
        strings.update({"repo_dir": repo_dir, "new_branch": new_branch, "file_path": file_path, "file": file,
                        "Commit_MSG": Commit_MSG, "function": function, "Client-Info": configs})
        # print(strings)
    except:
        print("FAILED to produce value dictionary...")
    else:
        print("Added values to dictionary...")
        return strings

def readConfig(config_file):
    try:
        print("Reading JSON from config file...")
        with open(config_file) as f:
            data = json.load(f)
        # print(data)
    except:
        print("FAILED to read JSON from config file...")
    else:
        print("JSON config data read in...")
        return data

def createDir(repo_dir):
    try:
        os.mkdir(repo_dir)
    except OSError:
        print("FAILED to create directory: %s" % repo_dir)
    else:
        print("Added directory: %s ..." % repo_dir)

def removeDir(repo_dir):
    try:
        shutil.rmtree(repo_dir)
    except OSError:
        print("FAILED to delete directory: %s" % repo_dir)
    else:
        print("Deleted directory: %s ..." % repo_dir)

def replaceFunction(file_path, target_function, new_function):
    fh, abs_path = mkstemp()
    try:
        with fdopen(fh, 'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    new_file.write(line.replace(target_function, new_function))
        copymode(file_path, abs_path)
        remove(file_path)
        move(abs_path, file_path)
        # file_path.close()
        old_file.close()
        new_file.close()
    except:
        print("FAILED to replace function name within: %s ..." % file_path)
    else:
        print("Replaced function name...")

def gatherFunctions(strings):
    try:
        functions = strings["Client-Info"]["Functions"]
        print(functions)
    except:
        print("FAILED to return separate function information.")
    else:
        print("Function information has been separated...")
        return functions