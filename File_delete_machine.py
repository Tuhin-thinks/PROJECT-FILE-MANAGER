import os
import time
def File_delete():
    List=os.listdir()
    for j in List:
        print(j)
    print(16*'*',16*'-',16*'*')
    print('Enter the type of file you want to delete:',end='')
    typ=input()
    print('Enter the Mode of Deletion')
    print('1.single delete\n2.Multiple delete with exceptions\n3.delete all')
    response0=input()
    exceptions=[]
    if response0=='2':
        for i in range(len(List)):
            print('{}.{}'.format(i+1,List[i]))
        print('Enter the options numbers(seperated by spaces) to mark them as exception.')
        exceptions=input().split()
                  
    response=''
    for i in List:
        if i[-len(typ):]==typ and i[:-len(typ)]!='File_delete_machine' and i not in exceptions:
            print(i)
            if response0=='3' or response0=='2':
                response='x'
            if response0=='1':
                print('press "x" to delete and "k" to keep')
                response=input()
            if response=='x':
                try:
                    os.remove(i)
                    print('Deleted {} from {}'.format(i,os.path.basename(os.getcwd())))
                except:
                    print('Deleting Unsuccessful!')
            else:
                pass
    print('\n\nDo you want to delete more Files ? (yes or no)')
    response1=input()
    if response1=='yes':
        File_delete()
    else:
        print('you have chose to exit..\n Exiting...')
        time.sleep(0.3)
        exit(0)
File_delete()
        
