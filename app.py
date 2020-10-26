from flask import Flask,flash, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import datetime


app=Flask(__name__)
app.secret_key=b'_5#y2L"F4Q8z\n\xec]/'

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


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return  render_template("about.html")

@app.route("/nos_tarifs")
def tarif():
    
    return  render_template("nos_tarifs.html")

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

@app.route("/delete/<id>",methods=['GET','POST'])
def delete(id):
    m=Message.query.get(int(id))
    u=User.query.get(int(id))
    db.session.delete(m)
    db.session.delete(u)
    db.session.commit()
    return redirect("/msg")


@app.route("/admin")
def admin():
    return  render_template("admin.html")

@app.route("/veref",methods=['GET','POST'])
def ver():
    if request.method=="POST":
        u=request.form.get("user")
        p=request.form.get("password")

        w=Admin.query.first()
        
        if (u==w.login and p==w.password):
            return redirect('/msg')
        else:
            flash("The password OR username that you've entered is incorrect.")
            return render_template("admin.html")

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


if __name__=="__main__":
    app.run(debug=True)
