import database 

from flask import Flask, render_template, request, redirect, flash, session


app= Flask(__name__)
app.secret_key="весёлые тюленчики захватят этот мир потому что они милые"

@app.get("/")
def get_root():
    username=session.get("username","Гуманитарий")
    return render_template("index.html" , user ={'name':username})

@app.get("/reg")
def get_reg():
    return render_template("reg.html")

@app.post("/reg")
def post_reg():
    username= request.form.get("username").strip()
    phonenumber =  request.form.get("phonenumber")
    password = request.form.get("password")

    if database.create_user(username,phonenumber,password):
        return redirect("/")
    flash("такой пользователь уже есть, сорри",'error')   
    return render_template("reg.html")

@app.get("/login")
def get_login():
     return render_template("login.html")

@app.post("/login")
def post_login():
    username= request.form.get("username").strip()
    password = request.form.get("password")

    user = database.get_user_by_name(username)
    if not user or password!=user[3]:
        flash("не не ти чёт попутал",'error') 
        return render_template("login.html")
    session["username"]= username
    return redirect("/")

@app.get("/logout")
def get_logout():
    session.clear()
    return redirect("/login")

@app.get("/messages")
def get_mess():
    chat_id=request.args.get("chat_id")
    messages=[]
    if chat_id:
        messages=database.get_messages(chat_id)
    username=session.get("username")
    if not username:
        return redirect("/login")
    user= database.get_user_by_name(username)
    chats=database.get_chats(user[0])
    return render_template("messages.html", chats=chats, messages=messages)
# эту ветку захватили весёлые тюленчики 
app.run()
