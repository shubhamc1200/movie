from django.shortcuts import render,redirect
import pyrebase
from django.contrib import auth

config = {
    'apiKey': "AIzaSyDhZE9xMeSWveibyOk_QSqY4Il6-jg8nVw",
    'authDomain': "cpanel-6c4b9.firebaseapp.com",
    'databaseURL': "https://cpanel-6c4b9.firebaseio.com",
    'projectId': "cpanel-6c4b9",
    'storageBucket': "cpanel-6c4b9.appspot.com",
    'messagingSenderId': "970490557639",
    'appId': "1:970490557639:web:80b1969d3e10f449b23ae2",
    'measurementId': "G-FYKVR3SY8W"
  }

firebase = pyrebase.initialize_app(config)
database=firebase.database()#here database is essential cuz when user signs up all users info stroed in database

authe = firebase.auth()#for authorization of user

def signIn(request):
    return render(request,'accounts/signIn.html')


def postsign(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try: #try catch block if any user is incorret(ie not in database)
        user=authe.sign_in_with_email_and_password(email,passw)
    except:
        message="invalid credentials"
        return render(request,"accounts/signIn.html",{"messg":message})
    request.session["logged"]=True
    local_id=user['localId']#retrieving the localId cuz from it we can retrieve the name of user for comments
    users = database.child("users").get()

    all_users = database.child("users").get() #from documentation
    for user in all_users.each():
        if user.key()==local_id:
            print(user.val()['details']['name']) #here we have retrieved the name of user
            name_of_user=user.val()['details']['name']

    #for superusers
    if email=="cshubham1200@gmail.com":
        request.session['superuser']=True

    return redirect("movies:list")


def logout(request):
    auth.logout(request)
    request.session["logged"]=False
    return redirect("movies:list")



def signUp(request):
    return render(request,"accounts/signUp.html")


def postsignup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    passw1=request.POST.get('pass1')
    passw2=request.POST.get('pass2')
    if passw1!=passw2:
        message="Passwords are not matching."
        return render(request,"accounts/signUp.html",{"messg":message})
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
    except:
        message="Incorret details. Unable to create, please try again."
        return render(request,"accounts/signUp.html",{"messg":message})
    data={"name":name,"status":"1"} #for new users status is 1 which means account is enabled
    uid=user['localId'] #after capturing the uid with the help of it we are gonna store name status
    #for pushing the data into database
    #database is the parent table user is child table
    database.child("users").child(uid).child("details").set(data)
    request.session["logged"]=True
    local_id=user['localId']
    users = database.child("users").get() #this is the same comments as postsign for retriving name for comments after signing up
    all_users = database.child("users").get()
    for user in all_users.each():
        if user.key()==local_id:
            print(user.val()['details']['name'])
            name_of_user=user.val()['details']['name']

    request.session['name_user']=name_of_user

    return redirect("movies:list")
