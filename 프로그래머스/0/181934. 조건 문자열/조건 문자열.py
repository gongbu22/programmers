def solution(ineq, eq, n, m):
    answer = 0
    if (ineq == '>'):
        answer = int(n >= m) if eq == '=' else int(n > m)
    else:
        answer = int(n <= m) if eq == '=' else int(n < m)

    return answer