#! /usr/bin/python
# -*- encoding: utf-8 -*-

def printList(a):
    if(len(a)==0):
        print '\nCurrent list is empty '
    else:
        print 'Current list:\n\nindex \telement'
        for i in range(0, len(a)):
            print str(i) + '\t' + a[i]


def createJavalist(a, name):
    x = 'String[] ' + str(name) + ' = {'
    for i in range(0,len(a)):
        if(i == (len(a)-1)):
            x += '"' + a[i] + '"'
        else:
            x += '"' + a[i] + '"' + ', '
    x += '};'
    print x


def createPythonlist(a, name):
    x = str(name) + ' = ['
    for i in range(0,len(a)):
        if(i == (len(a)-1)):
            x += '"' + a[i] + '"'
        else:
            x += '"' + a[i] + '"' + ', '
    x += ']'
    print x


run = True
print('Welcome to list creator!')
list = []
while(run):
    try:
        printList(list)
        select = raw_input('''\n
a - add an element to the end of the list
i - inserts and element to the index given in next input
dn - deletes the first element by given name
di - deletes the element from the index given in next input
q - exit list creator

selection: ''')

        if(select == 'a'):
            add_element = raw_input('name of the element: ')
            list.append(add_element)

        elif(select == 'i'):
            insert_element = raw_input('name of the element: ')
            try:
                insert_index = input('which index to insert element to: ')
            except:
                print 'Index must be a number, press ENTER to continue'
            list.insert(insert_index, insert_element)

        elif(select == 'dn'):
            delete_element = raw_input('which element to delete: ')
            try:
                list.remove(delete_element)
            except:
                raw_input('no such element, press ENTER to continue')

        elif(select == 'di'):
            try:
                delete_index = input('element on which index to delete: ')
            except:
                raw_input('Index must be a number, press ENTER to continue')
            try:
                list.pop(delete_index)
            except:
                raw_input('no elements on given index, press ENTER to continue')

        elif(select == 'q'):
            list_name = raw_input('Name your list: ')
            save_selection = raw_input('''Export list
j - Java list
p - Python list
             ''')
            if(save_selection == 'j'):
                createJavalist(list, list_name)
                raw_input('press ENTER to exit')
                run = False
            elif(save_selection == 'p'):
                createPythonlist(list, list_name)
                raw_input('press ENTER to exit')
                run = False
            else:
                raw_input('Invalid selection! Press ENTER to continue')
        else:
            raw_input('Invalid selection!  Press ENTER to continue')
    except:
        'Something went wrong!\nexiting program.'
