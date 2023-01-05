import pandas
import numpy

# Read excel file -> Dataframe
df = pandas.read_excel("xl.xlsx")

# Converting to an array
array = df[1].to_numpy()
array = numpy.insert(array, 0, df.columns[0])  # Adding the colName at beginning of the array as colName is also an "id"

# Size of the array
lenOfArray = len(df)

# Calculating total run of the loop
runEachTime = 4
totalRun = lenOfArray / runEachTime
totalRunInt = int(totalRun)
loopTotalRun = totalRunInt if totalRunInt == lenOfArray else totalRunInt + 1

# Read 4 items each time from the array
start = 0
end = 4
for i in range(loopTotalRun):
    # Reading array containing 4 items
    print(array[start:end])

    # Increase the index
    start += runEachTime
    end += runEachTime
