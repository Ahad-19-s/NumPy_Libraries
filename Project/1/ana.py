import numpy as np
import matplotlib.pyplot as plt

# Load CSV
data = np.genfromtxt(
    r"D:\1986\NumPy\Project\1\data.csv",
    delimiter=",",
    skip_header=1
)

roll = data[:, 0].astype(int)
marks = data[:, 1:]

# Student-wise average (ignore NaN)
student_avg = np.nanmean(marks, axis=1)

# 🔹 Graph: Bar Chart
plt.figure()
plt.bar(roll, student_avg)

plt.xlabel("Student Roll")
plt.ylabel("Average Marks")
plt.title("Average Marks per Student")

plt.show()
subject_avg = np.nanmean(marks, axis=0)
subjects = ["Math", "Physics", "Chemistry"]

plt.figure()
plt.bar(subjects, subject_avg)
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Subject-wise Average Marks")
plt.show()
