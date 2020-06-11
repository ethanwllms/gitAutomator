from git import Repo

def cloneRepo(git_url, repo_dir):
    try:
        repo = Repo.clone_from(git_url, repo_dir)
    except OSError:
        print("FAILED to clone repo from: %s" % git_url)
    else:
        print("Cloned repo from: %s ..." % git_url)
        return repo


def checkoutBranch(repo, new_branch):
    try:
        repo.git.checkout('-b', new_branch)
    except NameError:
        print("FAILED to create new branch.")
    else:
        print("Created new branch...")

def addChanges(repo, file):
    try:
        repo.git.add(file, update=True)
    except ValueError:
        print("FAILED to add item to tracked files. [SHA or MODE do not match previous file]")
        # "Ref: https://gitpython.readthedocs.io/en/stable/reference.html#git.objects.tree.TreeModifier.add"
    else:
        print("Added adding of file to tracked items.")
        return repo

def commitAndPush(repo, Commit_MSG, new_branch):
    try:
        repo.git.commit('-m', Commit_MSG)
        repo.git.push('origin', new_branch)
    except:
        print("FAILED to push branch to remote.")
    else:
        print("SUCCESSFUL push of new branch to remote.")