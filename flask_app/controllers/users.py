from flask import render_template, request, redirect, flash, session
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/display/<int:id>')
def dashboard(id):
  print(f"!!!!!!!!!!!!!!!??????????? {User.patient_create_encrypted_file(id)}")

  return render_template('display.html', patient=User.get_patient_by_id(id), cid=User.patient_ipfs_file_upload(id))

@app.route('/user/login', methods=['POST'])
def create_user_withcid():
  return redirect(f"/display/{request.form['number']}")