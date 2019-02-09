# Name: Lina Chung
# Program: Python Assignment 1
# Description:  Given a starting word, find the shortest ladder of single letter changes which leads to a final word

MIN_VALUE = 4
MAX_VALUE = 6

def main():
    dictionary = get_Dict("dictionary.txt")
    testfile = input("Enter file for pair of words: ")
    result = get_Test(testfile, dictionary)
    print(result)

# Function to read in the dictionary
def get_Dict(filename):
    global MIN_VALUE
    global MAX_VALUE
    d = {}
    f = open(filename,'r')
    for line in f:
        word = line.strip('\n')
        if MAX_VALUE >= len(word) >= MIN_VALUE:
            if len(word) not in d:
                d[len(word)] = [word]
            else:
                d[len(word)].append(word)
    f.close()
    return d

# Function to read in the pair file and find shortest ladder
def get_Test(filename,dictionary):
    with open(filename) as t:
        for line in t:
            line = line.split()
            start = line[0]
            end = line[-1]
            print(wordLadder(start,end,dictionary[len(start)]))

# Function to find difference of one character between words 
def difference(word1, word2):
    difference = 0
    if len(word1) != len(word2):
        return [False]
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            difference += 1
    return difference == 1

# Function to find shortest path to end result 
def wordLadder(start, end, dictionary):
    if len(start) != len(end):
        return ('Length of start word and end word are not the same')
    if start == end:
        return [start]
    curr = [start]
    path = [[start]]
    visited = []
    while(len(path)>0):
        curr = path.pop(0)
        for word in dictionary:
            if difference(curr[-1],word) and word not in visited:
                path.append(curr + [word])
                visited.append(word)
                if word == end:
                        return path[-1]
    return ('No ladder found')

if __name__ == "__main__":main()
