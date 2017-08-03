import pwclass
import subprocess

class Patch(object):

    PATCH_NOT_FOUND = -1
    PATCH_FOUND = 0

    def __init__(self,patch_id):
        self.patch_id = patch_id
        self.data = {}
        self.files = []
        self.repositories = []
        self.pw = pwclass.PatchWork()

    def load_info(self):
        raw_info = self.pw.query('info '+ self.patch_id)
        if len(raw_info) == 0:
            return self.PATCH_NOT_FOUND;
        self.parse_info(raw_info)
        self.load_file_list()
        return self.PATCH_FOUND;

    def parse_info(self,info):
        for line in info:
            # remove the starting '-'. make sure that we split only once since there is
            # possiblity to have this char else where
            temp = line.split('-',1)

            if len(temp) == 2:
                # split according to ':' like before me must only split once
                temp = temp[1].split(':',1)
                if(len(temp) == 2):
                    # remove spaces
                    key = self.trim_spaces(temp[0])
                    value  = self.trim_spaces(temp[1])
                    # insert line into object
                    self.data[key] = value

    # download and extract the file list from the patch
    def load_file_list(self):
        res = self.download()
        if res == self.PATCH_NOT_FOUND:
            return res
        self.extract_file_list()
        self.delete_file()

    # used in order to get the files related to this patch
    def download(self):
        res = self.pw.query('get ' + str(self.patch_id))
        if len(res) == 0:
            return self.PATCH_NOT_FOUND;
        return self.PATCH_FOUND

    def delete_file(self):
        p = subprocess.Popen('rm ' + self.data['filename'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def extract_file_list(self):
	f = open(self.data['filename'], 'r')
        data = f.readlines()
        for line in data:
            values = line.split('+++');
            if len(values) == 2:
                file_name = self.trim_spaces(values[1])
                self.files.append(file_name)

    def get_name(self):
        return self.data['name']

    def get_files(self):
        return self.files
    # add one repository to the repository array
    def set_repository(self,rep):
        self.repositories.append(rep)

    # replace the repository list with a new list
    def set_repository_list(self,rep_list):
        self.repositories = rep_list;

    def get_repositorys(self):
        return self.repositories

    def get_id(self):
        return self.patch_id

    def trim_spaces(self,string):
        res = string.lstrip()
        res = res.rstrip();
        return res

    def log_info(self):
        print ('========================')
        print ('Patch ID: ' + self.get_id())
        print ('Title: ' + self.get_name())
        print ('Files:')
        for f in self.get_files():
            print(f)
        print ('Reposetories: ')
        if len(self.get_repositorys()) > 0:
            for r in self.get_repositorys():
                print (r['rep'] +',' + str(r['priority']))
        else:
            print ('no repository found')
