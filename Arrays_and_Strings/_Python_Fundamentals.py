# for x in range(1,1001):
# 	if x%2 == 1:
# 		print x

# for x in range(5,1000001):
# 	if x%5 == 0:
# 		print x

# sum = 0
# for count in a:
# 	sum += count
# print sum
# print sum/len(a)

def counting():
	for x in range(1,2001):
		if x%2 == 1:
			y = "odd"
		else:
			y = "even"
		print "number is {}. This is an {} number.".format(x, y)

def multiply(list,z):
	new = []
	for x in list:
		new.append(x * z)
	return new

import random
chance = random.randint(0,1)
def coin_toss():
	head = 0
	tail = 0
	for x in range (1,5001):
		chance = random.randint(0,1)
		if chance == 0:
			head += 1
			print "Attempt #{}: throwing a coin... It's a head! ... got {} head(s) so far and {} tails(s) so far".format(x,head,tail)
		else:
			tail += 1
			print "Attempt #{}: throwing a coin... It's a Tail! ... got {} head(s) so far and {} tails(s) so far".format(x,head,tail)
coin_toss()

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(array):
	for idx, item in enumerate(array):
		print idx


# draw_stars(y)

users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def displayStudents(users):
	y= 0
	for x in users['Students']:
		length = len(x['first_name']+x['last_name'])
		print "{} - {} {} - {}".format(y, x['first_name'], x['last_name'], length)
		y += 1
	print 'Instructors'
	y = 1
	for x in users['Instructors']:
		length = len(x['first_name']+x['last_name'])
		print "{} - {} {} - {}".format(y, x['first_name'], x['last_name'], length)
		y += 1

	for key, value in users.items():
		print key
		counter = 1
		for i in range(len(value)):
			First = value[i]['first_name']
			Last = value[i]['last_name']
			length = len(First+Last)
			print '{} - {} {} - {}'.format(counter, First.upper(), Last.upper(), length)
			counter += 1

'''BUBBLE SORT'''
def bubble(x):
	for i in range(len(x)-1):
		for j in range(len(x)-i-1):
			if x[j]>x[j+1]:
				(x[j],x[j+1]) = (x[j+1],x[j])

'''SELECTION SORT'''
def selection(x):
	for i in range(len(x)):
		min = i
		for j in range(i,len(x)):
			if x[j] < x[min]:
				min = j
		(x[i],x[min]) = (x[min],x[i])

'''INSERTION SORT'''
def insertion(x):
	for i in range(1,len(x)):
		swap = i
		for j in range(i-1,-1,-1):
			if x[swap] < x[j]:
				(x[swap],x[j]) = (x[j],x[swap])
				swap -= 1
		print x

'''Threes and Fives'''
def threesFives():
	for x in range (100, 4000001):
		if x%3==0 and x%5==0:
			continue
		elif x%3==0:
			print x
		elif x%5==0:
			print x

'''Generate Coin Change'''
import math
def generatechange(x):
	coins = ['quarters', 'dimes', 'nickels', 'pennies']
	change = {'quarters': 25, 'dimes': 10, 'nickels': 5, 'pennies': 1}
	remainder = x
	for x in coins:
		print x
		value = change[x]
		number = math.floor(remainder/value) 
		if number >= 1:
			change[x] = number
			remainder = remainder - (number * value)
		else:
			change[x] = 0
	print "{} coins can be represented by:".format(x)
	for x in coins:
		print "{}: {}".format(x, change[x])


def messyMath(num):
	sum = 0
	count = 0
	for x in range (1, num+1):
		count +=1
		if count == (float(num)/3):
			return -1
		if count % 3 == 0:
			continue
		elif count % 7 == 0:
			sum += x
		sum += x
	return sum

def bars():
	for x in range(1,13):
		print x
		print 'chick'
		print 'boom'
		print 'chick'

