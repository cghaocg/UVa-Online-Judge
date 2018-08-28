'''
Encoding is the process of transforming information from one format into another. There exist several
different types of encoding scheme. In this problem we will talk about a very simple encoding technique;
Run-Length Encoding.
Run-length encoding is a very simple and easy form of data compression in which consecutive
occurrences of the same characters are replaced by a single character followed by its frequency. As an
example, the string ‘AABBBBDAA’ would be encoded to ‘A2B4D1A2’, quotes for clarity.
In this problem, we are interested in decoding strings that were encoded using the above procedure.

[Input]
The first line of input is an integer T (T < 50) that indicates the number of test cases. Each case is
a line consisting of an encoded string. The string will contain only digits [0-9] and letters [A-Z]. Every
inputted string will be valid. That is, every letter will be followed by 1 or more digits.
[Output]
For each case, output the case number followed by the decoded string. Adhere to the sample for exact
format.
You may assume the decoded string wont have a length greater than 200 and it will only consist of
upper case alphabets.

[Sample Input]
3
A2B4D1A2
A12
A1B1C1D1
[Sample Output]
Case 1: AABBBBDAA
Case 2: AAAAAAAAAAAA
Case 3: ABCD
'''
import re

# 判斷為字母或數字
def alphaOrNum(self):
    if re.search('[A-Z]',self):
        return 'A'
    elif re.search('[0-9]',self):
        return 'N'

# 輸入測試資料組數
number = int(input())

li_testCases = []
# 輸入測試資料
for a in range(number):
    li_testCases.append(input())

output = []
total = 0
# 處理每一筆測試資料
for testCase in li_testCases:
    total = total + 1
    tempNum = ''
    case = ''
    isCalcu = False
    # 將字串以字元存成陣列
    li_tempAlpha = list(testCase)
    # 處理每個字元
    for x in range(0,len(li_tempAlpha)):
        # 字母
        if (alphaOrNum(li_tempAlpha[x]) == 'A'):
            tempChar = li_tempAlpha[x]
        # 字母出現次數
        elif (alphaOrNum(li_tempAlpha[x]) == 'N'):
            tempNum = tempNum + li_tempAlpha[x]
            # 判斷下一個字元不會超出索引再往下執行
            if (x+1 < len(li_tempAlpha)):
                # 判斷下一個出現的字元是字母or數字
                if (alphaOrNum(li_tempAlpha[x+1]) == 'A'):
                    isCalcu = True
            # 此字元為最後一個字元
            else :
                isCalcu = True

        if (isCalcu):
            for i in range(int(tempNum)):
                case = case + tempChar
            tempNum = ''
            isCalcu = False
    output.append(case)
    print('Case', str(total) + ':', case)
