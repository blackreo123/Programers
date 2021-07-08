import operator
def solution(genres, plays):
    answer = []
    각각플레이수 = []
    장르별총플레이수 = {}
    전체순서 = []
    # 장르별 순위를 정한다
    for 번째 in range(0,len(genres)):
        각각플레이수.append({번째 : {genres[번째] : plays[번째]}})
        if genres[번째] in 장르별총플레이수.keys():
            장르별총플레이수[genres[번째]] = 장르별총플레이수[genres[번째]] + plays[번째]
        else:
            장르별총플레이수[genres[번째]] = plays[번째]
    플레이수_많은순_장르별총플레이수 = sorted(장르별총플레이수.items(), key=operator.itemgetter(1), reverse=1)
    플레이수_많은순_장르 = []
    for i in 플레이수_많은순_장르별총플레이수:
        플레이수_많은순_장르.append(i[0])
    for i in range(len(각각플레이수)):
        for j in range(len(각각플레이수) - 1 ,i, -1):
            if list(list(각각플레이수[j].items())[0][1].values())[0] > list(list(각각플레이수[j-1].items())[0][1].values())[0]:
                각각플레이수[j],각각플레이수[j-1] = 각각플레이수[j-1], 각각플레이수[j] 
    
    for 장르 in 플레이수_많은순_장르별총플레이수:
        for i in range(0,len(각각플레이수)):
            
        # 장르가 같은거 뽑기
            if 장르[0] in list(각각플레이수[i].values())[0].keys():
                전체순서.append(각각플레이수[i])
    print(플레이수_많은순_장르)
    print(전체순서[0])
    # 나열한다
    # for i in 플레이수_많은순_장르:
    #     for j in 전체순서:
    #         if 
        # answer.append(list(i.keys())[0])
    # print(answer)
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
solution(genres, plays)