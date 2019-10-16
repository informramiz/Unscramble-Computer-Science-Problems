# Unscramble-Computer-Science-Problems
A set of 4 very basic algorithm problems solved in Python.


## Run Time Analysis

**Note:** I have provided run time analysis for my own solution and not the code provide for reading calls and texts files. Still to share info, the time read files is O(n) where n is the number of characters inside the bigger file. 

Also, the worst case time for dictionary will be constant as I am only keeping one value against each key so no key collisions.

### Task 0: O(1)

In this task we only access first and last element inside an array and because accessing element inside an array is a constant time `(O(1))` operation so this task takes `O(1)` time in worst case.

### Task 1: O(n)

1. Go through each record in `calls` to keep track of duration for each number inside a dictionary (which is constant time). This costs `O(X)` assuming `X` is the number of call records. 
2. Go through each record in `texts` to keep track of duration inside the same dictionary (again constant time). This costs `O(Y)` assuming `Y` is the number of call records and dictionary access is constant time. run time is `O(X) + O(Y)`
3. `O(X) + O(Y)` can be simplified for worst case to `O(n)` as both loops are serial and not nested and we are only interested in large input for worst case.

### Task 2: O(n)

1. First we go through all the numbers inside `calls` to sum up call duration for each number and this is `O(n)` and as dictionary operations will cost constant time.
2. Second we go through all possible numbers (which can be at most n, in case all numbers were unique) and keep track of only max duration number. This costs `O(n)`
3. So the total cost is `O(n)`

### Task 3: O(nlgn)

1. Go through all call records and find the ones that were called from banglore. This will cost `O(n)` in worst case as all functions being called inside this loop will not cost more than 10 operations (because area codes are always lesser than 10) which is `O(1)`
2. Remove duplicates and sort the unique codes, this in total costs `O(nlgn)` 
3. Go through all codes that were called from Bangalore and filter the ones are from Banglore. This costs `O(n)` in worst case
4. Print all codes, `O(n)`
4. Total is `O(n) + O(nlgn) + O(n) = O(nlgn)`

### Task 4: O(nlgn)

1. Filter all the call receivers by going through all call records and remove duplicates, total worst case `O(n)`.
2. Find the numbers that sent texts by going through all the `texts` records, total worst case `O(n)`
3. Find the numbers that that received texts and merge them with text senders, total worst case `O(n)`
4. Go through all numbers in `calls` and filter the ones that are not in `texters` set and also not in `call_receivers`. As the set lookup is `O(1)` so total worst case time cost is `O(n)`
5. Filter numbers are sorted, which is `O(nlgn)`
6. Numbers are printed which is `O(n)`
7. Total is `O(n) + O(n) + O(n) + O(n) + O(nlgn) + O(n) = O(nlgn)`