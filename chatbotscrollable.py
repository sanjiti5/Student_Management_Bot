import cx_Oracle

try:
    con = cx_Oracle.connect('system/priti@localhost:1521/xe')
    print('\nConnected...\nSay hi to proceed')
    qna = {
         "hi":"hey",
         "HI":"hey",
         "Hi":"hey",
         "hI":"hey"
    }
    print('\nUser: ')
    qs=input()
    print('\nBot: ',qna[qs])
    

except cx_Oracle.DatabaseError as er:
    print('There is an error in the Oracle database:', er)
    
else:
    try:
        
        print('\nBot: Welcome to chatbot')
        cur = con.cursor(scrollable=True)
        
        i=1
        while i>0:
            print('\nPlease enter Student ID only')
            print('\nUser: ')
            ur=input()
            if(ur=='~'):
                break
            ur=int(ur)
            if(ur=='~'):
                break
            j=1
            while j>0:
                print('\nBot: ','Select required option\n1. Student Name     2. Mother Name\n3. Student Email    4. Student Contact No.\n5. City             6. Quit')
                print('\nUser: ')
                o=int(input())
         
                if(o==1):
                    cur.execute('select sname from studpersonal order  by studid')
                    cur.scroll(ur,mode="absolute") 
                    print('\nBot: Student Name-',cur.fetchone())
                elif(o==2):
                    cur.execute('select mname from studpersonal order  by studid')
                    cur.scroll(ur,mode="absolute") 
                    print('\nBot: Mother Name-',cur.fetchone())
                elif(o==3):
                    cur.execute('select semail from studpersonal order  by studid')
                    cur.scroll(ur,mode="absolute") 
                    print('\nBot: Student Email-',cur.fetchone())
                elif(o==4):
                    cur.execute('select scontact from studpersonal order  by studid')
                    cur.scroll(ur,mode="absolute") 
                    print('\nBot: Student Contact No.-',cur.fetchone())
                elif(o==5):
                    cur.execute('select city from studpersonal order  by studid')
                    cur.scroll(ur,mode="absolute") 
                    print('\nBot: City-',cur.fetchone())
                else:
                    break
                
                #j+=1    
                #print('Bot: Do you want to continue with same Student ID? Y / N')
                #print('User: ')
                #a=input()
                #if(a=='Y' or a=='y'):
                #    continue
                #else:
                #    break
                

            print('\nBot: Type ~ to Exit')
            i+=1
            


    except cx_Oracle.DatabaseError as er:
        print('This Student Id does not exist')
 
    except Exception as er:
        print('Error:'+str(er))
 
    finally:
        if cur:
            cur.close()
 
finally:
    if con:
        con.close()
print('\nBot: Thank You for visiting\nDisconnected...')