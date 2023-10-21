from FINAL_GAME import game_loop
import mysql.connector as m
if __name__ != '__main__':
    def run_game(name):             #fn called in menu.py
            con = m.connect(host = 'localhost', username = 'root', passwd = 'dashmaharaj05', db = 'project')

            def insertion_sort_scores(lst):         #sort the scores from highest to lowest using insertion sort algorithm
                length = len(lst)
                for i in range(1, length):
                    temp = lst[i]
                    j = i-1
                    while j >= 0 and temp[2] > lst[j][2]:

                        if temp[2] > lst[j][2] :        # If score is greater
                            lst[j+1] = lst[j]           # Swap element at jth position with (j+1)th position
                            j -= 1
                    else:
                        lst[j+1] = temp
            
            def bubble_sort_time(lst):          # sort the scores, if equal, based on time taken to complete from lowest to highest
                                                # using bubble sort algorithm
                n = len(lst)
                for i in range(n): # Number of passes
                    for j in range(0, n-i-1):
                
                        if lst[j][2] == lst[j+1][2]:                    # Check if scores are equal
                            if lst[j][3] > lst[j+1][3]:                 # If time is greater
                                lst[j], lst[j+1] = lst[j+1], lst[j]     # Swap element at jth position with (j+1)th position

            #---------------------------------------------------------------------------
            
            score, time = game_loop()                           # run the game and store the returned values
            
            player = [100, name, score , time]
            if con.is_connected():
                mycursor = con.cursor()

                query1 = 'select * from leaderboard'
                mycursor.execute(query1)
                result = mycursor.fetchall()                    #returns result as tuples nested in a list
                lst = []

                if len(result) != 0:                            #if players data exists
                    for i in range(len(result)):
                        a = list(result[i])                     #convert result tuples into lists
                        lst.append(a)
                        
                    lst.append(player)                          #append player data
                    insertion_sort_scores(lst)                  #sort player ranking based on score
                    bubble_sort_time(lst)                       #based on time if their scores are equal

                    for i in range(len(lst)):                   #using index posn as iterable i, 
                        lst[i][0] = i+1                         #change rank to i+1 since indexing starts from 0
                        lst[i] = tuple(lst[i])                  #convert nested lists back to nested tuples
                    
                    if len(lst) > 5:
                        lst.pop()

                elif len(lst) == 0:                             #if no player data exists
                    lst.append(player)
                    lst[0][0] = 1                               #change rank to 1
                    lst[0] = tuple(lst[0])                      #convert nested list to nested tuple

                
                query2 = 'delete from leaderboard'              #delete existing data, since data may have changed after last play
                mycursor.execute(query2)
                con.commit()
                
                query3 = 'insert into leaderboard values (%s,%s,%s,%s)'         #insert new data into sql table
                mycursor.executemany(query3, lst)
                con.commit()

            con.close()

            if score == 1000:       #return score to decide which window should be displayed - win or lose
                return 'win'
            else:
                return 'lose'


