import patch
import classify

class PatchList:
    def __init__(self):
        self.patches = []
        self.classifier = classify.Classify()

    def pull_patch_list(self,start,number):
        for i in range (start,start+number):
            # print ('downloading patch id: ' + str(i))

            p = patch.Patch(str(i))
            res = p.load_info()
            if res == p.PATCH_FOUND:
                if res == p.PATCH_FOUND:
                    self.classifier.classify(p)
                    self.patches.append(p)
                    p.log_info()

    def get_patch_list(self):
        return self.patches
