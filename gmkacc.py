#!/usr/bin/python3
import hashlib
import random
import src.names
import imaplib
import csv

class Gmkacc:
    def __init__(self):
        self.acc = []
        self.pss = []
        self.address = 'smtp.gmail.com'
    
    def imap_login(self, username, password):
        code=0
        try:
            server = imaplib.IMAP4_SSL(self.address)
            server.login(username, password)
            if server.status == 'AUTH':
                code = 200
            if server.status == 'NONAUTH':
                code = 400
        except:
            code = 400
        
        return code

    def email_validate(self):
        with open('src/accounts.csv', 'r') as istr:
            with open('validated_accounts.csv', 'w') as ostr:
                for line in istr:
                    creds = line.rstrip().split('\t')
                    if self.imap_login(creds[0], creds[1]) == 200:
                        line = line.rstrip('\n')+ '\tACTIVE'
                    else:   
                        line = line.rstrip('\n') + '\tINACTIVE'
                    
                    print(line, file=ostr)
                
    
    def mkacc(self, n):
        
        for ii in range(0,n):
            pref = random.randint(1,4)
            if pref == 1:
                prefstr = 'guest'
            if pref == 2:
                prefstr = 'client'
            if pref == 3:
                prefstr = 'student'
            if pref == 4:
                prefstr = 'host'
            self.acc.append(prefstr +'.0'+str(random.randint(1,9))+'.'+hashlib.sha1(str(random.randint(1,9999)).encode('utf-8')).hexdigest()[1:10] + '@gmail.com')
        
        return self.acc

    def mkpass(self,n):

        for ii in range(0,n):
            self.pss.append(hashlib.sha1(str(random.randint(1,9999)).encode('utf-8')).hexdigest()[1:15])
        
        return self.pss

    def writefile(self,n):
        acc = self.mkacc(n)
        pss = self.mkpass(n)
        if len(acc) == len(pss):
            with open('src/accounts.csv', 'a') as f:
                for ii in range(0, len(acc)):
                    f.write('\n')
                    f.write(acc[ii] + '\t' + pss[ii] + '\t' + names.get_full_name())
                    
                f.close()
                    
accounts = Gmkacc()
#accounts.writefile(9)
#accounts.email_validate()
