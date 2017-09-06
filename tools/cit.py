#!/usr/bin/env python
import patch_list
import argparse
import git_control
import os

# id for testing
#id 27075 next-net
#id 26987 next-eventdev

# debug getting list from patchwork
# pw = pwclass.PatchWork()
#
# test = pw.query('list -n 5')
#
# for line in test:
#     print line


# debug gettign on patch info
# patch = patch.Patch('269870')
# res = patch.load_info()
# if res == patch.PATCH_FOUND:
#     patch.download()
#     files = patch.get_files()
#
#     for name in files:
#         print name
#
#     classifier = classify.Classify()
#     classifier.classify(patch)

# debug getting number of patchs
# plist = patch_list.PatchList()
# plist.pull_patch_list(26986,100)

def check_patchs(base_dir, patchs):
	for patch in patchs:
    	# git_control.clone('https://github.com/jlowin/git-sync.git', '/labhome/orika/mtr/temp/cli_repos/debug')
		git_control.reset(patch.get_repo_address(), os.path.join(base_dir,patch.get_repo_name()))
		git_control.apply(os.path.join(base_dir,patch.get_repo_name()),patch.get_id())

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("base_dir", type=str, help="the base folder for the repos")
	parser.add_argument("start", type=int, help="the first patch id to get")
	parser.add_argument("number", type=int, help="the number of patches to analyze")
	args = parser.parse_args()
	plist = patch_list.PatchList()
	plist.pull_patch_list(args.start,args.number)
	patchs = plist.get_patch_list()
	print("number of patches = " + str(len(patchs)))
	check_patchs(args.base_dir,patchs)


if __name__ == "__main__":
    main()


# retval = p.wait()
