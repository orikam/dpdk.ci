import json
import repo_constants


class Classify(object):

    def __init__(self):
        rules_file = open("git-repositories.json",'r')
        self.rules = json.load(rules_file)

    def classify(self,patch):
        title = patch.get_name()
        files = patch.get_files()

        # get the list of repositories
        for rep in self.rules['repos']:
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
                        # print("found rep based on file = " + rep[repo_constants.NAME])
            if found:
                obj = {};
                obj[repo_constants.NAME] = rep[repo_constants.NAME]
                obj[repo_constants.ADDRESS] = rep[repo_constants.ADDRESS]
                obj[repo_constants.PRIORITY] = rep[repo_constants.PRIORITY]
                patch.set_repository(obj)
        found_repos = patch.get_repositorys();
        if (len(found_repos)==0):
            obj = {}
            rep  = self.rules['default']
            obj[repo_constants.NAME] = rep[repo_constants.NAME]
            obj[repo_constants.ADDRESS] = rep[repo_constants.ADDRESS]
            obj[repo_constants.PRIORITY] = rep[repo_constants.PRIORITY]
            patch.set_repository(obj)
            newlist = []
            newlist.append(obj)
        else:
            newlist = sorted(patch.get_repositorys(), key=lambda x: x[repo_constants.PRIORITY], reverse=False)
        patch.set_repository_list(newlist)
