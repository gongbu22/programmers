def solution(my_string, indices):
    indices.sort(reverse=True)
    new = list(my_string)
    for i in indices:
        new.pop(i)
    return ''.join(new)