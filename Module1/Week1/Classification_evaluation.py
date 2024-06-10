import math
def cal_f1_score(tp,fp,fn):
    #Helper function to validate tp, fp and fn
    def validate_parameter(param,name):
        if not isinstance(param,int):
            print(f"{name} must be an integer value!")
            return False
        elif param <= 0:
            print(f"tp and fp and fn all must be greater than zero!")
            return False
        return True
    
    #Validate each parameter:
    if not validate_parameter(tp,'tp'):
        return
    if not validate_parameter(tp,'fp'):
        return
    if not validate_parameter(tp,'fn'):
        return
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = (precision * recall) / (precision + recall)

    print(" Precision is ",precision)
    print(" Recall is ", recall)
    print(" F1 Score is ",f1_score)
    return f1_score
    





    