### Como Squirrel Method funciona:

### A criptografia é feita com o **Calculo**, vamos dar um exemplo com a sua senha sendo 'abelha',
#### 'a' = 97 da ordem numerica ASCII, a soma seria 97+6+(exp(1)=1)+=97+6+(exp(-1)=-1), então 'a' = 'u',
#### 'b' = 98 da ordem numerica ASCII, a soma seria 98+6+(exp(1)=2)+=98+6+(exp(-1)=-2), então 'b' = 'y',
#### 'e' = 101 da ordem numerica ASCII, a soma seria 101+6+(exp(1)=3)+=101+6+(exp(-1)=-3), então 'e' = 'G',
#### 'l' = 108 da ordem numerica ASCII, a soma seria 108+6+(exp(1)=4)+=108+6+(exp(-1)=-4), então 'l' = 'W',
#### 'h' = 104 da ordem numerica ASCII, a soma seria 104+6+(exp(1)=5)+=104+6+(exp(-1)=-5), então 'h' = 'Q',
#### 'a' = 97 da ordem numerica ASCII, a soma seria 97+6+(exp(1)=6)+=97+6+(exp(-1)=-6), então 'a' = 'E'

### Porém, depende bastante do tamanho da senha, pois se voce tentar encriptografar apenas a primeira letra da sua senha que seria o 'a',<br>por exemplo, o resultado seria 'a' = 'k'

#### *Calculo - ordem numerica do caracter em ASCII + tamanho da senha + exponencial(1) += ordem numerica do caracter em ASCII + tamanho da senha + exponencial(-1)*