

# Função de exponeciação modular
def mod_exp(base, expo, c):

    # a^0%c
    res=1
    # Como (a * b) mod n = [(a mod n) * (b mod n)] mod n, vamos aproveitar para "diminuir" esse 'a'
    base=base%c
    while(expo>0):
        if expo%2==1:
            res = (res * base)%c
        expo=expo>>1
        base = (base * base) % c
    return res

print("EU: ", mod_exp(55, 435, 14))
print("Py: ", pow(55, 435, 14))