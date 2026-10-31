x_inputs = [0.53, 0.38, 0.67]
w_weights = [0.2, 0.5, 0.7]
bias = 0.6

def step(weighted_sum):
    return 1 if weighted_sum > 0 else 0

def perceptron():
    weighted_sum = 0
    for x,w in zip(x_inputs, w_weights):
        weighted_sum += x*w
        print(weighted_sum)
    weighted_sum += bias
    return step(weighted_sum)
print(perceptron())
print(list(zip(x_inputs, w_weights)))