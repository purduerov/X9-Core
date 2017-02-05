import math as np


class Convolution(object):

    @staticmethod
    def convolve(signal, signalLen, kernel, kernelLen, result):
        for n in range(0, signalLen + kernelLen - 1):
            result[n] = 0
            if n >= kernelLen - 1:
                kmin = n - (kernelLen - 1)
            else:
                kmin = 0
            if n < signalLen - 1:
                kmax = n
            else:
                kmax = signalLen - 1
            for k in range(kmin, kmax + 1):
                result[n] += signal[k] * kernel[n - k]


    @staticmethod
    def printSignal(name, signal, signalLen):
        for i in range(0, signalLen):
            print "%s[%d] = %f" % (name, i, signal[i])
        print

    @staticmethod
    def angle(time1, time2, d, v):
        angle = np.arccos(((time1 + time2) * (time2 - time1) * v + (d ** 2)) / (2 * time2 * d)) * 180 * 7 / 22
        return angle

if __name__ == "__main__":
    DISTANCE = 0.5
    VELOCITY = 50.45
    signal1 = [1, 1, 1, 1, 1]
    signal2 = [0, 1, 1, 1, 0]
    signal3 = [1, 1, 1, 1, 1]
    signal4 = [1, 1, 1, 1, 1]
    kernel = [1, 1, 1, 1, 1]
    signalReceive = True
    t = 0
    while 0 <= t <= 2:
        if signalReceive:
            result1 = [None] * (len(signal1) + len(kernel) - 1)
            result2 = [None] * (len(signal2) + len(kernel) - 1)
            result3 = [None] * (len(signal3) + len(kernel) - 1)
            result4 = [None] * (len(signal4) + len(kernel) - 1)

            Convolution.convolve(signal1, len(signal1), kernel, len(kernel), result1)
            Convolution.convolve(signal2, len(signal2), kernel, len(kernel), result2)
            Convolution.convolve(signal3, len(signal3), kernel, len(kernel), result3)
            Convolution.convolve(signal4, len(signal4), kernel, len(kernel), result4)

            Convolution.printSignal("result1", result1, len(result1))
            Convolution.printSignal("result2", result2, len(result2))
            Convolution.printSignal("result3", result3, len(result3))
            Convolution.printSignal("result4", result4, len(result4))

            t1 = 0.0
            t2 = 0.12
            t3 = 0.083
            t4 = 0.02

            delta_t2 = t2 - t1
            delta_t3 = t3 - t1
            delta_t4 = t4 - t1

            angleY = Convolution.angle(delta_t3, delta_t4, DISTANCE, VELOCITY)
            angleX = Convolution.angle(delta_t2, delta_t3, DISTANCE, VELOCITY)

            print "%f" % angleX
            print "%f" % angleY
        t += 0.1

