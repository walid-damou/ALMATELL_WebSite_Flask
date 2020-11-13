
#-----------------------------------CALL_LIBRARY-----------------------------------#

from flask import Flask,flash, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

#-----------------------------------/CALL_LIBRARY-----------------------------------#

#-----------------------------------FLASK-------------------------------------------#

app=Flask(__name__)
app.secret_key=b'_5#y2L"F4Q8z\n\xec]/'

#-----------------------------/FLASK------------------------------------------------#

#------------------------------------CREATE_DATA_BASE-------------------------------#

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///DMessages.db'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(20),nullable=False)
    email=db.Column(db.String(40),nullable=False)
    num=db.Column(db.String(30),nullable=False)

class Message(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    sujet=db.Column(db.String(30),nullable=False)
    mdate=db.Column(db.String(30),nullable=False)
    message=db.Column(db.Text,nullable=False)

class Admin(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    login=db.Column(db.String(30),nullable=False)
    password=db.Column(db.String(30),nullable=False)

#----------------------------------/CREATE_DATA_BASE---------------------------------#

#----------------------------HOME--------------------------------#

@app.route("/")
def home():
    return render_template("index.html")

#----------------------------/HOME--------------------------------#

#----------------------------QUI_SOMMES_NOUS--------------------------------#

@app.route("/about")
def about():
    return  render_template("about.html")

#---------------------------/QUI_SOMMES_NOUS---------------------------------#

#----------------------------NOS_TARIFS--------------------------------#

@app.route("/nos_tarifs")
def tarif():
    return  render_template("nos_tarifs.html")

#---------------------------/NOS_TARIFS---------------------------------#

#----------------------------CONTACT--------------------------------#

@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method=="POST":
        n= request.form.get("nom")
        e=request.form.get("email")
        nr=request.form.get("num")
        s=request.form.get("sujet")
        m=request.form.get("message")
        x=datetime.datetime.now()
        x=str(str(x).split(".")[0])[0:-3]
        
        us=User(nom=n,email=e,num=nr)
        db.session.add(us)
        db.session.commit()
        
        msg=Message(sujet=s,message=m,mdate=x)
        db.session.add(msg)
        db.session.commit()

    return  render_template("contact.html")

#---------------------------/CONTACT---------------------------------#

#--------------------------ADMIN----------------------------------#

@app.route("/admin")
def admin():
    return  render_template("admin.html")

#--------------------------/ADMIN----------------------------------#

#--------------------------LOGIN----------------------------------#

@app.route("/veref",methods=['GET','POST'])
def ver():
    if request.method=="POST":
        u=request.form.get("user")
        p=request.form.get("password")

        w=Admin.query.first()
        
        if (u==w.login and p==w.password):
            return redirect('/msg')
        else:
            flash("Mot de passe OU le nom d'utilisateur incorrect")
            return render_template("admin.html")

#--------------------------/LOGIN----------------------------------#

#---------------------------SHOW_MSG---------------------------------#

@app.route("/msg")
def verefication():
    messages=Message.query.all()
    user=User.query.all()
    M=[]
    S=[]
    for i in messages:
        M.insert(0,i)
    
    for e in user:
        S.insert(0,e)

    return  render_template("affiche.html",messages=M,user=S)

#---------------------------/SHOW_MSG---------------------------------#

#---------------------------DELETE_MSG---------------------------------#

@app.route("/delete/<id>",methods=['GET','POST'])
def delete(id):
    m=Message.query.get(int(id))
    u=User.query.get(int(id))
    db.session.delete(m)
    db.session.delete(u)
    db.session.commit()
    return redirect("/msg")

#---------------------------/DELETE_MSG---------------------------------#

#------------------------DEBUG------------------------------------#

if __name__=="__main__":
    app.run(debug=True)

#------------------------/DEBUG------------------------------------#