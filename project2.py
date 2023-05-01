# Sololearn: Python Data Structure Code Project 2: Average Word Length

# Problem: Given a sentence as input, calculate and output the average word length of that sentence.
#          To calculate the average word length, you need to divide the sum of all word lengths by 
#          the number of words in the sentence.

# Sample Input: "this is some text"
# Sample Output: 3.5

# Explanation: There are 4 words in the given input, with a total of 14 letters,
#              so the average length will be: 14/4 = 3.5

# My Solution:

# 1. Accept sentence (s) as input.
s = input()

# 2. Split the (s) to have a list, this helps calculating num of words in the sentence.
n = s.split()

# 3. Calculate the number of words in the sentence, using the len function.
ln = len(n)

# 4. Assume the length of the unknown (s) to be 0.
ls  = 0

# 5. Loop through the sentence.
for x in s:

    # 6. Take away spaces looped as el in the sentence.
    if x != " ":
      
    # 7. For every el in e, count it by adding 1 to ls (length of sentence).
      ls += 1

# 8. With the derived parameters, ls = length of sentence, ln = length of words in sentence,
#    we calculate the averge word length.

# 9. Average word length.
avg = (ls/ln)
print(avg)

# Hossanadev (: