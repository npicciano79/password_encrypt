import hashlib
import bcrypt 
from passlib.hash import pbkdf2_sha256
    

#create password salt
#def f_create_Password_Salt ():
    
    
    
    
    
        
#lv_hashed_pass = hashlib.sha256

#class hashUserPass created to contain objects used to hash and store password 
class hashedPassword:
    #NPSUPASS stores index, hash, salt, user
    def __init__(self , lv_hash , lv_salt ,  lv_user):
        self.sv_hash            = lv_hash
        self.sv_salt            = lv_salt
        self.sv_user            = lv_user




#takes user password and generates hash
#adds salt into hashed password
def f_create_Password_Hash (lv_password):
    #print('lv_pass: '+lv_password)
    return pbkdf2_sha256.hash(lv_password)
    
   
   




#initialize program
if __name__ == "__main__":
    
    #retrieve user password as lv_password    
    lv_password = input('Enter your password: ')
    
    #passes lv_password to has function and returns
    #sv hash as hash and salt
    sv_hashedPass_Salt = f_create_Password_Hash (lv_password)

    lv_salt,lv_hash = sv_hashedPass_Salt.split("-")[0], sv_hashedPass_Salt.split("-")[1]
    
    print ('hash: '+lv_hash+" salt: "+lv_salt)
    
    #call call hashedPassword 
    #pv_pass = hashedPassword (1234 , 'pfv' , 0000, 'Nick')  
    
    

"""
lv_hashed_pass.update('''pass to hash''')
#Procedure hashPass
def hashPass (self, 
              lv_password):
    
    def __init__ (self):
        
    
    def init self 
    
    """
    