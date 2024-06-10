import math
import random
def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True

def samples_init(n):
    targets = []
    predicts = []
    for i in range(n):
        predicts.append(random.uniform(0.0,10.0))
        targets.append(random.uniform(0.0,10.0))
    return targets, predicts


def mae(n):
    
    targets, predicts = samples_init(n)
    result = 0.0
    for i in range(n):
        result = result + abs(targets[i] - predicts[i])
    loss = result / n
    return loss, targets, predicts

    
def mse(n):
    targets, predicts = samples_init(n)
    result = 0.0
    for i in range(n):
        result = result + (targets[i] - predicts[i]) ** 2
    loss = result / n
    return loss, targets, predicts
        
def rmse(n):
    result, targets, predicts = mse(n)
    loss = math.sqrt(result)
    return loss, targets, predicts

no_sample = input("Input number of samples (integer number) to be generated: ")
loss_name = input("Name of Loss-Function( MAE | MSE | RMSE ): ")

if no_sample.isnumeric():
    no_sample = int(no_sample)
    if loss_name == "MAE":
        loss, targets, predicts = mae(no_sample)
        for i in range(no_sample):
            print(f"Loss function: {loss_name}, sample: {i+1}, pred: {predicts[i]}, target: {targets[i]}, loss = {abs(predicts[i] - targets[i])}")
            print(f"Final MAE = {loss}")        
    elif loss_name == "MSE":
        loss, targets, predicts = mse(no_sample)
        for i in range(no_sample):
            print(f"Loss function: {loss_name}, sample: {i+1}, pred: {predicts[i]}, target: {targets[i]}, loss = {abs(predicts[i] - targets[i])}")
            print(f"Final MSE = {loss}")   
    elif loss_name == "RMSE":
        loss, targets, predicts = rmse(no_sample)
        for i in range(no_sample):
            print(f"Loss function: {loss_name}, sample: {i+1}, pred: {predicts[i]}, target: {targets[i]}, loss = {abs(predicts[i] - targets[i])}")
            print(f"Final RMSE = {loss}")   
    else:
        print("Invalid loss function!")

else:
    print("n must be an integer number!")


        