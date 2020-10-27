from FireflyAlgorithm import *


def function(D, sol):
    val = 0.0
    for i in range(D):
        val = val + sol[i] * sol[i]
    return val



Algorithm = FireflyAlgorithm(10, 10, 100, 0.5, 0.2, 1.0,120, 180, function)
Best = Algorithm.Run()

print ('best solution is',Best[0], 'and time gained',round(Best[1]),'mins')
