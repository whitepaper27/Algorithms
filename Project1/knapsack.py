# -*- coding: utf-8 -*-

"""

knapsack.py - CS6515, Intro to Graduate Algorithms

Implement a Dynamic Programming Solution to the knapsack problem.   The program will be given a set
of items and a weight limit, and it should select the combination of items which achieves the highest
value without exceeding the weight limit.   Each item may only be selected once (non-repeating).

"""
import argparse  # argparse allows the parsing of command line arguments
import GA_ProjectUtils as util  # utility functions for cs 6515 projects


def initTable(numItems, maxWt):
    """
    Initialize the table to be used to record the best value possible for given
    item idx and weight
    NOTE : this table must:
              -- be 2 dimensional (i.e. T[x][y])
              -- contain a single numeric value (no tuples or other complicated abtract data types)
    """
    # TODO Replace the following with your code to initialize the table properly
    # Same code used for Summer 2021 by Sahil Soni
    #I have dropped class from summer 2021 . So I am using same/modified code for Fall 2021.
    #T = [0][0]
    T=[]
    #for i in range(len(numItems)+1):
    for i in range(numItems+1):
        x=[]#1st array of 1d to inistalized table
        for y in range(maxWt+1):
            x.append(0)#2nd y append to list
            #print(x)
        T.append(x)
    #print(T)
    #A=T
    return T


def buildItemIter(numItems):
    """
    Build item iterator - iterator through all available items
        numItems : number of items
    """
    # TODO Replace the following with your code to build the item iterator

    return range(1, numItems + 1)
    # return range(numItems + 1)


# return range(0)


def buildWeightIter(maxWt):
    """
    Build weight iterator - iterator of all possible integer weight values
        maxWt : maximum weight available
    """
    # TODO Replace the following with your code to build the weight iterator

    return range(0, maxWt + 1)
    #return range(0)


def subProblem(T, iterWt, itemIDX, itemWt, itemVal):
    """
    Define the subproblem to solve for each table entry - set the value to be maximum for a given
    item and weight value
        T : the table being populated
        iterWt : weight from iteration through possible weight values
        itemIDX : the index of the item from the loop iteration
        itemWt : the weight of the item
        itemVal : the value of the item
    """
    # TODO Replace the following with your code to solve the subproblem appropriately!

    if itemWt <=iterWt:
        T[itemIDX][iterWt] = max(itemVal+T[itemIDX-1][iterWt-itemWt],T[itemIDX-1][iterWt]          )
       # if T[itemIDX][iterWt] >=400:
       #     a=T[itemIDX][iterWt]
    else:
        T[itemIDX][iterWt] = T[itemIDX-1][iterWt]
      #  if T[itemIDX][iterWt] >=400:
        #    a=T[itemIDX][iterWt]
    #print(T[itemIDX][iterWt])
    return T[itemIDX][iterWt]

    #return T[0][0]


def buildResultList(T, items, maxWt):
    """
    Construct list of items that should be chosen.
        T : the populated table of item values, indexed by item idx and weight
        items : list of items
        maxWt : maximum weight allowed

    	result: a list composed of item tuples
    """
    result = []
    n=len(items)
    #print(T)
    final_value=T[n][maxWt]#1050
    for i in reversed(range(1,n+1)):
        if final_value != T[i-1][maxWt] and final_value>0:
            result.append(items[i])
            final_value=final_value-items[i][2]
            maxWt=maxWt-items[i][1]

    # TODO Your code goes here to build the list of chosen items!

    return result


def knapsack(items, maxWt):
    """
    Solve the knapsack problem for the passed list of items and max allowable weight
    DO NOT MODIFY THE FOLLOWING FUNCTION
    NOTE : There are many ways to solve this problem.  You are to solve it
            using a 2D table, by filling in the function templates above.
            If not directed, do not modify the given code template.
    """
    numItems = len(items)
    # initialize table properly
    table = initTable(numItems, maxWt)
    # build iterables
    # item iterator
    itemIter = buildItemIter(numItems)
    # weight iterator
    weightIter = buildWeightIter(maxWt)

    for itmIdx in itemIter:
        # query item values from list
        item, itemWt, itemVal = items[itmIdx]
        for w in weightIter:
            # expand table values by solving subproblem
            table[itmIdx][w] = subProblem(table, w, itmIdx, itemWt, itemVal)

    # build list of results - chosen items to maximize value for a given weight
    return buildResultList(table, items, maxWt)


def main():
    """
    The main function
    """
    # DO NOT REMOVE ANY ARGUMENTS FROM THE ARGPARSER BELOW
    # You may change default values, but any values you set will be overridden when autograded
    parser = argparse.ArgumentParser(description='Knapsack Coding Quiz')
    parser.add_argument('-i', '--items', help='File holding list of possible Items (name, wt, value)',
                        default='defaultItems.txt', dest='itemsListFileName')
    parser.add_argument('-w', '--weight', help='Maximum (integer) weight of items allowed', type=int, default=700,
                        dest='maxWeight')

    # args for autograder, DO NOT MODIFY ANY OF THESE
    parser.add_argument('-n', '--sName', help='Student name, used for autograder', default='GT', dest='studentName')
    parser.add_argument('-a', '--autograde', help='Autograder-called (2) or not (1=default)', type=int, choices=[1, 2],
                        default=1, dest='autograde')
    args = parser.parse_args()

    # DO NOT MODIFY ANY OF THE FOLLOWING CODE
    itemsList = util.buildKnapsackItemsDict(args)
    itemsChosen = knapsack(itemsList, args.maxWeight)
    util.displayKnapSack(args, itemsChosen)


if __name__ == '__main__':
    main()
