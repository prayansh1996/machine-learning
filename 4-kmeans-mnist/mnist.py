import numpy as np
import pandas
from matplotlib import pyplot as plt
While trying to find the number of distinct ways we can multiply (parenthesize) n matrices without changing their order ([Matrix Chain Multiplication](https://en.wikipedia.org/wiki/Matrix_chain_multiplication)) and using a bottom up approach, I came up with this recurrence relation for Catalan Numbers - 

While trying to find the number of distinct ways we can multiply (parenthesize) n matrices without changing their order ([Matrix Chain Multiplication](https://en.wikipedia.org/wiki/Matrix_chain_multiplication)) and using a bottom up approach, I came up with this recurrence relation for Catalan Numbers - 

$$T(n) = ^{n-1}C_1.T(n-1) - ^{n-2}C_2.T(n-2)   +  ^{n-3}C_3.T(n-3) - ^{n-4}C_4.T(n-4)...$$

or
$$\bbox[5px] T(n) = \lvert \sum \limits_{k=1}^{\lfloor n/2 \rfloor} (-1)^{n-k}.^{n-k}C_k.T(n-k) \rvert$$

Where T(n) is the nth Catalan Number. 

From the Top Down approach and from [Wikipedia](https://en.wikipedia.org/wiki/Catalan_number) we get the solution -

$$C_{n}={\frac {1}{n+1}}{2n \choose n}={\frac {(2n)!}{(n+1)!\,n!}}=\prod \limits _{k=2}^{n}{\frac {n+k}{k}}\qquad {\mbox{ for }}n\geq 0.$$

Is it possible to derive one from the other?

For any given set- $$ABCDE$$

Bottom Up approach: Make pairs of 2 matrices and remove the duplicate solutions - 
$$(AB)CDE,\bbox[5px] A(BC)DE, \bbox[5px]AB(CD)E, \bbox[5px]ABC(DE)$$ 

Top Down approach: Seperate the set into two distinct sets, no need to remove duplicates - 
$$(A)(BCDE),\bbox[5px] (AB)(CDE), \bbox[5px](ABC)(DE), \bbox[5px](ABCD)(E)$$ 
