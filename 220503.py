#(25083) 새싹 그리기 
# print(r'''         ,r'"7
# r`-_   ,'  ,/
#  \. ". L_r'
#    `~\/
#       |
#       |''')

# --------------------------------------------------

#(10926) 입력 문자열 뒤에 ??! 붙여 출력하기 
# a= input()
# print(a+'??!')

# --------------------------------------------------

#(18108) 불기를 서기로 변환해서 출력하기 
# be=int(input())
# print(be-543)

# --------------------------------------------------

#(2525) 현재시각과 소요시간을 더해 완료시각 출력하기 
# import sys
# a,b = map(int, sys.stdin.readline().split())
# c = int(input())

# end = (a*60)+b+c
# h = end//60
# m = end%60
# if (h>=24):
#     print(h-24, m)
# else:
#     print(h, m)

# --------------------------------------------------

#(2480) 주사위 세개를 던져 나온 눈에 대해 상금 처리하기
dice = list(map(int, input().split()))

if(dice[0]==dice[1]):
    if(dice[0]==dice[2]):
        print(10000+dice[0]*1000)
    else:
        print(1000+dice[0]*100)
elif(dice[0]==dice[2]):
    print(1000+dice[0]*100)
elif(dice[1]==dice[2]):
    print(1000+dice[1]*100)
else:
    print(max(dice)*100)
