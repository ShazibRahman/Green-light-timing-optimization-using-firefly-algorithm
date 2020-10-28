import random
import math
import numpy as np

import matplotlib.pyplot as plt


class FireflyAlgorithm():

    def __init__(self, D, NP, nFES, alpha, betamin, gamma, LB, UB, function,data_set):
        self.D = D  # dimension of the problem
        self.NP = NP  # population size
        self.nFES = nFES  # number of function evaluations
        self.alpha = alpha  # alpha parameter
        self.betamin = betamin  # beta parameter
        self.gamma = gamma  # gamma parameter
        self.data_set=data_set
        # sort of fireflies according to fitness value
        self.Index = [0] * self.NP
        self.Fireflies = self.data_set.copy()# firefly agents
        self.Fireflies_tmp =self.data_set.copy()  # intermediate pop
        self.Fitness = [0.0] * self.NP  # fitness values
        self.I = [0.0] * self.NP  # light intensity
        self.nbest = [0.0] * self.NP  # the best solution found so far
        self.LB = LB  # lower bound
        self.UB = UB  # upper bound
        self.fbest = None  # the best
        self.evaluations = 0
        self.Fun = function
        self.time_gain=0
    def plot(self,x,y):

        plt.scatter(x,y)
        plt.show()

    def init_ffa(self):
        for i in range(self.NP):
            for j in range(self.D):
                self.Fireflies[i][j] = random.uniform(
                    20, 50) +self.Fireflies[i][j] # adding noise of 20-30 for better movement and hence better Solution
            self.Fitness[i]=random.uniform(30,60)

            self.I[i] = self.Fitness[i]

    def alpha_new(self, a):
        delta = 1.0 - math.pow((math.pow(10.0, -4.0) / 0.9), 1.0 / float(a))
        return (1 - delta) * self.alpha

    def sort_ffa(self):  # implementation of bubble sort
        for i in range(self.NP):
            self.Index[i] = i

        for i in range(0, (self.NP - 1)):
            j = i + 1
            for j in range(j, self.NP):
                if (self.I[i] > self.I[j]):
                    z = self.I[i]  # exchange attractiveness
                    self.I[i] = self.I[j]
                    self.I[j] = z
                    z = self.Fitness[i]  # exchange fitness
                    self.Fitness[i] = self.Fitness[j]
                    self.Fitness[j] = z
                    z = self.Index[i]  # exchange indexes
                    self.Index[i] = self.Index[j]
                    self.Index[j] = z



    def replace_ffa(self):  # replace the old population according to the new Index values
        # copy original population to a temporary area
        for i in range(self.NP):
            for j in range(self.D):
                self.Fireflies_tmp[i][j] = self.Fireflies[i][j]

        # generational selection in the sense of an EA
        for i in range(self.NP):
            for j in range(self.D):
                self.Fireflies[i][j] = self.Fireflies_tmp[self.Index[i]][j]

    def FindLimits(self, k):
        for i in range(self.D):
            if self.Fireflies[k][i] < self.LB:
                self.Fireflies[k][i] = self.LB
            if self.Fireflies[k][i] > self.UB:
                self.Fireflies[k][i] = self.UB

    def move_ffa(self):
        for i in range(self.NP):
            scale = abs(self.UB - self.LB)
            for j in range(self.NP):
                r = 0.0
                for k in range(self.D):
                    r += (self.Fireflies[i][k] - self.Fireflies[j][k]) * \
                        (self.Fireflies[i][k] - self.Fireflies[j][k])
                r = math.sqrt(r)
                if self.I[i] > self.I[j]:  # brighter and more attractive
                    beta0 = 1.0
                    beta = (beta0 - self.betamin) * \
                        math.exp(-self.gamma * math.pow(r, 2.0)) + self.betamin
                    for k in range(self.D):
                        r = random.uniform(0, 1)
                        tmpf = self.alpha * (r - 0.5) * scale
                        self.Fireflies[i][k] = self.Fireflies[i][
                            k] * (1.0 - beta) + self.Fireflies_tmp[j][k] * beta + tmpf
            self.FindLimits(i)

    def Run(self):
        
       
        self.init_ffa()

        while self.evaluations < self.nFES:

            # optional reducing of alpha
            self.alpha = self.alpha_new(self.nFES/self.NP)

            # evaluate new solutions
            for i in range(self.NP):
                self.Fitness[i] = self.Fun(self.D, self.Fireflies[i])
                self.evaluations = self.evaluations + 1
                self.I[i] = self.Fitness[i]

            # ranking fireflies by their light intensity
            self.sort_ffa()
            # replace old population
            self.replace_ffa()
            # find the current best
            self.fbest = self.I[0]
            self.bestI=np.argmax(self.I)
            self.nbest=self.Fireflies[self.bestI]

            # move all fireflies to the better locations
            self.move_ffa()


        return  self.nbest, self.fbest
