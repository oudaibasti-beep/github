from numpy import array
#e=dict(nom=str,qt=int)
e={}
e=dict()
t=array([e]*20)
def saisie():
    n=int(input("n="))
    while not(3<=n<=20):
         n=int(input("n="))
        return n
def remplir(t,n):
    for i in range(n):
        e=dict()
        e['nom']=input("nom")
        while not(alpha(e["nom"]):
                  e['nom']=input("nom")
            e['qt']=int(input("quatité"))
        while not  e['qt']>=0:
                   e['qt']=int(input("quatité"))
                e['prix']=float(input("prix"))
        while not e['prix']>=0
                  e['prix']=float(input("prix"))
                e['etat']=int(input("etat"))
        while not e['etat'] in [1,0]:
                 e['etat']=int(input("etat"))
            t[i]=e
def Affiche(t,n):
      s=0
    for i in range (n):
        if t[t]['etat']==0
            s=s+t[i]['qt']*t[i]['prix']
            print ("total à payé ,"s,"Dt")
def alpha(ch):
    test=len(ch)>0
    i=0
    ch=ch.upper()
    while not test and i<len(ch):
        test="A"<=ch[i]<="z"
            i=i+1
        return test
n=saisie()
remplir(t,n)
Affiche(t,n)
                  
                  
                  
        
        
