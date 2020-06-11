import fileOps, gitOps, time

strings = fileOps.createStringDict()
fileOps.createDir(strings["repo_dir"])
functions = fileOps.gatherFunctions(strings)
for key, value in functions.items():
    FunctionName = key
    URL = value['URL']
    TargetFunct = value['Target-Function']
    print("Working on: %s" % FunctionName)
    repo = gitOps.cloneRepo(URL, strings["repo_dir"])
    gitOps.checkoutBranch(repo, strings["new_branch"])
    fileOps.replaceFunction(strings["file_path"], TargetFunct, strings["new_function"])
    time.sleep(3)
    gitOps.addChanges(repo, strings["file"])
    gitOps.commitAndPush(repo, strings["Commit_MSG"], strings["new_branch"])
    fileOps.removeDir(strings["repo_dir"])
    time.sleep(5)
