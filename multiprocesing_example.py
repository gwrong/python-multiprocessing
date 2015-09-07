import time
from multiprocessing import Pool

NUM_POOLS = 12

#Making this a function sped up runtime by 12%
def sum_line(line):
    lineSum = 0
    elements = line.rstrip().split(',')
    for element in elements:
        lineSum = lineSum + int(element)
    return int(lineSum)

def main():

    #no multiprocessing
    dataFile = open('poker-hand-testing.data')
    start = time.time()
    totalSum = 0

    #Boring sum over all the lines
    for line in dataFile:
        totalSum = totalSum + sum_line(line)

    dataFile.close()
    end = time.time()
    timeTaken = end - start
    print('Sum: ' + str(totalSum))
    print('Time taken without multiprocessing: ' + str(timeTaken) + ' seconds')

    #multiprocessing time
    dataFile = open('poker-hand-testing.data')
    start = time.time()

    #We create a pool that manages the processes
    pool = Pool(NUM_POOLS)

    #The map function takes in an iterable and sends
    #the chunks into separate processes
    results = pool.map(sum_line, dataFile, NUM_POOLS)

    #We have to sum the resulting array which is a list of result sums
    totalSum = sum(results)
    end = time.time()
    timeTaken = end - start
    print('Sum: ' + str(totalSum))
    print('Time taken with multiprocessing: ' + str(timeTaken) + ' seconds')
    dataFile.close()

if __name__ == "__main__":
    main()