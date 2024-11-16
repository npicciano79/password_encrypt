import hashlib

#function create hashed password 
#takes user password and hashes 
def f_createHashedPassword (lv_password):
    print('lv_pass: '+lv_password)

        
#lv_hashed_pass = hashlib.sha256

#class hashUserPass created to contain objects used to hash and store password 
class hashedPassword:
    #NPSUPASS stores index, hash, salt, user
    def __init__(self , lv_pass , lv_hash , lv_salt ,  lv_user):
        self.sv_pass            = lv_pass
        self.sv_hash            = lv_hash
        self.sv_salt            = lv_salt
        self.sv_user            = lv_user
        
        print(f"password: {self.sv_pass} hash: {self.sv_hash} salt: {self.sv_salt} user: {self.sv_user}")
        
    
    #call function to hash password
    self.hash = f_createHashedPassword (self.sv_pass)





#initialize program
if __name__ == "__main__":
    #call call hashedPassword 
    pv_pass = hashedPassword (1234 , 'pfv' , 0000, 'Nick')  
    
    

"""
lv_hashed_pass.update('''pass to hash''')
#Procedure hashPass
def hashPass (self, 
              lv_password):
    
    def __init__ (self):
        
    
    def init self 
    
    """
    