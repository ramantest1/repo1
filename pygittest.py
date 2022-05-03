import subprocess
from pexpect import popen_spawn
#from github import Github
#g = Github("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")
#repos = g.get_user().get_repos()
#for repo in repos:
#    print(repo.name)
#user = g.get_user().login
#print(user)
#
user = "ramantest1"
password = "githubpython1"
cmd = "git fetch --all"
subprocess.call(cmd, shell=True)
cmd = "git switch QA"
subprocess.call(cmd, shell=True)
cmd = "git checkout origin/DEV DESIGN.txt"
subprocess.call(cmd, shell=True)
cmd = "git add DESIGN.txt"
subprocess.call(cmd, shell=True)
cmd = 'git commit -m "to QA"'
subprocess.call(cmd, shell=True)
cmd = "git push -u origin QA"
subprocess.call(cmd, shell=True)
