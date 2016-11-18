```python
'''
按成绩排序，取前三
'''

lst = [ {'student_name': 'zhangsan', 'student_score': 65}, {'student_name': 'lisi', 'student_score': 95}, {'student_name': 'wangwu', 'student_score': 80},
        {'student_name': 'maliu', 'student_score': 75}, {'student_name': 'zhuqi', 'student_score': 88} ]

# 方法一
from operator import itemgetter
top3 = sorted(lst, key=itemgetter('student_score'), reverse=True)[:3]
print(top3)

# 方法二
print(sorted(lst, key=lambda student: student['student_score'], reverse=True)[0:3])

# 方法三
import heapq
score_first = heapq.nlargest(3, lst, key=lambda student: student["student_score"])
print(score_first)
```
