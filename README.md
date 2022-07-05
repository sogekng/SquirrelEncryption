### How Squirrel Method works:

### Encryption is done with *Calculation*, let's take an example with your password being 'abelha',
#### 'a' = 97 of ASCII numerical order, the sum would be 97+6+(exp(1)=1)+=97+6-(exp(-1)=-1), so 'a' = 'u',
#### 'b' = 98 of ASCII numerical order, the sum would be 98+6+(exp(1)=2)+=98+6-(exp(-1)=-2), so 'b' = 'y',
#### 'e' = 101 of the ASCII numerical order, the sum would be 101+6+(exp(1)=3)+=101+6-(exp(-1)=-3), so 'e' = 'G',
#### 'l' = 108 of ASCII numerical order, the sum would be 108+6+(exp(1)=4)+=108+6-(exp(-1)=-4), so 'l' = 'W',
#### 'h' = 104 of ASCII numerical order, the sum would be 104+6+(exp(1)=5)+=104+6-(exp(-1)=-5), so 'h' = 'Q',
#### 'a' = 97 of ASCII numerical order, the sum would be 97+6+(exp(1)=6)+=97+6-(exp(-1)=-6), so 'a' = 'E'.

#### The result depends a lot on the length of the password, because if you try to encrypt only the first letter of your password, which would be the 'a', for example, the calculation being 'a' = 97 of the ASCII numerical order, the sum would be 97+1+(exp(1)=1)+=97+1-(exp(-1)=-1), so 'a' = 'k'.

#### *Calculation - ASCII numeric character order + password length + exponential(1) += ASCII numeric character order + password length + exponential(-1)*.