
'''
List_remove_append:
Description: Remove SPSS from input_list=['SAS', 'R', 'PYTHON', 'SPSS'] and add 'SPARK'
in its place.  
'''

def remove_element_from_list(input_list,get_val):
     #To remove elements from list
    
    if get_val.islower():
        get_val =get_val.upper()

    input_list.remove(get_val)
    print('Item ' + get_val+ ' removed,please see the following list.')
    print('This is list after element '+get_val+ ' deleted.',input_list)


def add_element_to_list(input_list,get_val):
    #To add elements from list

    if get_val.islower():
        get_val =get_val.upper()

    input_list.append(get_val)
    print('Item ' + get_val+ ' ,please see the following list.')
    print('This is list after element '+get_val+ ' added.',input_list)
 
       
def replace_element_to_list(input_list,get_old_val,get_new_val):
    # Remove present element and replace with new element
    
    if get_old_val.islower():
        get_old_val =get_old_val.upper()

    if get_new_val.islower():
        get_new_val =get_new_val.upper()
     
    for i,value in enumerate(input_list):        
           
            if value == get_old_val:
               input_list[i] = get_new_val
           
            print('Item ' + get_old_val+ ' is replaced with ' + get_new_val+'.please see the following list.')
            print('This is list after element '+get_old_val+ ' replaced.',input_list)

def main():

    input_list=['SAS', 'R', 'PYTHON', 'SPSS']
    
    while True:
        
        print('This is the list:',input_list)

        del_element = input('\nPlease enter the element you want to delete from the list.\n')       
        
        remove_element_from_list(input_list,del_element)

        add_element = input('\nPlease enter the element you want to add to the list.\n')
        add_element_to_list(input_list,add_element)
      
        old_element = input('\nPlease enter the present element of the list which you want to replace.\n')
        new_element = input('\nPlease enter the new replacement element.\n')
        
        replace_element_to_list(input_list,old_element,new_element)    

        restart = input('\nWould you like to continue? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
