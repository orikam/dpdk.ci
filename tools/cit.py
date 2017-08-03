#!/usr/bin/env python
import patch_list
import argparse

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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start", type=int, help="the first patch id to get")
    parser.add_argument("number", type=int, help="the number of patches to analyze")
    args = parser.parse_args()
    plist = patch_list.PatchList()
    plist.pull_patch_list(args.start,args.number)


if __name__ == "__main__":
    main()


# retval = p.wait()
