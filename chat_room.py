recode = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
id_set = set([])
user = {}
comment_list = []
for i in recode:
    id = i.split(' ')[1]
    id_set.add(id)
id_list = list(id_set)
for i in id_list:
    user.setdefault(i,{})
for i in recode:
    if len(i.split(' ')) == 3:
        id = i.split(' ')[1]
        name = i.split(' ')[2]
        user[id]['name'] = name

for i in recode:
    id = i.split(' ')[1]
    behavior = i.split(' ')[0]
    if behavior == 'Enter':
        comment = user[id]['name']+'님이 들어왔습니다'
        comment_list.append(comment)
    elif behavior == 'Leave':
        comment = user[id]['name']+'님이 나갔습니다'
        comment_list.append(comment)
print(comment_list)