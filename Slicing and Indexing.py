
# Python slice
#a[start:end] # items start through end -1
#a[start:]  # items start through the rest of the array
# a[;end]   # items from the begining through end -1
# a[:]      # a copy of the whole array
#a[start:end:step]  # start through not past end, by step





#slicing and indexing  with 2D array
import array
array2 = array.array([2,4,6], [1,3,5], [22,23,24], [13,14,15])
print (array2)

######
##a = [1,2,3,4,5,6,7,8,9]
##a[-5:0]

--- no results

##a[-5:-1]-----[5,6,7,8]
##a[-5:]
##[5,6,7,8,9]
a[-1]
9
a[-2]
8
a[::-1]
9,8,7,6,5,4,3,2,1,0

a[1::-1]
1,0

a[:-3:-1]
[9,8]
a[-3::-1]
[7,6,5,4,3,2,1]

###a[:7]
##[0,1,2,3,4,5,6]

###a[:]
##[0,1,2,3,4,5,6,7,8,9]

##a[1:8:2]---starting,ending and increment
###[1,3,5,7]

#a[10:0:-2]

(9,7,5,3,1)
a[::-2]

[9,7,5,3,1]





