import time

def absTime():
    return time.time()

def TimeStep(prevTime, newTime):
    return newTime-prevTime