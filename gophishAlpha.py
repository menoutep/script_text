fichier = open("gophish-chris.csv","a")
intro = "First Name,Last Name,Email,Position \n"
fichier.write(intro)

def clean_mail(mail):
    i = int(len(mail))
    i=i-2
    mail = mail[0:i]
    return mail

def clean_name(mail):
    i = int(len(mail))
    i=i-1
    mail = mail[0:i]
    return mail

def clean(mot):
    mot = str(mot)
    mot = mot.strip('[')
    mot = mot.strip(']')
    mot = mot.strip("'")
    return mot



def decoupe(filemail):
    with open(filemail, mode='r', encoding='utf-8') as mails_file:
        for mail in mails_file:
            xxx = mail.split('@') 
            user = xxx[0:1]
            user = clean(user)
            smtp = xxx[1:2]
            smtp = clean(smtp)
            smtp = clean_mail(smtp)
            smtp_ = list(smtp)
            size = len(smtp_)
            if smtp_[size-1] == '.':
                smtp_.pop(size-1)
                        
            smtp = "".join(smtp_)            
            email = user+"@"+smtp
            ligne ="{},{},{},{}".format(user, user, email,user)    
            if len(ligne)>0:   
                fichier.write(ligne)
                tabu = '\n'
                fichier.write(tabu)
                print(ligne)
               
decoupe('list_mail.txt')           