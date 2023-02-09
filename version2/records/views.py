from django.shortcuts import render
from http.client import HTTPResponse
from .models import results
import json
import sqlite3
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission, User
conn=sqlite3.connect('db.sqlite3',check_same_thread=False)
cursor=conn.cursor()

# from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
def fun(request,x):
    return HTTPResponse(x)
        

def upload(request):
    csrf_token = get_token(request)
    if request.method=='POST':
        # print(type(request.body))
        # print(type(request.headers))
        # print(request.headers)
        #print(request.body.decode('ASCII'))
        dat1=json.loads(request.body.decode('ASCII'))
        # print(type(dat1))
        # print(dat1)
        head=request.headers
        Username=head['Username']
        Password=head['Password']
        user1 = authenticate(username=Username, password=Password)
        if user1 is not None:
                # print(dat1)
                u = User.objects.get(username=Username)
                employee_name=u.get_full_name()
                employee_id=Username
                created_at= dat1['created_at']
                plat_form=dat1['plat_form']
                project_name=dat1['project_name']
                python=dat1["python"]
                for row in dat1['tests']:
                    # print(row)
                    test_name=row['test_name']
                    duration=row['duration']
                    test_outcome=row['test_outcome']
                    longrep=row['longrep']
                    cursor.execute('insert into records_results(project_name,test_name,duration,test_outcome,longrep,created_at,employee_id,employee_name,plat_form,python) values(?,?,?,?,?,?,?,?,?,?)',(project_name,test_name,duration,test_outcome,longrep,created_at,employee_id,employee_name,plat_form,python))
                    conn.commit()
                # res1.save(self=results2)
                print('saved to db')
     
    return render(request,'upload.html')
    # else :
    #     return render(request,'upload.html')
# @login_required(login_url='upload/up/')
def get1(request,pk1,pk2,pk3):
    if request.method=='GET':
        print('hello')
        cursor.execute('select project_name,test_name,created_at,test_outcome,duration,longrep,employee_id,employee_name,plat_form,python from records_results where id=?',(pk3,))
        res=cursor.fetchall()
        print(res)
        data={'project_name':res[0][0],'test_name':res[0][1],'created_at':res[0][2],'test_outcome':res[0][3],'duration':res[0][4],'longrep':res[0][5],'employee_id':res[0][6],'employee_name':res[0][7],'plat_form':res[0][8],'python':res[0][9]}
        #     data.append(entry)
        return render(request,'f.html',{'data':data})
def get(request,pk1,pk2):
    if request.method=='GET':
        cursor.execute('select id, test_name,project_name,created_at,test_outcome from records_results where project_name=? and created_at=?',(pk1,pk2,))
        res=cursor.fetchall()
        i=1
        data=[]
        for row in res:
            row=list(row)
            row.insert(1,i)
            i=i+1
            row[0]=str(row[0])
            entry={'actual_data':row[1:],'button':str(pk2+'/'+row[0])}
            data.append(entry)
        return render(request,'get.html',{'data':data})

  
    
# @login_required   
def get_run(request,pk):
    if request.method=='GET':
        print(pk)
        print(type(pk))
        st=str(pk)
        cursor.execute('select distinct created_at from records_results where project_name=?',(st,))
        res=cursor.fetchall()
        print(res)
        data=[]
        i=1
        for row in res:
            row=list(row)
            row[0]=str(row[0])
            print(row[0])
            cursor.execute('select id,test_outcome from records_results where project_name=? and created_at=?',(st,row[0],))
            res1=cursor.fetchall()
            total=0
            passed=0
            for x in res1:
                if x[1]=='passed':
                    passed=passed+1
                total=total+1
            
            row.insert(0,i)
            row.insert(1,st)
            row.append(str(passed)+'/'+str(total))
            print(row)
            i=i+1
            entry={'actual_data':row,'button':st+'/'+str(row[2])}
            data.append(entry)
        return render(request,'run.html',{'data':data})
        
def login(request):
    if request.method=='POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']

        user=authenticate(username=user_name,password=pass_word)
        if user is not None:
            print('successfully in')
            login(user)
            return HTTPResponse( 'logged in yayaya')



        else:
            print('successfully checked')
            return HTTPResponse('sorry magga')



    print(request.GET)
    return render(request,'login.html',{})
    
def projects(request):
     if request.method=='GET':
        cursor.execute('select distinct project_name from records_results')
        res=cursor.fetchall()
        data=[]
        i=1
        for row in res:
            row=list(row)
            row[0]=str(row[0])
            row.insert(0,i)
            print(row)
            i=i+1
            entry={'actual_data':row,'button':str(row[1])}
            data.append(entry)
        return render(request,'index.html',{'data':data})
    
