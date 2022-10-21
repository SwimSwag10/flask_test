
from cgitb import text
from flask_app.config.mysqlconnection import connectToMySQL
import json, ipfshttpclient, os, hashlib
from flask import session, request

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

class User:
  db = 'demo'
  patient_ipfs_data_path = 'C:/Users/Justi/personal-projects/projects/ipfs_projects/flask_test/flask_app/user_data'
  def __init__(self,data):
    self.patient_number = data['PatNum']
    self.last_name = data['LName']
    self.first_name = data['FName']

    self.data = f"{User.get_patient_by_id(id)}".encode() # this will not work because we need to input what id the user has inputted into the application
    self.password = b"PASSWORD" # password has to be what user inputes, therefore it will have to be "[]" and we will have to save this in a schema with the saved user session.
    self.salt = get_random_bytes(32)

  @classmethod
  def get_patient_by_id(cls,id):
    data = {
      'patnum' : id
    }
    query = """
    SELECT * FROM patient 
    WHERE patnum = %(patnum)s;
    """
    results = connectToMySQL(cls.db).query_db(query,data)
    if len(results) < 1:
      return False
    return results[0]

  @classmethod
  def patient_create_file(cls,id):
    patient_file_name = f"{User.get_patient_by_id(id)['PatNum']}{User.get_patient_by_id(id)['LName'].lower()}"

    # -- encryption should happen right here before the file is created with the information inside of it --

    text_file = open(f"{cls.patient_ipfs_data_path}/{patient_file_name}.txt", "w")
    if text_file == False:
      print("patient already has a file created")
      return patient_file_name
    
    text_file.write(f"{User.get_patient_by_id(id)}")
    text_file.close()

    return patient_file_name


  @classmethod
  def patient_create_encrypted_file(cls,id):
    patient_file_name = f"encrypted.{User.get_patient_by_id(id)['PatNum']}{User.get_patient_by_id(id)['LName'].lower()}"

    key = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1, dklen=32)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open(f"{cls.patient_ipfs_data_path}/{patient_file_name}.bin", "wb")
    if file_out == False:
      print("patient already has a file created")
      return patient_file_name
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    file_out.close()

    return patient_file_name

  @classmethod
  def patient_ipfs_file_upload(cls,id):
    # instead of using the ipfs file uploader package, you could requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files)

    file_in = open("encryptedfile.bin", "rb")
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

    key = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1, dklen=32)
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    print(data.decode('UTF-8')) 

    # the content inside the encrypted file will have to be decrypted before we add the information to ipfs
    res = client.add(f'{cls.patient_ipfs_data_path}/{User.enpatient_create_file(id)}.txt')
    # results from uploading the content to ipfs-http-client

    cidOfPatient = res['Hash']
    getContentFromCID = client.cat(f'{cidOfPatient}').decode('utf-8')
    cls.patient_uploaded_content = getContentFromCID
  
    return res