immutable_var = 1, 3 ,"BMW",'AUDI'
print(immutable_var)
#в кортеже не изменяются значения элементов ,т.к только в списке можно производить изменения . В выводе он мне напишет ошибку
immutable_list=['bmw','audi','mers']
(immutable_list[0])
immutable_list[0]='kia'
print(immutable_list)
(immutable_list[1])
(immutable_list[1])='lada'
print(immutable_list)
(immutable_list[2])
immutable_list[2]='chery'
print(immutable_list)
