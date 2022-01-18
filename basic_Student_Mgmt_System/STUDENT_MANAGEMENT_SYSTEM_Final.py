#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
#Student Registration Management System 
Fields :- [‘roll’, ’name’ ,’age’,’ email’, ’phone no.’]
1. Add New Student
2 View Students 
3. Search Student
4. Update Student
5. Delete Student
'''
import pandas as pd
import csv

file_path = 'D:/Self-Study/PYTHON/'

#Define global variables
student_fields = ['Roll No','Name', 'Age', 'E-mail', 'Phone No']
student_database = 'students.csv'


# In[4]:


def display_menu ():
    print('\n\t\t---------------------------------------------------')
    print('\n\t\t Welcome to Student Registration Management System')
    print('\n\t\t---------------------------------------------------')
    print('1. Add New Student')
    print('2. View Students')
    print('3. Search Student')
    print('4. Update Student')
    print('5. Delete Student')
    print('6. Quit')


# In[5]:


def add_student():
    global student_fields
    global student_database
    while True:
        print('\n\t\t--------------------------------')
        print('\n\t\t Add Student Information')
        print('\n\t\t--------------------------------')
    
        student_data =[]
        for field in student_fields:
            value = input('Enter '+ field+' :')
            student_data.append(value)
        with open(student_database,'a', encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(student_data)

        print('Data saved successfully')
        more = input('Do you want to Add another student information! [Yes/No]')
        if ((more=='Yes')or (more=='yes') or (more=='Y') or (more=='y')):
            continue
        else:
            break
    input('Press any key to continue')
    return


# In[6]:


def view_students():
    global file_path
    global student_fields
    global student_database
    
    print('\n\t\t---------------------------')
    print('\n\t\t View Student Record')
    print('\n\t\t---------------------------')
    
    ###Alternative
    df_view = pd.read_csv(file_path + student_database)
    print(df_view)
    
    input('Press any key to continue')


# In[7]:


def search_student():
    global file_path
    global student_fields
    global student_database
    
    print('\n\t\t---------------------------')
    print('\n\t\t Search Student Record')
    print('\n\t\t---------------------------')

    df_student = pd.read_csv(file_path + student_database)
    
    while True:
        
        roll = int(input('Enter roll no. to search :\t '))
        df_search = df_student[df_student['Roll No'] == roll]
        if df_search.shape[0]>0:
            print('\n\t----------- Student Information Found -----------\n')
            print(df_search)
        else:
            print('\n\t!!!!! Student information for the entered Roll No is not found !!!!!')
            
        more = input('Do you want to Search more student information! [Yes/No]')
        if ((more=='Yes')or (more=='yes') or (more=='Y') or (more=='y')):
            continue
        else:
            break
    
    input ('Press any key to continue')


# In[9]:


def update_student():
    global file_path
    global student_fields
    global student_database
    updated_student_fields = ['Updated Roll No','Name', 'Age', 'E-mail', 'Phone No']

    print('\n\t\t---------------------------')
    print('\n\t\t Update Student Record')
    print('\n\t\t---------------------------')
    
    while True:
        
        roll = int(input('Enter roll no. to update :\t'))
        df = pd.read_csv(file_path + student_database)
        df_student = df.copy()
        if (df_student[df_student['Roll No'] == roll].shape[0]) > 0:
            print("\n\t----- Student's Current Information -------\n")
            print(df_student[df_student['Roll No'] == roll])
            for field in updated_student_fields :
                value = input('Enter' + field  + ' :')
                df_student.loc[df_student['Roll No'] == roll,field] = value
            df_student.loc[df_student['Roll No'] == roll,'Roll No'] = df_student.loc[df_student['Roll No'] == roll,'Updated Roll No']
            print('\n!!!!! Student information updated suessfully !!!!!')
            #print(df_student)
            df_student.drop('Updated Roll No',axis=1,inplace=True)
            df_student.to_csv(file_path + student_database,index=False)

        else:
            print('\n\t!!!!! Student information for the entered Roll No is not found !!!!!')

        more = input('Do you want to Update more student information! [Yes/No]')
        if ((more=='Yes')or (more=='yes') or (more=='Y') or (more=='y')):
            continue
        else:
            break
         
    input ('Press any key to continue')
       


# In[14]:


def delete_student():
    global student_fields
    global student_databse
    
    print('\n\t\t---------------------------')
    print('\n\t\t Delete Student Record')
    print('\n\t\t---------------------------')
    
    while True:
        
        roll = int(input('Enter roll no. to delete :\t'))
        df = pd.read_csv(file_path + student_database)
        df_student = df.copy()
        if (df_student[df_student['Roll No'] == roll].shape[0]) > 0:
            print("\n\t----- Student's Existing Information -------\n")
            print(df_student[df_student['Roll No'] == roll])
            
            indexNames = df_student[df_student['Roll No'] == roll ].index
            # Delete these row indexes from dataFrame
            df_student.drop(indexNames , inplace=True)
            df_student.to_csv(file_path + student_database,index=False)
            print(f'\n!!!!! Student information for roll no {roll} Deleted suessfully !!!!!')
            
        else:
            print('\n\t!!!!! Student information for the entered Roll No is not found !!!!!')

        more = input('Do you want to Delete more student information! [Yes/No]')
        if ((more=='Yes')or (more=='yes') or (more=='Y') or (more=='y')):
            continue
        else:
            break
         
    input ('Press any key to continue')
 


# In[13]:


while True:
    display_menu()
    choice = int(input ('Enter your choice:\t'))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    else:
        break
print('\t\t-----------------------------------')
print('\t\t  Thank you for using our system') 
print('\t\t-----------------------------------')         


# In[ ]:




