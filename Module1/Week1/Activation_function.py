import math
def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True

def sigmoid(x):
    return (1/(1+math.exp(-x)))
    
def relu(x):
    if x > 0:
        return x
    else:
        return 0
        
def elu(x):
    if x > 0:
        return x
    else:
        return 0.01 * (math.exp(x) - 1)

value = input("x = ")
activation = input("Activation Function ( sigmoid | relu |elu ): ")

if is_number(value):
    value = float(value)
    if activation == 'sigmoid':
        f = sigmoid(value)
        print(f"Simoid({value}) = {f}")
    elif activation == 'elu':
        f = elu(value)
        print(f"Elu({value}) = {f}")
    elif activation == 'relu':
        f = relu(value)
        print(f"Relu({value}) = {f}")
    else:
        print(f"{activation} is not supported!")
else:
    print("x must be a number!")

