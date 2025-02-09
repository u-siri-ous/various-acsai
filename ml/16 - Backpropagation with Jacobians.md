Pytorch creates a DAG under the hood

![](pictures/Pasted%20image%2020250206193504.png)
# REMARK

![](pictures/Pasted%20image%2020250206181212.png)
![](pictures/Pasted%20image%2020250206181223.png)

-------

![](pictures/Pasted%20image%2020250206194607.png)![](pictures/Pasted%20image%2020250206194859.png)
![](pictures/Pasted%20image%2020250206193825.png)
ooooookay so the green values are computed by the forward pass

the yellow values are **local gradients** → **partial derivatives of a function with respect to its inputs at a specific point** 

the red values are **external gradients** → **gradients that come from the subsequent layers during the backward pass and propagate error**

They are the product of the subsequent layer external gradient by the current local gradient

![](pictures/Pasted%20image%2020250206195528.png)

**The output layer does not have a gradient because there isn't a fcn applied at the output!** It's the starting point of backpropagation 

It's considered to be 1 for a simplified view of the start of backpropagation

![](pictures/Pasted%20image%2020250206200100.png)

![](pictures/Pasted%20image%2020250206200117.png)

------------
# Another Example (loooots of pictures)

1. ![](pictures/Pasted%20image%2020250206200916.png)
2. ![](pictures/Pasted%20image%2020250206200934.png)
	![](pictures/Pasted%20image%2020250206201007.png)
	
3. ![](pictures/Pasted%20image%2020250206201016.png)
4. ![](pictures/Pasted%20image%2020250206201128.png)
5. ![](pictures/Pasted%20image%2020250206201501.png)

![](pictures/Pasted%20image%2020250206201532.png)
![](pictures/Pasted%20image%2020250206201557.png)
![](pictures/Pasted%20image%2020250206201834.png)

so, finally:

![](pictures/Pasted%20image%2020250206201815.png)
![](pictures/Pasted%20image%2020250206201931.png)

