import math
import statistics
results={'SMA 2104': 69 ,
         'SDS 2101': 70 ,
         'SDS 2102': 65 ,
         'SDS 2103': 62 ,
         'SDS 2104': 55 ,
         'SDS 2105': 63}
for x in results.keys():
    print (x)

for x in results.values():
    print (x)

for x in results.items():
    print (x)

total=sum(results.values())
print(total)

average=statistics.mean(results.values())
print(average)

med=statistics.median(results.values())
print(med) 

var=statistics.variance(results.values())
print(var)

deviation=statistics.stdev(results.values())
print(deviation)



