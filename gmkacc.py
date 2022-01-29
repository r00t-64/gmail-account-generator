#!/usr/bin/python3
from __future__ import absolute_import
from __future__ import print_function
import hashlib
import random
import src.names
import smtplib
from six.moves import input
import csv

class Gmkacc:
    def __init__(self):
        self.acc = []
        self.pss = []
        self.init_smtplib()
    
    def init_smtplib(self):
        self.smtp = smtplib.SMTP("smtp.gmail.com",587)
        self.smtp.starttls()
        self.smtp.ehlo()
        
    def try_gmail(self, username, password):
        code=0
        try:
            self.smtp.login(username,password)
            code = 200
            self.smtp.quit()
            self.init_smtplib()
            
        except smtplib.SMTPAuthenticationError:
            code = 400
        
        return code

    def gmail_validate(self):
        with open('src/accounts.csv', 'r') as istr:
            with open('validated_accounts.csv', 'w') as ostr:
                for line in istr:
                    creds = line.rstrip().split('\t')
                    if self.try_gmail(creds[0], creds[1]) == 200:
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


print('''
	==================================
	|[Gmail Account Generator] ==> 3 |
	|--------------------------------|
	| "We are fsociety"              |
	| Coded By isaac (@r00t-64)      |
	|--------------------------------|
	''')

instance = Gmkacc()

do = input('''
		Choose any number ?
		1 - Validate gmail accounts
		2 - Create new gmail accounts (#)
		
		==> ''')

if do == '1':
	headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	instance.gmail_validate()
################	
if do == '2':
	headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	instance.writefile(9)

