
class sumBlock:
    def __init__(self, sumTotal, numCells, cellList, solutionList):
        self.sumTotal = sumTotal
        self.numCells = numCells
        self.cellList = cellList
        self.solutionList = solutionList


def findPossibleSolutions(value, solutions):
    """ Given a value, find all sets of solutions that satisfy the conditions """
    result = []
    for i in range(len(solutions)):
        if value == solutions[i][0]:
            result.append([len(solutions[i][1][0]), solutions[i][1]])
    return result


def sixCells(total, alphabet):
    """ Given a total value of six cells, return all combinations of Sudoku-legal values that add up to the sum """
    result = []
    for i in alphabet:
        for j in alphabet:
            for k in alphabet:
                for m in alphabet:
                    for n in alphabet:
                        for o in alphabet:
                            if i != j and i != k and i != m and i != n and i != o and j != k and j != m and j != n and j != o and k != m and k != n and k != o and m != n and m != o and n != o and i + j + k + m + n + o == total:
                                if sorted([i, j, k, m, n, o]) not in result and i + j + k + m + n + o == total:
                                    result.append(sorted([i, j, k, m, n, o]))
    return result


def fiveCells(total, alphabet):
    """ Given a total value of five cells, return all combinations of Sudoku-legal values that add up to the sum """
    result = []
    for i in alphabet:
        for j in alphabet:
            for k in alphabet:
                for m in alphabet:
                    for n in alphabet:
                        if i != j and i != k and i != m and i != n and j != k and j != m and j != n and k != m and k != n and m != n and i + j + k + m + n == total:
                            if sorted([i, j, k, m, n]) not in result:
                                result.append(sorted([i, j, k, m, n]))
    return result


def fourCells(total, alphabet):
    """ Given a total value of four cells, return all combinations of Sudoku-legal values that add up to the sum """
    result = []
    for i in alphabet:
        for j in alphabet:
            for k in alphabet:
                for m in alphabet:
                    if i != j and i != k and i != m and j != k and j != m and k != m and i + j + k + m == total:
                        if sorted([i, j, k, m]) not in result:
                            result.append(sorted([i, j, k, m]))
    return result


def threeCells(total, alphabet):
    """ Given a total value of three cells, return all combinations of Sudoku-legal values that add up to the sum """
    result = []
    for i in alphabet:
        for j in alphabet:
            for k in alphabet:
                if i != j and i != k and j != k and i + j + k == total:
                    if sorted([i, j, k]) not in result:
                        result.append(sorted([i, j, k]))
    return result


def twoCells(total, alphabet):
    """ Given a total value of two cells, return all combinations of Sudoku-legal values that add up to the sum """
    result = []
    for i in alphabet:
        for j in alphabet:
            if i != j and i + j == total and [j, i] not in result:
                result.append([i, j])
    return result


