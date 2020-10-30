<div style="text-align: center; font-family:Georgia;">

### CONTRIBUTORS

</div>



---


|[Shazib Rahman   ](https://github.com/shazx06)|
|:-------------:|
|<img src="https://avatars0.githubusercontent.com/u/45175156?s=400&v=4" alt="drawing"  width="152"> |
|commits __43__|

---
<div style="font-family:Georgia">


# Project Title - optimization of green signal timings of traffic light controllers using firefly algorithms

<br>



## Abstract

Traffic lights are source of signalling device for road junctions. Traffic light controllers are programmed to assign timely directions to road users in Red, Yellow and Green. Present Traffic Light Controllers are based on microcontroller.TLC have limitations as it uses pre-defined hardware, which functions according to program that does not have flexibility of modification on real time basis. As the numbers of road users’ increases, resources provided by current infrastructures are limited, thus control of traffic becomes very important. To mange traffic flow, introduction of new technique ‘Dynamic Traffic Signal Controller’ emerged. Thus, optimization of traffic light switching; controls road capacity traffic flow and prevent congestions. The unique aspect is that web application is provided over mobile phones to road users who wish to access the traffic management application for traffic news. The application displays the traffic status. The proposed system has simple architecture, ease of implementation and user friendliness.

## 1.Introduction

Presently, modern lifestyle consists of fast and rapid transport mediums which play a vital role in economic development for any nation. All developed nations have well developed transportations system with efficient traffic control on road, rail and air. Transportation of goods, industrial products, manpower and machinery are the key factors which influence the industrial development of any country. Also, the drastic/rigorous changing condition of road traffic is rising as a serious problem for people to move, infrastructure wise and as nation’s economic point of view. Hence traffic congestion leads to long waiting hours along with fuel and money wastage. So, the Traffic management on road is crucial to reduce these problems. Now, control and management of city traffic has become a major problem in many countries even though Regional Traffic Office has found solutions to overcome these traffic issues. One way to improve traffic flow and safety of current transport system is to apply automation and intelligent control methods to road infrastructure . Also, measures like new roads, flyovers, ring roads, city trains are applicable for traffic management. But as the number of road users increase and resources provide by current infrastructures are limited dynamic control of traffic is need of hour.

## Traffic Jams Everywhere

Under ordinary conditions when the traffic lanewaits for the green light, time setting is same and fixed.With increasing number of vehicles on roads has  substantially increases congestion. This is observedusually at main junctions in morning, office hours andafter office hours. Hence the main effect of this increases the waiting time of people on road. Thus a solution for this matter can be given by different delays to traffic lanes which is called as normal mode operation.

## Have To Wait , Even Where Is No Traffic

At certain junctions even if there is no traffic when the traffic light remains red the road users have to wait until the light turns green. And if rule is broken fine has to be paid .The solution of this problem is by developing the system which detects traffic density on each road and then sets signal timing accordingly along with synchronization of the adjacent junction’s traffic signal.

## During Emergency
During traffic jam an emergency vehicle like ambulance, fire brigade, police are stuck and have to wait for the traffic light to turn green. Hence this critical problem may further complicate that costs human life. So solution to this problem can be given by having priority for emergency vehicle to flow rapidly through the traffic while other vehicles are instructed to be still (i.e. traffic signal light is red).

## Limited Traffic Information To Drivers
Present conventional traffic system fails to provide traffic status about congested roads,alternate routes etc. A remedy for this issue is to design a user web application to road users who shall access the URL of he web application.

The dynamic traffic signal controller is introduced in this project with efficient functions and hardware interface. The traffic jam will be reduced by increasing green signal time for busy lanes and decreasing red signal time for non busy roads. In other words dynamic signal switching can be achieved by when vehicle density of the four way junction road is known. Secondly, traffic news is provided through the website design for users ease. Therefore, improvement of town traffic condition is largely dependent on the modern ways of traffic management and control. Advanced traffic signal controllers and control system contribute to the improvement of the traffic problem.

## 2. Survey
Nowadays, vehicles on road are increasing each day like growing cities of this world. Traffic Management on road has become the need of hour in today’s urban lifestyle. Efficient techniques are needed to reduce travel time, usage of money, fuel and waiting hours along with gamut of other problems too. Thus need arises for simulating and optimizing current system for the traffic controllers to better accommodate this increasing demand by road users around the world.Traffic lights are commonly used devices to regulate roadway intersection traffic with a view to both safety and smoothness of vehicle flow, for generations where it is still considered the best practices . Various methods and approaches are suggested in literature for solving the traffic control problem. It includes rule based learning to the modern fuzzy and neural network approaches. In this section, the various solutions to the traffic control problems suggested in the literature are discussed, along with their merits and demerits.

Since the traffic light was invented ages ago, there have been significant revolutions lined down in various aspects about same. The most common revelation which we can visualize is the displays of traffic light itself. The other revolution which is being enhanced and improved is the traffic light controllers.

 ## 3. Proposed Model
The primary objective of this project is to design a  program and implement hardware for dynamic traffic light control system that is suitable for real life implementations. The project implementation also aims to have efficient and safe traffic flow control along with reduced waiting time at signal junction, priority for emergency case, heavy traffic jams and provision of information to road users instantly.The traffic jam will be reduced by increasing the green signal time on busy road and decreasing the red signal time on non busy road. Infra Red-Light Emitting Diode (IR-LED) transmittor and receivers are used to measure the traffic flow in real time (like no of cars, buses etc) their speed and their Density. This Data is very useful when It comes to firefly Algorithm to work because firefly algorithm works on the Parameter of brightness. Which in this case is the type of vehicle (biggger the vehicle greater the brightness and vice versa).
And the distance between vehicles is Used as distance between the fireflies.
The Infrared Sensors mounted on road to detect above explained parameters. The presence of a Vehicle is sensed and recorded as an imput for the firefly algorithm. The input signal indicates the densitty of vehicles on each road. In This type of system the basic operations are implemented by Alog.
<br>

<b>

```
    Begin
     1.Objective function: f ( x ) , x = ( x 1 , x 2 , . . . , x d ));
     2.Generate an initial population of fireflies x i ( i = 1 , 2 , … , n ) ;.
     3.Formulate light intensity I so that it is associated with f ( x )
     4.Define absorption coefficient γ

    While (t < MaxGeneration)
        for i = 1 : n (all n fireflies)
            for j = 1 : i (n fireflies)
                if ( I>J),
                    Vary attractiveness with distance r via e**( -Yr)
                    Evaluate new solutions and update light intensity;
                end if
            end for j
        end for i
        Rank fireflies and find the current best;
    end while

    Post-processing the results and visualization;

 end
```

</b>

<br>

_**Firefly algorithm**_<br>
Firefly algorithm (FA) is a simple yet quite efficient nature-inspired search technique for global optimization. Since FA was developed, it has attracted a lot of attentions and becomes more popular in solving various real-world problems. FA is a swarm-based intelligence algorithm, which mimics the flashing behavior of fireflies . A firefly flashes as a signal to attract others for some purposes, e.g. predation or mating. Accordingly, this biological phenomenon is formulated as a meta-heuristic algorithm depending on following three rules :
  - All fireflies are attracted by each other without respect to their sex;
  - Attractiveness is proportional to its brightness, that is, the less bright one will move towards the brighter one;
  - If there are no brighter fireflies than a particular firefly, it will move randomly in the space.

In FA, the distance between any teo fireflies x<sub>i</sub>,x<sub>j</sub>, respectively, can be defined as the Euclidean  Distance r<sub>ij</sub> whic is formulted as follows,<br>

![logo](https://github.com/shazx06/DataSets/blob/master/1.jpg) (1)<br>
where _D_ is the dimension of an optimization problem.
<br>
Indeed, the larger the distance r<sub>ij</sub> is , the less the light fireflies can see from each other .Accordingly, it is necessary to define monotonically decreasing functions for the light intensity and attractiveness , respectively. they are presented in Eqs (2) and (3).<br>

![logo2](https://github.com/shazx06/DataSets/blob/master/2.jpg)   (2)<br>
Where _I_<sub>o</sub> is initial light intensity, and _Y_ is the light absorption coefficient, which controls the decrease of light intensity. Accordingly, the attractiveness _B_ of a firefly is defined as shown in EQ (3)<br>
![image3](https://github.com/shazx06/DataSets/blob/master/3.jpg)   (3)<br>

where _B_<sub>o</sub> is a constant , which is the Attractiveness at r=0. the step of a firefly _i_ is attracted to move another more attractive firefly _j_ is determined by<br>

![image2](https://github.com/shazx06/DataSets/blob/master/4.jpg)  (4) <br>

where **c** is a constant vector _[0.5,0.5,0.5,,,,]_<sup>D</sup> and _t_ is the time step, __e__<sup>t</sup> is drawn from a normal distribution <sup> _N(0,1)_</sup>. __deltaX__ is the step size of the _i_ th firefly moving. the first term is the attraction from _j_ th fireflyh , while the second term is randomization controlled by __x__,  which is a const. in the range _(0,1)_ .Therefor, the update of the _ith_ firefly is formed as follows <br>

![i](https://github.com/shazx06/DataSets/blob/master/5.jpg)   (5)<br>

the equation (4) and (5) show that the _ith_ firefly will move towards the _jth_ firefly , which is a more atractive one.
<br>




**Global best** Fitness is the maximum of the Local Best Fitness and also here we store the value of maximum element as global best fitness index.
**Global best Position** is nothing its just the corresponding value from current position at index equal to global best fitness index.
<div style="text-align:center" markdown="1">

![flowchart](https://github.com/shazx06/DataSets/blob/master/6.png)






![graph](https://github.com/shazx06/DataSets/blob/master/Figure_2.png)

<br>




Fireflies tend to move close to each other after every Generation and hence gives the optimized result.

![lane](https://github.com/shazx06/DataSets/blob/master/lane2.png)
<br>
The above Graph represents the optimized minutes of green light for a Traffic light 
according to its density of vehicles, their speed and the distance in between them.



**Fiteness function** used here is called sphere which is follows:

<br>



```python
def function(D, sol):
    val = 0.0
    for i in range(D):
        val = val + sol[i] * sol[i]
    return val
```


<br>

</div>







## 4. Conclusion
The optimization of city traffic scenario is an important issue to be considered. Hence modern techniques of traffic management contribute to optimization of traffic problem. The dynamic traffic signal controller is introduced in this project having specific functions along with hardware interface. The first part is designing of program which consists of data collection, sorting  and therefore automatic evaluation of signal time. After that the second part is optimizong algortihm which is designed to provide traffic alerts for road users and take measures to avoid delay. So problems such as wastage of fuel, emergency case could be overcome through this proposed system. This system aims at saving a large amount of waiting hours caused by traffic deadlocks, where control can save time and property.

<br>

---

## Reference Papers:

I. Fister Jr.,  X.-S. Yang,  I. Fister, J. Brest. [Memetic firefly algorithm for combinatorial optimization](http://www.iztok-jr-fister.eu/static/publications/44.pdf) in Bioinspired Optimization Methods and their Applications (BIOMA 2012), B. Filipic and J.Silc, Eds.
Jozef Stefan Institute, Ljubljana, Slovenia, 2012

I. Fister, I. Fister Jr.,  X.-S. Yang, J. Brest. [A comprehensive review of firefly algorithms](http://www.iztok-jr-fister.eu/static/publications/23.pdf). Swarm and Evolutionary Computation 13 (2013): 34-46.
</div>

---