import math
import statistics

# Step ii: Create a data dictionary for counties and their GCP
counties_gcp = {
    "Nairobi": 3379354,
    "Kiambu": 721205,
    "Nakuru": 600518,
    "Mombasa": 564147,
    "Meru": 407419,
    "Machakos": 378446,
    "Kisumu": 312651,
    "Uasin Gishu": 295698,
    "Kakamega": 276484,
}

# Step iii: Display the top 10 counties with the highest GCP (counties only)
top_10_counties = sorted(counties_gcp, key=counties_gcp.get)
print("Top 10 Counties by GCP:", top_10_counties)

# Step iv: Display the GCP for each county in the table
print("\nGCP of Each County:")
for county, gcp in counties_gcp.items():
    print(f"{county}: {gcp}")

# Step v: List the county with the minimum and maximum GCP
min_county = min(counties_gcp, key=counties_gcp.get)
max_county = max(counties_gcp, key=counties_gcp.get)
print("\nCounty with Minimum GCP:", min_county, "GCP:", counties_gcp[min_county])
print("County with Maximum GCP:", max_county, "GCP:", counties_gcp[max_county])

# Step vi: Calculate the average GCP for the first 10 counties
average_gcp = statistics.mean(counties_gcp.values())
print("\nAverage GCP for the First 10 Counties:", average_gcp)

# Step vii: Calculate the total GCP for all counties combined
total_gcp = sum(counties_gcp.values())
print("Total GCP for All Counties Combined:", total_gcp)