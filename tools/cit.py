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

def check_patches(base_dir, patches):
    for patch in patches:
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
    patches = plist.get_patch_list()
    check_patches(args.base_dir,patches)


if __name__ == "__main__":
    main()


# retval = p.wait()
