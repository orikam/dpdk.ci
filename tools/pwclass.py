
import subprocess

class PatchWork(object):

    # def __init__(self):


    def query(self,param):
        p = subprocess.Popen('./pwclient '+ param, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return p.stdout.readlines()
        # for line in p.stdout.readlines():
        #     print line,

