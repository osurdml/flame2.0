import matplotlib.pyplot as plt
import pickle


with open('LearningScore.pkl', 'rb') as input:
    data = pickle.load(input)
print data
y = range(len(data))

plt.plot(data, y)
plt.show()
