
# Solução Desenvolvida

Foram desenvolvidas as funções de para:

* Exponenciação modular eficiente (mod_exp)
* Inverso modular (Euclides Estendido) (mod_inverse, ext_euclides)
* Teste Miller-Rabin
* Geração de números primos grandes (get_prime)
* Geração de primos seguros (p = 2q + 1) (get_sure_prime)
* Geração do grupo multiplicativo mod p (get_gen)
* Diffie-Hellman 
* ElGamal
* Conversão texto para inteiro e vice-versa

Foi usada a gmpy2 para trabalhar com inteiros grandes

# Diffie-Hellman

O algoritmo de Diffie-Helman tem seguinte sequencia de passos:

1. Geração de um primo p (get_sure_prime)
2. Escolha de g gerador do grupo multiplicativo mod p (get_gen)
3. Escolha de um valor secreto a por A.
4. Escolha de um valor secreto b por B.
5. Cálculo das chaves públicas (mod_exp):
    - A = g^a mod p
    - B = g^b mod p
6. Troca das chaves públicas.
7. Cálculo do segredo:
    - Segredo = B^a mod p
    - A^b mod p

Pelas propriedades da exponenciação modular:

8. Segredo = g^(ab) mod p

Assim A e B conseguem gerar o mesmo segredo

# Implementação do Esquema ElGamal

## Geração de Chaves

1. Obtem-se os valores p e g (ordem e gerador)
2. B escolhe a chave privada x.
3. B calcula a chave pública h = g^x mod p (mod_exp)

## Criptografia

Para criptografar uma mensagem m codificada como int:

1. Escolhe-se um k aleatorio.
2. Calcula-se c1 = g^k mod p
3. Calcula-se c2 = m * h^k mod p
4. O texto criptografado será (c1, c2)

## Descriptografia

1. Calcular s = c1^x mod p
2. Calcular mod_inverse(s, p):
3. mensagem = c2 . s^-1 mod p
(4. conversão em texto)

# Miller-Rabin

1. para um 'n' ímpar, calcular n − 1 = 2^s · d para um 'd' impar

# Dificuldades Encontradas

- Entender como se implementar uma exponenciação modular eficiente
- Preencer "lacunas de conhecimento" e entender como elgamal utiliza miller-rabin para geração de primos, por exemplo