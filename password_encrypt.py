import hashlib
import bcrypt 
#import password_encrypt.db.pass_encrypt_db
from passlib.hash import pbkdf2_sha256

#takes user password and generates hash
#adds salt into hashed password
def f_create_Hash (lv_username_password):
    #print('lv_pass: '+lv_password)
    #lv_temp_pass_user_arr = []
        return pbkdf2_sha256.hash(lv_username_password)
  
  
  
#use imported package to insert user pass into DB
def f_database_Insert (pv_username,
                       pv_pass_hash, 
                       pv_pass_salt):
    print(obj_user_pass)
  
  
   
   
#initialize program
if __name__ == "__main__":
    
    #retrieve username and password from user and stored in array 
    la_pass_user_arr = [] 
    lv_username = input('Enter your username: ')
    #la_pass_user_arr.append(lv_username)
    lv_password = input('Enter your password: ')
    #la_pass_user_arr.append(lv_password)
    #user entered password and user name
    #print('username password array: '+la_pass_user_arr)
    
    #passes lv_password into hash function to return hash and salt pass
    lv_password = f_create_Hash (lv_password)
    
    lv_pass_hash,lv_pass_salt = lv_password.split("-")[1],lv_password.split("-")[0]
    
    print('salt: '+lv_pass_salt+' hash: '+lv_pass_hash)
 
    #creates user object calling encryptedUser class
    #obj_user_pass = encryptedUser (lv_username , lv_pass_hash , lv_pass_salt)
    
    
    #pass obj_user_pass to pass_encrypt_db to insert into database
    f_database_Insert (lv_username, 
                       lv_pass_hash, 
                       lv_pass_salt)
    