I gathered in this repository the solutions to some well-know problems in algorithmic. I got the opportunity to read about them and whereby I attempted to solve them while I was strengthening my knowledge in algorithmic and data structure. I put below the key ideas I have learned throughout my journey of learning.

In algorithmic, there are three famous approaches used for solving problems. I mean here by approach some sort of methodology that ones apply to solve a particular problem.

# Greedy algorithm
The first one, and the easiest to apply is "Greedy algorithm".
It consists of splitting a given problem into a sequence of stages wherein each stage we have a set of available actions and we have to select the optimal among them. Let's consider the following example to illustrate this approach. We want a plane to flow from an airport A to an airport B. The plane can only travel a certain distance at full-tank which might be less than the distance between the two airports. Fortunately, between A and B, there are airports, that we know previously their location, where the plane can land to refill its tank. We can not choose arbitrarily the number of stops since each one would cost not only time but also money. Therefore, the challenge is to find the minimum number of stops to refill the tank in the travel from A to B. 
In this case, our stages are airports. In each one, we have to choose between two actions whether to stop or not. The criterion on which we would determine the optimality of the decision is whether, at a given airport, the remaining fuel in the tank would be sufficient to travel to the next airport. If so, then we do not stop and continue to the next airport. If the answer is no then we stop to refill.

# Divide and conquer
The second approach is "Divide and conquer". The idea behind this approach is: given a problem, we subdivide it into smaller disjoint ones that have the same nature as the primary one. Then, we solve the small problems and combine their results to find a solution to the primary problem. This approach might seem abstract. Hence, let us consider the following example: Given a sorted list of numbers (let's say in increasing order), we want to find the index of a target number. How can we do that while avoiding going throughout all the elements of the list and comparing each time the current number with our target? In practice, the latter approach turns out to be very slow. The fact of the list being sorted will be helpful in that case. Indeed, we can check the element in the middle and see whether it is greater or less than our target number. if it turns out to be greater than the target then no need to search on the right side of the current number as we already know that all the elements located there would greater than it. Therefore, we will focus our search only on the left side. If the result of the comparison was the opposite we make the opposite of what was said. We apply the same reasoning to the remaining elements until we find the target number. 
To summarize this reasoning, each time we divide the list of numbers into two halves and then focus the research on one of them depending on the result of the comparison between the number in the middle and our target. Notice here that the resulting lists of numbers are smaller disjointed instances of the same nature of the problem.

# Dynamic programming
The last approach, but not least, is called "Dynamic programming". The key idea of dynamic programming is to split a problem into a sequence of related stages wherein each stage we have to take an optimal decision among multiple ones. Dynamic programming may seem like "Greedy algorithm". Yet, the key difference is that in Dynamic programming the optimal decision taken in each stage considers the previous decisions. In "Greedy algorithm", the optimal decision taken does not rely on past decisions. It only cares about the current stage.
A very famous example that can be solved using dynamic programming and where a Greedy strategy gives a false solution is the "knapsack problem". The latter can be stated as follow: Imagine a thief entered a room bank full of gold bars that have different weights. Unfortunately, the thief can not bring with him all the gold bars as he has only a bag with a limited capacity. The challenge for the thief is to take as many gold bars as possible without exceeding the bag capacity while considering that gold bars can not be split (he can either take a bar or leave it!). If we opt for a Greedy strategy our stages would be the actual weight remaining in the bag and the actions that need to be considered are taking one of the currently available gold bars. In each stage, we are going to put in the bag the heaviest gold bar until there is no space available. Applying the above reasoning to solve the following instance of the problem where there are 3 gold bars with weights: 2, 2, 3, and a bag capacity of 4; we would end up recommending the thief to take the bar with weight 3 since it not only fits inside the bag but also it is the heaviest one at that stage. 1 will be the next remaining space which can not be filled with any remaining bar. However, one could easily notice that by putting the first two bars we can manage to get 4 as total weight which a better solution for the problem.

# Notes
I brought these ideas from my lecture of the book "Learning algorithmic through programming and puzzle-solving" by Alexander Kulikov and Pavel Pevzner;
all along while taking a course in the Coursera platform on algorithm and data structure: https://www.coursera.org/specializations/data-structures-algorithms