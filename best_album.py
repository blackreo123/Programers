

def solution(genres, plays):
    answer = []

    # 곡 별 재생 수 리스트
    list_a = []
    for i in range(0,len(genres)):
       list_a.append({"num" : i, "genre" : genres[i], "play" : plays[i]}) 
    list_a = sorted(list_a, key = lambda item: (-item["play"], item["num"]))
    
    # 장르 종류만 거르기
    genre = {}
    for i in genres:
        genre[i] = 0
    
    # 장르별 총 플레이 수
    for i in genre:
        for j in list_a:
            if i == j["genre"]:
               genre[i] =  genre[i]+j["play"]
     
    # 장르별 순위
    sorted_genre = sorted(genre.items(), key = lambda item: -item[1])
    # print(sorted_genre)
    
    # 장르별 곡 묶기 {장르 :[고유번호]}
    temp = {}
    for i in sorted_genre:
        temp_list = []
        for j in list_a:
            if i[0] == j["genre"]:
                temp_list.append(j["num"])
                if len(temp_list) == 2:
                    break
        temp[i[0]] = temp_list

    # 마지막 배열에 담기
    for i in list(temp.values()):
        for j in range(len(i)):
            answer.append(i[j])
    
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
solution(genres, plays)