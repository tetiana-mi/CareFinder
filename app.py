from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@localhost:5432/postgres'

db = SQLAlchemy(app)

class Caregiver(db.Model):
    __tablename__ = 'caregivers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255)) 
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    experience = db.Column(db.Integer)
    skills = db.Column(db.String(255))

@app.route('/become-a-caregiver', methods=['GET', 'POST'])
def become_caregiver():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        experience = request.form['experience']
        skills = request.form['skills']

        caregiver = Caregiver(name=name, email=email, phone=phone, address=address,
                              experience=experience, skills=skills)
        db.session.add(caregiver)
        db.session.commit()
        return redirect('/homepage')

    return render_template('become-a-caregiver.html')

@app.route('/homepage', methods=['GET'])
def carefinder_home():
    return render_template('homepage.html')