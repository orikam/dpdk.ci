import subprocess

def clone(git_url,target_folder):
    res = subprocess.call("git clone "+ git_url + " " + target_folder, shell=True)

def reset(target_folder):
    res = subprocess.call("git fetch origin", shell=True, cwd=target_folder)
    res = subprocess.call("git reset --hard origin/master", shell=True, cwd=target_folder)