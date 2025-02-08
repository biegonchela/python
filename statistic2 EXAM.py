import statistics
import math
dict={2021:3.9,
      2022:6.5,
      2023:5.5,
      2024:4.3}
print("Unemployment in Kenya between the years 2021 to 2024")
print(".........................................................................")

for x,y in dict.items():
    print(f"Year{x} : {y}")

total=sum(dict.values())
print(f"The total unemployment rate in Kenya is: {total}")

average=statistics.mean(dict.values())
print(f"The average unemployment rate in Kenya is: {average}")

med=statistics.median(dict.values())
print(f"The median score is: {med}")

mode=statistics.mode(dict.values())
print(f"The mode score is: {mode}")

stdev=statistics.stdev(dict.values())
print(f"The standard deviation  is: {stdev}")

var=statistics.variance(dict.values())
print(f"The variance score is: {var}")