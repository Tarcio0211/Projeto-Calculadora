def calculadora(n1,n2,operador):
    primeiro_numero=float (input("Digite o primeiro número aqui:"))
    segundo_numero=float (input("Digite o segundo  número aqui:"))
    seu_operador=input("Digite o seu operador pra fazer o calculo aqui:")
    if seu_operador=="+":
        return primeiro_numero+segundo_numero
    elif seu_operador=="-":
        return primeiro_numero-segundo_numero
    elif seu_operador=="/":
        return primeiro_numero/segundo_numero
    elif seu_operador=="*":
        return  primeiro_numero*segundo_numero
    else:
        return"operador inválido"
    
resultado_calculadora=calculadora("n1","n2","operador")
print(f"o resultado do calculo é:{resultado_calculadora}")   