def sudoku_main():
    print("Welcome to the Killer Sudoku solver that me, this guy, wrote.")
    print("For all intents and purposes, we will go row by column.")
    print("The first row is rows[0] on the top and the last row is rows[8] on the bottom.")
    print("The first column is columns[0] on the left and the last column is columns[8] on the right.")
    print("The subgrids go from top left to bottom right, with the first three on top, the second three in the middle, and the last three on bottom.")
    print("This is the puzzle without any values inserted.")
    
    puzzle = [[0]*9]*9
    for i in range(9):
        print(puzzle[i])

    # temp = []
    # rows = [[]*9]
    # for i in range(9):
    #     for j in range(9):
    #         temp.append(puzzle[i][j])
    #     rows[i].extend(temp)
    #     print("For testing:")
    #     print(rows[i])
    # columns = [[]*9]
    # for i in range(9):
    #     for j in range(9):
    #         temp.append(puzzle[j][i])
    #     columns[i].extend(temp)
    #     print("For testing:")
    #     print(columns[i])
    alphabet = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    solutions = []
    found = False
    numBlocks = int(input("Enter total number of sum blocks: "))
    listOfBlocks = [sumBlock] * numBlocks
    for i in range(numBlocks):
        listOfBlocks[i].userValue = int(input(f"Enter total value of sumBlock {i+1}: "))
        listOfBlocks[i].numCells = int(input(f"Enter total number of cells in sumBlock {i+1}: "))
    
        if listOfBlocks[i].numCells < 1:
            print("That input doesn't make any sense. There has to be at least one cell.")
            exit
        if listOfBlocks[i].numCells == 1:
            if sumBlock[i].userValue > 0 and sumBlock[i].userValue < 10:
                print(f"If there's only one cell, you already know the answer is {sumBlock[i].userValue}.")
            else:
                print(f"That input doesn't make any sense. You can't have a sum of {sumBlock[i].userValue} in only one cell.")
        if listOfBlocks[i].numCells > 6:
            print("There aren't any blocks in Killer Sudoku with more than 6 cells. Do better.")
            exit

        # sumBlock[i].cellList = []

        for i in range(listOfBlocks[i].numCells):
            sumBlock[i].cellList.append(int(input(f"Enter cell number {i+1}: ")))
        
        if listOfBlocks[i].numCells > 1:
            totalsWithTwo = []
            for i in range(sum(alphabet[:2]), sum(alphabet[7:]) + 1):
                totalsWithTwo.append([i, twoCells(i, alphabet)])
            solutions.extend(totalsWithTwo)
        if listOfBlocks[i].numCells > 2:
            totalsWithThree = []
            for i in range(sum(alphabet[:3]), sum(alphabet[6:]) + 1):
                totalsWithThree.append([i, threeCells(i, alphabet)])
            solutions.extend(totalsWithThree)
        if listOfBlocks[i].numCells > 3:
            totalsWithFour = []
            for i in range(sum(alphabet[:4]), sum(alphabet[5:]) + 1):
                totalsWithFour.append([i, fourCells(i, alphabet)])
            solutions.extend(totalsWithFour)
        if listOfBlocks[i].numCells > 4:
            totalsWithFive = []
            for i in range(sum(alphabet[:5]), sum(alphabet[4:]) + 1):
                totalsWithFive.append([i, fiveCells(i, alphabet)])
            solutions.extend(totalsWithFive)
        if listOfBlocks[i].numCells > 5:
            totalsWithSix = []
            for i in range(sum(alphabet[:6]), sum(alphabet[3:]) + 1):
                totalsWithSix.append([i, sixCells(i, alphabet)])
            solutions.extend(totalsWithSix)

        solved = findPossibleSolutions(listOfBlocks[i].numCells, solutions)
        listOfBlocks[i].solutionList = solved

    for i in range(numBlocks):
        print(listOfBlocks[i])
        for i in range(len(solved)):
            if listOfBlocks[i].numCells == solved[i][0]:
                found = True
                sames = [] 
                sameCount = [] 
                sameFinal = []
                print(f"List of {len(solved[i][1])} solution(s) for a group of {userNum} cells with total value of {userValue}: {solved[i][1]}")
                for j in range(len(solved[i][1])):
                    for k in range(len(solved[i][1][j])):
                        sames.append(solved[i][1][j][k])
                for m in range(len(alphabet)):
                    sameCount.append(sames.count(m + 1))
                for n in range(len(sameCount)):
                    if sameCount[n] == len(solved[i][1]):
                        sameFinal.append(n + 1)
                if len(sameFinal) == 1:
                    print(f"There is 1 number that shows up in all solutions: {sameFinal[0]}")
                elif len(sameFinal) > 1:
                    print(f"There are {len(sameFinal)} numbers that show up in all solutions: {sameFinal}")
                else:
                    print("There are not any numbers that show up in every solution.")
        if not found: 
            print(f"There are no solutions for a group of {userNum} cells with total value of {userValue}.")

if __name__ == '__main__':
    sudoku_main()
