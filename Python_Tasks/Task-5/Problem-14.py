# 14.Finding the Percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks.keys():
        c=student_marks.get(query_name)
        avg=sum(c)/len(c)
        print(f"{avg:.2f}")
