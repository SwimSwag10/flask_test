
from cgitb import text
from flask_app.config.mysqlconnection import connectToMySQL
import json, ipfshttpclient, os
from flask import session, request

client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

class User:
  db = 'demo'
  patient_ipfs_data_path = 'C:/Users/Justi/personal-projects/projects/ipfs_projects/flask_test/flask_app/user_data'
  def __init__(self,data):
    self.patient_number = data['PatNum']
    self.last_name = data['LName']
    self.first_name = data['FName']
    self.patient_uploaded_content = []

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
    patient_file_name = f"{User.get_patient_by_id(id)['PatNum']}{User.get_patient_by_id(id)['LName']}"

    text_file = open(f"{cls.patient_ipfs_data_path}/{patient_file_name}.txt", "w")
    if text_file == False:
      print("patient already has a file created")
      return patient_file_name
    
    text_file.write(f"{User.get_patient_by_id(id)}")
    text_file.close()

    return patient_file_name

  @classmethod
  def patient_ipfs_file_upload(cls,id):
    res = client.add(f'{cls.patient_ipfs_data_path}/{User.patient_create_file(id)}.txt')
    # results from uploading the content to ipfs-http-client
    print(f"############################### {res}")
    cidOfPatient = res['Hash']
    getContentFromCID = client.cat(f'{cidOfPatient}').decode('utf-8')
    cls.patient_uploaded_content = getContentFromCID
    # retrieving our uploaded patient data from ipfs
    print(getContentFromCID['PatNum'])
    return res