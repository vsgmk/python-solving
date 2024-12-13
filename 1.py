if __name__ == '__main__':
    list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name,score])
    sorted_list=sorted(list,key=lambda x:x[1])
    li=sorted_list[1][1]
    second_low_score=[name for name, score in list if score==li ]
  
    second_low_score.sort()
    for name in second_low_score:
        print(name)