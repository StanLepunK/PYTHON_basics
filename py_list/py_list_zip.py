list_a = [1,2,3,4,5,6,7,8,9]
list_b = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
list_mix = zip(list_a,list_b)
print(list_a)
print(list_b)
# converting values to print as set 
list_mix = set(list_mix) #verifier les doublons par exemple
list_mix = sorted(list_mix) 
  
# printing resultant values  
print ("The zipped result is : ",end="") 
print (list_mix) 

