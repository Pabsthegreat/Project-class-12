from FINAL_GAME import game_loop
import mysql.connector as m
if __name__ != '__main__':
    def run_game(name):
            con = m.connect(host = 'localhost', username = 'root', passwd = 'fab4', db = 'project')

            def insertion_sort_scores(lst):
                length = len(lst)
                for i in range(1, length):
                    temp = lst[i]
                    j = i-1
                    while j >= 0 and temp[2] > lst[j][2]:

                        if temp[2] > lst[j][2] :
                            lst[j+1] = lst[j]
                            j -= 1
                    else:
                        lst[j+1] = temp
            
            def bubble_sort_time(lst):
                n = len(lst)
                for i in range(n): # Number of passes
                    for j in range(0, n-i-1):
                
                        if lst[j][2] == lst[j+1][2]:
                            if lst[j][3] > lst[j+1][3]:
                            # Swap element at jth position with (j+1)th position
                                lst[j], lst[j+1] = lst[j+1], lst[j]

            score, time = game_loop()
            
            player = [100, name, score , time]
            if con.is_connected():
                mycursor = con.cursor()

                query1 = 'select * from leaderboard'
                mycursor.execute(query1)
                result = mycursor.fetchall()
                lst = []
                print()

                if len(result) != 0:
                    for i in range(len(result)):
                        a = list(result[i])
                        lst.append(a)
                        
                    lst.append(player)
                    insertion_sort_scores(lst)
                    bubble_sort_time(lst)

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
                mycursor.executemany(query3, lst)
                con.commit()

            con.close()

            if score == 1000:
                return 'win'
            else:
                return 'lose'


