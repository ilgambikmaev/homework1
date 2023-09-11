f = open ("train.csv","r")
Spisok = list(f.readlines())
f.close()

All_count = 0
Male_count = 0
Female_count = 0

S = []
for i in range(1, len(Spisok)):
    S = Spisok[i].split(',')
    if S[1] == "1" and S[5] == 'male':
        Male_count += 1
    if S[1] == '1' and S[5] == 'female':
         Female_count += 1
All_count = Male_count + Female_count

print("Общее кол-во выживших:", All_count)
print("Кол-во выживжих мужчин:", Male_count)
print("Кол-во выживших женщин:", Female_count)


