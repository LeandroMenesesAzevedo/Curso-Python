print (' ============== Boletim ============== ')
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda  nota do aluno: '))
media = (nota1 + nota2)/2

if media >= 6.0:
    print(' Parabéns, você foi aprovado!')
else:
    print('Você terá que fazer prova final')