name_list=["reza","Amir","fatame","Taha","ali","samiar","Saman","ahmad","sara","abas"]

def filter_name(name):
    filter_list =[]
    for i in name :
        if i[0].islower():
            filter_list.append(i)
    return filter_list

print(filter_name(name_list))