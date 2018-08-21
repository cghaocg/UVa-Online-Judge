'''
    Once upon a time in a far, far away forest, there was a team of lazy lumberjacks. Since they were too
lazy to cut trees, they were always figuring out ways to sneak out of work. Their foreman, on the other
side, was always trying to put them all to work.
    After a lot of discussions the foreman and the lumberjacks came to an agreement: they will work,
but only if the area of the forest assigned to each one was a triangle. If it was any other shape they will
be free not to work that week. The idea was to give each lumberjack three numbers representing the
length of each of the triangles side. If the numbers were correct and form a triangle, the lumberjacks
had to work, else, they were free to leave and not work.
    Since our lumberjacks are as cunning as they are lazy, they convince the foreman to let them
determine the surface and the site in the forest were they will work. As a result, the lumberjacks keep
passing the foreman sets of numbers that could not form the sides of a triangle. After a while, the
foreman began to suspect and decide to write a program that validates the input of each lumberjack.
Now when the lumberjacks decide to pass wrong numbers they get a fine of $1000.00 (more than a
day’s salary).
    Your job is to write the program that the foreman has to use to determine if the numbers (all
integers) passed by the lumberjacks can be the sides of a triangle. If they can, you have to print ‘OK’
else you have to print ‘Wrong!!’

[Input]
The input consist in a data set describing the numbers of that each lumberjack has passed to the
foreman for the day. The data is formatted as follows:
The first line is an integer N (2 ≤ N ≤ 20). Then follows N lines, each one containing three integers
separated by a space.
[Output]
For each line in the input you have to find if the integers can represent the sides of a triangle. If they
can you have to print ‘OK’ for each line in the input, else you have to print ‘Wrong!!’

[Sample Input]
6
1 2 3
3 2 5
3 4 5
6 6 1
3 3 3
7 3 10
[Sample Output]
Wrong!!
Wrong!!
OK
OK
OK
Wrong!!
'''

# 輸入測試資料組數
number = int(input())

li_testCases = []
# 輸入測試資料
for a in range(number):
    li_testCases.append(input())

li_output = []
# 處理每一筆測資
for triangle in li_testCases:
    # 取出欲判斷的三個邊長
    li_side = triangle.split(' ')
    # 判斷，任兩邊的和大於第三邊，即為三角形
    if int(li_side[0]) + int(li_side[1]) > int(li_side[2]) and int(li_side[0]) + int(li_side[2]) > int(li_side[1]) and int(li_side[1]) + int(li_side[2]) > int(li_side[0]) :
        answer = 'OK'
    else :
        answer = 'Wrong!!'
    print(answer)

