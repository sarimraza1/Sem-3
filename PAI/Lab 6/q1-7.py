import numpy as np


# Question 1


data = np.array([
    [60, 70, 80, 50, 90],
    [45, 55, 65, 75, 85],
    [80, 90, 70, 60, 75],
    [30, 40, 50, 45, 35],
    [90, 85, 95, 80, 90],
    [55, 60, 65, 70, 75],
    [40, 50, 45, 55, 60],
    [75, 80, 85, 90, 95],
    [65, 70, 60, 75, 80],
    [50, 55, 60, 65, 70]
])

total = np.sum(data, axis=1)
average = np.mean(data, axis=1)

subject_average = np.mean(data, axis=0)

highest = np.argmax(average) + 1

passed = np.sum(average >= 50)

result = np.where(average >= 50, "Pass", "Fail")

print("Student Totals:", total)
print("Student Averages:", average)
print("Subject Averages:", subject_average)
print("Highest Average: Student", highest)
print("Students Passed:", passed)
print("Pass/Fail:", result)




# Quesiton 2


data = np.array([
    [20,  5, 100, 0.5],
    [25,  7, 120, 0.7],
    [30,  6, 110, 0.6],
    [35,  8, 130, 0.8],
    [40, 10, 150, 1.0],
    [45,  9, 140, 0.9],
    [50, 11, 160, 1.1],
    [55, 13, 170, 1.3],
    [60, 12, 180, 1.2],
    [65, 14, 190, 1.4]
])

feature_avg= np.mean(data,axis=0)
feature_std= np.std(data,axis=0)

print(feature_avg)
print(feature_std)

standardized_data = (data - feature_avg) / feature_std

print(standardized_data)
print("\nNew Means:")
print(np.mean(standardized_data, axis=0))

print("\nNew Standard Deviations:")
print(np.std(standardized_data, axis=0))




# Question 3


image = np.array([
    [0,   50,  100, 150, 200],
    [25,  75,  125, 175, 225],
    [10,  60,  110, 160, 210],
    [40,  90,  140, 190, 240],
    [15,  80,  130, 180, 255]
])

print(image)
print(f"Min Intensity = {np.min(image)}\nMax Intensity = {np.max(image)}\nMean Intensity = {np.mean(image)}")

mask= np.where(image>=100, 1,0) 

print(f"Binary Mask =  {mask}")
t_image = np.where(image >= 100, image, 0)

print("Thresholded Image:")
print(t_image)




# Question 4



data = np.array([
    [22, 45, 31, 28, 50],   
    [30, 42, 35, 33, 48],   
    [18, 25, 22, 27, 30],   
    [55, 60, 58, 62, 65]    
])

sensor_mean =np.mean(data,axis=1)
print(f"Per Sensor Mean = {sensor_mean}")
print(f"Per Sensor Min = {np.min(data,axis=1)}")
print(f"Per Sensor Max = {np.max(data,axis=1)}")
print(f"Per Sensor Std = {np.std(data,axis=1)}")

high_avgreading= np.max(sensor_mean)
highest_sensor = np.argmax(sensor_mean)
print(f"Sensor with Highest Avg Reading is Sensor {highest_sensor+1} with {high_avgreading}")

threshold= 30

readings = np.where(data>threshold,1,0)
print(readings)



# Question 5


matA = np.array([
    [11, 22, 31],
    [14, 25, 19],
    [7, 18, 15]
])

matB = np.array([
    [9, 21, 11],
    [26, 13, 17],
    [1, 7, 2]
])

matC = np.array([
    [5, 10],
    [15, 20],
    [25, 30]
])

print("Shape of A:", matA.shape)
print("Shape of B:", matB.shape)
print("Shape of C:", matC.shape)

print("\nA + B:")
print(matA + matB)

print("\nA - B:")
print(matA - matB)

print("\nA * B:")
print(matA * matB)

print("\nA @ B:")
print(matA @ matB)

print("\nA @ C:")
print(matA @ matC)

print("\nTranspose of A:")
print(matA.T)

print("\nTranspose of C:")
print(matC.T)

print("\nDeterminant of A:")
print(np.linalg.det(matA))

print("\nDeterminant of B:")
print(np.linalg.det(matB))

print("\nInverse of A:")
print(np.linalg.inv(matA))

print("\nInverse of B:")
print(np.linalg.inv(matB))

# +, -, * require compatible dimensions
# @ requires columns of A = rows of B
# det and inverse require square matrix



# Question 6


rng = np.random.default_rng(42)
data = rng.normal(100, 15, 1000)

mean = np.mean(data)
std = np.std(data)

print("Mean =", mean)
print("Median =", np.median(data))
print("Std =", std)
print("Min =", np.min(data))
print("Max =", np.max(data))

print("Percentage inside 1 std =",
      np.mean((data >= mean - std) & (data <= mean + std)) * 100)


rng = np.random.default_rng(100)
data = rng.normal(100, 15, 1000)

mean = np.mean(data)
std = np.std(data)

print("\nSecond Seed")
print("Mean =", mean)
print("Median =", np.median(data))
print("Std =", std)
print("Min =", np.min(data))
print("Max =", np.max(data))

print("Percentage inside 1 std =",
      np.mean((data >= mean - std) & (data <= mean + std)) * 100)




# Question 7


data = np.array([10, 20, np.nan, 40, 50, np.nan, 70])

print("NaN values:", np.isnan(data))

print("Mean:", np.nanmean(data))
print("Min:", np.nanmin(data))
print("Max:", np.nanmax(data))

mean = np.nanmean(data)
data[np.isnan(data)] = mean

print("After replacing NaN:", data)
print("NaN remaining:", np.isnan(data).any())