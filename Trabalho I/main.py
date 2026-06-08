
import random
import gmpy2

# -----------------------------------------------------------------------------------------------------
# Função de exponeciação modular
def mod_exp(base, expo, c):

    base, expo, c = gmpy2.mpz(base), gmpy2.mpz(expo), gmpy2.mpz(c)
    # a^0%c
    res=gmpy2.mpz(1)
    # Como (a * b) mod n = [(a mod n) * (b mod n)] mod n, vamos aproveitar para "diminuir" esse 'a'
    base=base%c
    while(expo>0):
        if expo%2==1:
            res = (res * base)%c
        expo=expo>>1
        base = (base * base) % c
    return res
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# mdc(a, b) = a*x + b*y
# mdc(a, b) = mdc(b, a % b).
# a = bq + r --> mdc(a, b) = mdc(b, r)
def ext_euclides(a, b):
    
    a, b = gmpy2.mpz(a), gmpy2.mpz(b)
    x0, x1 = gmpy2.mpz(1), gmpy2.mpz(0)
    y0, y1 = gmpy2.mpz(0), gmpy2.mpz(1)
    while (r = a % b) > 0:
        # a = b*q + r
        q = a // b
        a, b = b, r
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        
    return a, x0, y0
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
def mod_inverse(a, m):
    
    mdc, x, y = ext_euclides(a, m)
    
    if(mdc != 1) {
        print("Não pode gerar o inverso multiplicativo de ", a, " mod ", m)
        exit()
    }
       
    return x % m
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
def miller_rabin(n, k):
    
    if n in [2, 3]:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Passo 1: Encontrar 's' e 'd' tal que n - 1 = 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Executar o teste 'k' vezes
    for _ in range(k):
        # Passo 2: Escolher base aleatória 'a'
        a = random.randrange(2, n - 1)
        
        # Passo 3: x = a^d mod n (Usa a função da Fase 1)
        x = mod_exp(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
            
        # Passo 4: Elevações ao quadrado sucessivas
        for _ in range(s - 1):
            x = mod_exp(x, 2, n)
            if x == n - 1:
                break
        else:
            # Se o laço terminar sem 'break', n é composto
            return False
            
    # Se passou em todas as k iterações, é (com altíssima probabilidade) primo
    return True
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
def get_gen(p, q):
  
    p = gmpy2.mpz(p)
    q = gmpy2.mpz(q)
    
    # O gerador deve estar no intervalo [2, p - 2]
    limite_inferior = gmpy2.mpz(2)
    limite_superior = p - 2
    
    while True:
        g = gmpy2.mpz(random.randrange(int(limite_inferior), int(limite_superior) + 1)) 
        condicao1 = mod_exp(g, 2, p)
        if condicao1 == 1:
            continue
        condicao2 = mod_exp(g, q, p)
        if condicao2 == 1:
            continue
            
        return g
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# Diffie-Hellman
def get_prime_candidate(bits):
    p = gmpy2.mpz(random.getrandbits(bits))
    p |= (1 << bits - 1) | 1
    return p
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# Diffie-Hellman
def get_prime(bits):
    while True:
        p = get_prime_candidate(bits)
        if miller_rabin(p, 40):
            return p
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# Diffie-Hellman
def get_sure_prime(bits):
    while True:
        q = get_prime(bits - 1)
        p = 2 * q + 1
        if miller_rabin(p, 40):
            return p, q
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# ElGamal
def txt_to_int(txt):
    return gmpy2.mpz(int.from_bytes(txt.encode('utf-8'), 'big'))
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# ElGamal
def int_to_txt(i):
    size = (int(i).bit_length() + 7) // 8
    return int(i).to_bytes(size, 'big').decode('utf-8')
# -----------------------------------------------------------------------------------------------------

# --------------------------------------------------
# Geração de par de chaves ElGamal
def generate_keys(p, g):
    x = gmpy2.mpz(random.randrange(2, p - 2))
    h = mod_exp(g, x, p)
    return x, h
# --------------------------------------------------

# --------------------------------------------------
# Encripta uma mensagem de texto usando a chave pública do receptor
def encrypt_elgamal(txt, p, g, h):
    m = txt_to_int(txt)
    k = gmpy2.mpz(random.randrange(2, p - 2))
    c1 = mod_exp(g, k, p)
    s = mod_exp(h, k, p)
    c2 = (m * s) % p
    return c1, c2
# --------------------------------------------------

# --------------------------------------------------
# Desencripta o par (c1, c2) usando a chave privada do receptor
def decrypt_elgamal(cipher, p, x):
    c1, c2 = cipher
    s = mod_exp(c1, x, p)
    s_inv = mod_inverse(s, p)
    m = (c2 * s_inv) % p
    return int_to_txt(m)
# --------------------------------------------------

# --------------------------------------------------
# Simula uma troca simples de mensagem entre A e B
def messaging():
    p, q = get_sure_prime(64)
    g = get_gen(p, q)

    b_priv, b_pub = generate_keys(p, g)
    msg = "Olá Mundo"
    cipher = encrypt_elgamal(msg, p, g, b_pub)
    decrypted = decrypt_elgamal(cipher, p, b_priv)

    print(f"Primos usados: p={p}, q={q}")
    print(f"Gerador g={g}")
    print(f"Chave pública de B: {b_pub}")
    print(f"Chave privada de B: {b_priv}")
    print(f"Mensagem original: {msg}")
    print(f"Mensagem criptografada: c1={cipher[0]}, c2={cipher[1]}")
    print(f"Mensagem descriptografada: {decrypted}")
# --------------------------------------------------

if __name__ == "__main__":
    messaging()
# -----------------------------------------------------------------------------------------------------
