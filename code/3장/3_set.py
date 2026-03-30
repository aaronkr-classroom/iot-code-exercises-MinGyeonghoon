# 3_set.py
#두 집합 정의
set1 = {1,2,3,'a',"Hello"}
set2 = {"Hello",3,4,5,'b'}

#합집합 (union)
union_set = set1 | set2 #c에서 || = or, py에서 or

#교집합(intersection)
int_set = set1 & set2

#차집합(difference)
diff_set = set1 - set2

#대칭 차집합(symmetric_difference)
sym_diff_set = set1 ^ set2 # 합집합와 교집합의 차집합

print('union:' , union_set)
print(f"intersection: {int_set}")
print(f"difference: {diff_set}")
print(f"symmetric difference: {sym_diff_set}")