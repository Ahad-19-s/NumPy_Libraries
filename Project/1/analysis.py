import numpy as np
data = np.genfromtxt(
    r"D:\1986\NumPy\Project\1\data.csv",
    delimiter=',',
    skip_header=1
)


print ("original data :")
print(data)

print( "\n Missing values (NaN) :")
print(np.isnan(data))


clean_data = np.nan_to_num(data)
print("\n cleaned data :")

print(data)

marks =clean_data[:,-1:]

print("Marks Array:")
print(marks)
print("Shape:", marks.shape)



# statstical analysis


print("\n Avarage marks per student :")
print(np.mean(marks,axis=1))

print("\n Avarage marks per subject :")
print(np.mean(marks,axis=0))

print("\n All sub highest marks")
print(np.max(marks))

print("\n All sub lowest marks")
print(np.min(marks))

print("\n Failed stduent marks :")
failed_student= np.where(marks<50)
print(failed_student)
