# Python-lambda-filter-map-reduce
If you have trouble understanding or implementing lambda,filter,map or reduce. Do checkout this repository.<br>
### 1.lambda functions - Also known as Anonymous function or function without a name.These function are return type functions.<br>
                     They can be vey useful for writing short codes
<br>
#### 2.filter function - filter functions are used to filter out elements from an iterable for which the applied function returns True<br>
Filter takes two arguments: 1st is a Function & 2nd an iterable<br>
<br>
### 3.map function - map function is similar to filter function but can be used in case of multiple lists. if the lists are of same length<br>
<br>
### 4.reduce function - reduce function reduces a sequence of element to a single valueby processing the elements.<br>
<br>
<br>
WORKING OF MAP FUNCTION<br>
first let us understand the working of inner code then move to outer part<br>
inside map we pass a function in this case we have used a lambda function<br>
 then we have passed two lists<br>
Now map will, one by one maps the lambda function to each element of the list<br>
first 1 and 11 will be supplied from both lists to lambda arguments x and y and their sum is returned<br>
then 2 and 12 will be supplied from both lists to lambda arguments x and y and their sum is returned<br>
and that is how all the elements are added<br>
finally we get a list of sum of the corresponding elements of the two lists<br>
<br>
<br>
WRKING OF REDUCE:<br>
reduce takes two arguments a function and an iterable<br>
<br>
lst = [1,2,3,4,5]<br>
a = reduce(lambda a,b:a*b,lst)<br>
<br>
Now, 1 and 2 are passed to lambda function it return 1*2<br>
which is 2.<br>
Now the above result(i.e. 2) is passed as 'a' and next element(i.e. 3) as 'b' to lambda function<br>
and it returns 2*3 which is 6<br>
Again 6 is passed as 'a' and next element from list is passed as 'b' and their product is calculated.<br>
<br>
this process goes on & on until whole list is converted inot a single number in this case product of all the elements(i.e. 1*2*3*4*5) = 120<br>
