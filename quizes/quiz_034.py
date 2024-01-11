def mystery (list1:list, list2:list) -> list:
    output=[]
    for k,v in zip(list1,list2):
        if list1[k] == list2[v]:
            output.append(list1[k])
    return output