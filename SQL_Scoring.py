from FINAL_GAME import game_loop
import mysql.connector as m
if __name__ != '__main__':
    def run_game(name):
            con = m.connect(host = 'localhost', username = 'root', passwd = 'fab4', db = 'project')

            def insertion_sort(lst):
                length = len(lst)
                for i in range(1,length):
                    temp = lst[i]
                    j = i-1
                    while j >= 0 and temp[2] > lst[j][2]:
                        lst[j+1] = lst[j]
                        j = j -1
                    else :
                        lst[j+1] = temp

            score,time = game_loop()
            try:
                player = [100, name, score , time]
                if con.is_connected():
                    mycursor = con.cursor()

                    query1 = 'select * from leaderboard'
                    mycursor.execute(query1)
                    result = mycursor.fetchall()
                    lst = []
                    lst1 = [mycursor.column_names]
                    

                    if len(result) != 0:
                        for i in range(len(result)):
                            a = list(result[i])
                            lst.append(a)
                            if player[2] > a[2] and lst.count(player) == 0:
                                lst.insert(i,player)

                        if lst.count(player) == 0 and len(lst) < 5:
                            lst.append(player)
                            lst[len(lst)-1][0] = len(lst) 

                        insertion_sort(lst)

                        for i in range(len(lst)):
                            lst[i][0] = i+1
                            lst[i] = tuple(lst[i])
                        
                        if len(lst) > 5:
                            lst.pop()

                    elif len(lst) == 0:
                        lst.append(player)
                        lst[0][0] = 1
                        lst[0] = tuple(lst[0])

                    query2 = 'delete from leaderboard'
                    mycursor.execute(query2)
                    con.commit()
                    
                    query3 = 'insert into leaderboard values (%s,%s,%s,%s)'
                    mycursor.executemany(query3,lst)
                    con.commit()

            except Exception as e:
                print(e)

            else:
                lst.insert(0,lst1[0])
                con.close()