def Fibonacci(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return Fibonacci(x-1) + Fibonacci(x-2)

def sumtoOne(num):
	if len(str(num)) ==1:
		return num
	sum = 0
	for x in range (len(str(num))):
		number = int(str(num)[x])
		sum += number
	return sumtoOne(sum)

def isprime(num):
	for x in range(2, int(math.sqrt(num))+1):
		if num%x==0:
			return False
	return True

def sweatshirtPricing(num):
	total = num * 20
	discount = 0
	if num == 2:
		discount = .09
	elif num == 3:
		discount = .19
	elif num >= 4:
		discount = .35
	return math.ceil(total*(1-discount))

def extractDigit(num, digit):
	string = str(num)
	length = len(string)
	if digit >= length:
		return 1
	return string[length-digit-1]

def sigfig(num):
	num = abs(num)
	while num < 1:
		num = num*10
	while num > 10:
		num = num/10
	return int(math.floor(num))		

'''gaming Fundamentals'''
import random

def rollOne():
	return random.randint(1,6)

def playfives(num):
	x = num
	while x>0:
		number = rollOne()
		if number == 5:
			print "that's good luck"
		x -= 1

def playStats():
	x = 8
	min = 6
	max = 1
	while x>0:
		number = rollOne()
		if number < min:
			min = number
		if number > max:
			max = number
		x -= 1
	return min, max

def playStats2():
	x = 8
	sum = 0
	min = 6
	max = 1
	while x>0:
		number = rollOne()
		if number < min:
			min = number
		if number > max:
			max = number
		x -= 1
		sum += number
	return min, max, sum

def playStats3(num):
	x = num
	sum = 0
	min = 6
	max = 1
	while x>0:
		number = rollOne()
		if number < min:
			min = number
		if number > max:
			max = number
		x -= 1
		sum += number
	return min, max, sum

def playStats4(num):
	x = num
	sum = 0
	min = 6
	max = 1
	while x>0:
		number = rollOne()
		if number < min:
			min = number
		if number > max:
			max = number
		x -= 1
		sum += number
	return min, max, sum

def playStats20():
	sum = 0
	min = 20
	max = 1
	count = 0
	prev = 0 
	number = random.randint(1,20)
	while prev != number:
		count += 1 
		if number < min:
			min = number
		if number > max:
			max = number
		prev = number
		number = random.randint(1,20)
		sum += number
	return min, max, sum, sum/count 

'''ARRAYS'''
array = [1,2,3,4,5,6,6,7,8,9,10]

def pushFront(arr, num):
	arr.append(arr[len(arr)-1])
	for x in range(len(arr)-2,-1,-1):
		arr[x+1] = arr[x]
	arr[0] = num
	return arr

def popFront(arr):
	for x in range (0, len(arr)-1):
		arr[x]=arr[x+1]
	arr.pop()
	return arr

def insertAt(arr, idx, num):
	arr.append(arr[len(arr)-1])
	for x in range(len(arr)-2,idx-1,-1):
		arr[x+1] = arr[x]
	arr[idx] = num
	return arr

def removeAt(arr, idx):
	if idx > len(arr)-1:
		return 'idx too large'
	for x in range (idx, len(arr)-1):
		arr[x]=arr[x+1]
	arr.pop()
	return arr

def swapPairs(arr):
	length = len(arr)
	if len(arr) % 2 != 0:
		length -= 1
	for x in range (0, length, +2):
		(arr[x], arr[x+1]) = (arr[x+1], arr[x])
	return arr

def removedupes(arr):
	value = arr[len(arr)-1]
	for x in range(len(arr)-2, -1, -1):
		if arr[x] == value:
			removeAt(arr, x)
		value = arr[x]
	return arr

array = [1,2,3,4,5,6,6,7,8,9,10]

def mintoFront(arr):
	min = 0
	for x in range (1,len(arr)):
		if arr[x] < arr[min]:
			min = x
	pushFront(arr, arr[min])
	removeAt(arr, min+1)
	return arr

def reverse(arr):
	for x in range (0, len(arr)/2):
		temp = arr[x]
		arr[x] = arr[len(arr)-1-x]
		arr[len(arr)-1-x] = temp
	return arr

def rotate(arr, shift):
	x = shift%len(arr)
	while x >0:
		y =  arr[len(arr)-1]
		pushFront(arr, y)
		arr.pop()
		x -= 1
	return arr

def filter(arr, min, max):
	for x in range(len(arr)-1, -1, -1):
		if arr[x]< max and arr[x]>min:
			removeAt(arr,x)
		print arr
	return arr

def concat(arr, arr2):
	newarr = []
	for x in range(0, len(arr)):
		newarr.append(arr[x])
	for x in range(0, len(arr2)):
		newarr.append(arr2[x])
	return newarr

array2 = [-2,0,2,5,-7,3,-2,4,9]

def skyline(arr):
	newarr = []
	min = 0
	for x in range(0, len(arr)):
		if arr[x]>min:
			newarr.append(arr[x])
			min = arr[x]
	return newarr

def removeNegs(arr):
	for x in range(len(arr)-1, -1, -1):
		if arr[x]<0:
			removeAt(arr, x)
	return arr

def secondtolast(arr):
	if len(arr)<2:
		return null
	return arr[len(arr)-2]

def secondLargest(arr):
	if len(arr)<2:
		return null
	max = arr[0]
	max2 = arr[0]
	for x in range(1, len(arr)):
		if arr[x]>max:
			max = arr[x]
	for x in range(1, len(arr)):
		if arr[x]>max2 and arr[x]<max:
			max2 = arr[x]
	return max2

def findLast(arr, n):
	if len(arr) < n:
		return null
	return arr[len(arr)-n]

array2 = [-2,0,2,5,-7,3,-2,4,9]

def NLargest(arr, n):
	if len(arr)<2:
		return null
	max = arr[0]
	for x in range(1, len(arr)):
		if arr[x]>max:
			max = arr[x]
	for j in range(0,n-1):
		max2 = arr[0]
		for x in range(1, len(arr)):
			if arr[x]>max2 and arr[x]<max:
				max2 = arr[x]
				print max, 'newmax'
		max = max2
	return max

def isCreditCardValid(arr):
	last = arr.pop()
	sum = 0
	for x in range(len(arr)-1, -1, -2):
		arr[x] = arr[x] * 2
		if arr[x] > 9:
			arr[x] = arr[x] - 9
	for x in range(0, len(arr)):
		sum += arr[x]
	sum += last
	if sum % 10 == 0:
		return True
	else:
		return False

def shuffle(arr):
	for x in range(1,100):
		a = random.randint(0,len(arr)-1)
		b = random.randint(0,len(arr)-1)
		(arr[a], arr[b]) = (arr[b], arr[a])
	return arr

def removeRange(arr, n, m):
	for x in range (m, n-1, -1):
		removeAt(arr, x)
	return arr

def intermedSums(arr):
	sum = 0
	for x in range(0, len(arr)):
		sum += arr[x]
		if x>0 and x%10==0:
			sum -= arr[x]
			insertAt(arr, x, sum)
			sum = 0 
	if x%10==0:
		return arr
	else:
		arr.append(sum)
		return arr

array = ['kim','george',7,10]

def doubles(arr):
	for x in range(0, len(arr)*2, +2):
		insertAt(arr, x+1, arr[x])
	return arr

def zipit(arr, arr2):
	newarr = []
	if len(arr) > len(arr2):
		long = len(arr)
	else:
		long = len(arr2)
	for x in range(0, long):
		try:
			newarr.append(arr[x])
		except:
			pass
		try:
			newarr.append(arr2[x])
		except:
			pass
	return newarr

'''CHAPTER 4 - STRINGS'''
def removeblanks(str):
	newstr = ''
	letter = str.split(' ')
	for x in letter:
		newstr += x
	return newstr

def getDigits(str):
	num = ''
	dict = {
			'1':'',
			'2':'',
			'3':'',
			'4':'',
			'5':'',
			'6':'',
			'7':'',
			'8':'',
			'9':'',
			'0':'',
			}
	for x in str:
		if x in dict.keys():
			num += x
	return int(num)

def acronyms(str):
	newstr = ''
	if str[0] != ' ':
		newstr += str[0].upper()
	for x in range(1,len(str)):
		if str[x] != ' ' and str[x-1] == ' ':
			newstr += str[x].upper()
	return newstr

def countNonSpace(str):
	count = 0
	for x in str:
		if x != ' ':
			count += 1
	return count

def removeShortString(str, length):
	words = str.split(' ')
	print words
	for x in range(len(words)-1, -1, -1):
		if len(words[x]) < length:
			removeAt(words, x)
	return words

def reversestring(str):
	newstr = ''
	for x in range(len(str)-1, -1, -1):
		newstr += str[x]
	return newstr

array2 = ['Nope!','Its','Kris','starting','with','K!',('instead','of','chris','with','c'),'.']

def removeEven(arr):
	for x in range(len(arr)-1,-1,-1):
		if len(arr[x]) > 1:
			removeEven(arr[x])
		elif len(arr[x]) % 2 == 0:
			removeAt(arr,x)
	return arr

def ParesValid(str):
	count = 0
	for x in (str):
		if x == '(':
			count += 1
		elif x == ')':
			count -= 1
		if count == -1:
			return False
	if count != 0:
		return False
	return True

def BracesValid(str):
	bracesStack = []
	for x in (str):
		if x == '(' or x == '{' or x == '[':
			bracesStack.append(x)
		elif x == ')' or x == '}' or x == ']':
			if x == ')' and bracesStack[len(bracesStack)-1] == '(':
				bracesStack.pop()
			elif x == '}' and bracesStack[len(bracesStack)-1] == '{':
				bracesStack.pop()
			elif x == ']' and bracesStack[len(bracesStack)-1] == '[':
				bracesStack.pop()
			else:
				return False
	if len(bracesStack) == 0:
		return True
	else:
		return False


def isPalendrome(str):
	for x in range(0,len(str)):
		if str[x] != str[len(str)-1-x]:
			return False
	return True

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def createAlphHash(alphabet):
	alphDict = {}
	for x in alphabet:
		alphDict[x]=''
	return alphDict

8925

def isPalenIgnoreSpace(str):
	alphDict = createAlphHash(alphabet)
	str = str.lower()
	str = str.split()
	str = ''.join(str)
	y = len(str)-1
	for x in range(0,len(str)/2):
		while str[y] not in alphDict:
			y -= 1
		if x not in alphDict:
			pass
		if str[x] != str[y]:
			return False
		y -= 1
	return True

def findComplement(num):
        """
        :type num: int
        :rtype: int
        """
        num = str(bin(num))
        newnum = ''
        for x in range(2, len(num)):
            if num[x] == '1':
                newnum += '0'
            else:
                newnum += '1'
        return int(newnum, base=2)


[1,2,2,3,3,4,7,8]

def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dict = {}
    missing = []
    for x in range(1,len(nums)+1):
        dict[x]=False
    for y in (nums):
        if y in dict.keys():
            dict[y]=True
    for key,value in dict.iteritems():
    	if not value:
    		missing.append(key)
    return missing

# print findDisappearedNumbers([1,2,2,3,3,4,7,8])
 # INEFFICIENT
def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in range(len(nums)):
            print i 
            print nums[i]
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
            print nums[index], 'nums'
            print index, 'index'
        print nums
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

# print findDisappearedNumbers([4,3,2,7,8,2,3,1])

# INEFFICIENT
def singleNumber(nums): 
        dict = {}
        for x in range(len(nums)):
            if nums[x] in dict.keys():
                dict[nums[x]]=True
            else:
                dict[nums[x]]=False
        for key,value in dict.iteritems():
            if not value:
                return dict

def singleNumber(nums):
	dict = {}
	for x in range(len(nums)):
		if nums[x] in dict.keys():
			del dict[nums[x]]
		else:
			dict[nums[x]]=False
	for key,value in dict.iteritems():
		return key

# print singleNumber([1])

import timeit

start = timeit.default_timer()
stop = timeit.default_timer()



def constructRectangle(area):
	x = math.ceil(math.sqrt(area))
	while area % x !=0:
		x+=1
	return [int(x),int(area/x)]





def singleNumber2(nums):
    res = 0
    for num in nums:
        res ^= num
        print res
    return res


nums1 = [1,25,3,6,2,5,6,34,63]
nums2 = [1,252,5,6,63,724,2,9,5]
nums1 = set(nums1)
nums2 = set(nums2)
print nums1&nums2