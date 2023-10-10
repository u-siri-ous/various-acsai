Let's train a logistic classifier:
* Start with a random classifier
* Repeat many, fixed times (epochs)
* Measure logloss to decide when to stop running, if it does not improve for 1000 steps (or if it is under a certain threshold)

## The logistic trick

This is similar to the perceptron trick. it has the two cases:
1. Case 1: If the point is correctly classified, **slightly move the line away from the point**. 
2. Case 2: If the point is incorrectly classified, **slightly move the line closer to the point**.

If points are deeper in the correct zone, their probability increases

![Pasted image 20231005153249](../pictures/Pasted%20image%2020231005153249.png)
![Pasted image 20231005153121](../pictures/Pasted%20image%2020231005153121.png)

* Update should be a multiple of y-ŷ
* Weight of aack should be updated by an amount proportional to #aack 
* The same with beep
* Bias is updated by an amount proportional to 1
* Finally, updates should be multiplied by the learning rate number