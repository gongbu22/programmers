def solution(str_list):
    for idx, str in enumerate(str_list):
        if str == 'l' :
            return str_list[:idx]
        elif str == 'r' :
            return str_list[idx+1:]
        
    return []
        
        