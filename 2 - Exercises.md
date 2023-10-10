## Compute the error function 
### Classifier 1

Weights:
* Aack   a = 1
* Beep   b = 2
* Bias     c = -4
Prediction:
<b>ŷ = step(x<sub>aack</sub> - 2x<sub>beep</sub> - c)</b>

### Classifier 2

Weights:
* Aack   a = -1
* Beep   b = 1
* Bias     c = 0
Prediction:
<b>ŷ = step(-x<sub>aack</sub> +x<sub>beep</sub>)</b>

![Pasted image 20231003141632](../pictures/Pasted%20image%2020231003141632.png)

![Pasted image 20231003141802](../pictures/Pasted%20image%2020231003141802.png)

>NOTE: 
>Encoding: 1 $\rightarrow$ happy, 0 $\rightarrow$ sad
>In class, point (1, 3) is **sad(0)**, but the table was too long to do in md
>Apply prediction equation with the scores


**REM**: if the point is correctly classified, the error is 0, otherwise its |score|

Classifier 1 error column:
1. 0
2. 2
3. 3
4. 3

Classifier 2 error column:
1. 0
2. 0
3. 2
4. 0

Mean perceptron error (classifier 1): -2
Mean perceptron error (classifier 2): 0,5

