
# for i in range(0,11):
#     print('top')
#     for j in range(0,5):
#         print(j , end = ' ')
        
# # para repetir uma vez só é só fazer com um for, sem estar aninhado.


# ----------------------------------------------------------------------


# for i in range(0,3):
#     print('top')
#     for j in range(0,2):
#         print(f"{i}{j}", end = ' ')
        
# # Terminal:
# # Top
# # 00_01

# # Top
# # 10_11

# # Top
# # 20_21


# ----------------------------------------------------------------------


# for i in range(0,3):
#     print('top')
#     for j in range(i,5):
#         print(j , end = ' ')
    
    
# Top
# 0 1 2 3 4

# 2 3 4 (mudando o range para 2,5 e criando uma variavel com valor 2)

# i começa valendo 0; 
# Top
# 0 1 2 3 4

# Top
# 1 2 3 4

# Top
# 2 3 4

# ---------------------------------------------------------------------

for i in range(0,3):
    print("1", end =' ')
    for j in range(0,4):
        print("2", end =' ')
        for k in range(0,2):
            print("3", end =' ')