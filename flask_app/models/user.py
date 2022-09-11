
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

  # this method should return the name of the file.
  @classmethod
  def patient_create_file(cls):
    print(f"??????????????????????? {cls.patient_ipfs_data_path}")
    filepath = os.path.join(f'{cls.patient_ipfs_data_path}', f'filename.txt')
    # if not os.path.exists(f'{cls.patient_ipfs_data_path}'):
    #   os.makedirs(f'{cls.patient_ipfs_data_path}')
    f = open(filepath, "a")
    return f

  @classmethod
  def patient_ipfs_file_upload(cls):
    res = client.add(f'{cls.patient_ipfs_data_path}/{User.patient_create_file()}')
    print(res)
    cidOfPatient = res.address

    # this gets the values inside of the file uploaded to ipfs
    # QmZJsQUWUes6vz6DzDT3z6383k1Y4hFYUKun9UkPN1PYSX
    getContentFromCID = client.cat(f'{cidOfPatient}').decode('utf-8')
    print(getContentFromCID)
    return res