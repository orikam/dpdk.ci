import subprocess
import os

def clone(git_url,target_folder):
	res = os.path.isdir(target_folder)
	print("folder exist = "+str(res))
	if res == False:
		os.makedirs(target_folder)
	res = subprocess.call("git clone "+ git_url + " " + target_folder, shell=True)

def reset(git_url, target_folder):
	if os.path.isdir(target_folder) == False:
		clone(git_url, target_folder)
	else:
		subprocess.call("git fetch origin", shell=True, cwd=target_folder)
		subprocess.call("git reset --hard origin/master", shell=True, cwd=target_folder)

def apply(target_folder,patch_id):
	cwd = os.getcwd()
	os.chdir(target_folder)
	debug = os.path.join(cwd,'pwclient') +' git-am ' + patch_id 
	print("line to run: " + debug)
	print("current dir: " + str(os.getcwd()))
	subprocess.call(debug,shell=True )
		
