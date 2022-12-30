def quantosBlocosUsados(lista_blocos, total, minimo_blocos):
    for blocos in range(total + 1):
        contaBlocos = blocos
        for i in [b for b in lista_blocos if b <= blocos]:  # Consideramos o uso de todos os blocos possiveis para igualar o total necessario
            if minimo_blocos[blocos - i] + 1 < contaBlocos:  # minimo_blocos armazena os blocos usados e contaBlocos guarda o numero minimo de blocos utilizados
                contaBlocos = minimo_blocos[blocos - i] + 1  # Se for menor os valores são trocados
        minimo_blocos[blocos] = contaBlocos  # E guardamos o minimo de blocos possiveis utilizados
    return minimo_blocos[total]  # Retornamos o valor minimo utilizado na última iteração que sera o total que queremos


def main():
    t = int(input())
    while t > 0:
        t -= 1
        n, m = input().split()
        n = int(n)
        m = int(m)
        lista = input().split()
        lista = [int(val) for val in lista]
        contadorBlocos = [0] * (m + 1)
        if n == len(lista):
            print(quantosBlocosUsados(lista, m, contadorBlocos))


main()
