import math

def sigmoid(x):
    return (1/(1+math.exp(-x)))

w  = [0.3, 0.5, 0.4]
b = [0.4, 0.1, 0.9]

i = 2
y = math.sqrt(i)

# I want to train a neural network to calculate square roots
answer = (w[2]*sigmoid(w[1]*sigmoid(w[0]*i+b[0]) + b[1]) + b[2])*i

print(y, answer)