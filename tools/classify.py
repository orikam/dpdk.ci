import json

class Classify(object):

    def __init__(self):
        rules_file = open("git-repositories.json",'r')
        self.rules = json.load(rules_file)

    def classify(self,patch):
        title = patch.get_name()
        files = patch.get_files()

        # get the list of repositories
        for rep in self.rules:
            found = False
            # run on all title rules
            for rule in rep['subject']:
                if title.find(rule)>-1:
                    found = True
                    # print("found rep based on title = " + rep['repo_name'])
            # run on all files rules
            for rule in rep['paths']:
                # print(rule)
                # run on all files
                for f in files:
                    if f.find(rule)>-1:
                        found = True
                        # print("found rep based on file = " + rep['repo_name'])
            if found:
                obj = {};
                obj['rep'] = rep['repo_name']
                obj['priority'] = rep['priority']
                patch.set_repository(obj)

        newlist = sorted(patch.get_repositorys(), key=lambda x: x['priority'], reverse=False)
        patch.set_repository_list(newlist)
