#!/usr/bin/env python
# -*- coding: utf-8 -*-

# perceptron adaptado
# falso = 0, verdadeiro = 1
# numero maximo de interacoes
max_int = 200

# threshold (limiar)
threshold = -1

# peso 0
w_0 = threshold

# entrada 0
x_0 = -1

# entradas
##x =[[x_0,-0.3665,   0.0620  ,  5.9891],   
##   [x_0,-0.7842 ,   1.1267  ,  5.5912], 
##   [x_0, 0.3012 ,   0.5611  ,  5.8234], 
##   [x_0, 0.7757 ,   1.0648  ,  8.0677], 
##   [x_0, 0.1570 ,   0.8028  ,  6.3040], 
##   [x_0,-0.7014 ,   1.0316  ,  3.6005],
##   [x_0, 0.3748 ,   0.1536  ,  6.1537],   
##   [x_0,-0.6920 ,   0.9404  ,  4.4058],  
##   [x_0,-1.3970 ,   0.7141  ,  4.9263],   
##   [x_0,-1.8842 ,  -0.2805  ,  1.2548]]


x= [[x_0, 0.4329,   -1.3719,    0.7022, -0.8535],   
    [x_0, 0.3024,    0.2286,    0.8630,  2.7909],  
    [x_0, 0.1349,   -0.6445,    1.0530,  0.5687],  
    [x_0, 0.3374,   -1.7163,    0.3670, -0.6283] ] 



#portalogica

##x = [[x_0,0,0],
##     [x_0,0,1],
##     [x_0,1,0],
##     [x_0,1,1]]

# quantos itens tem o vetor x (30)
tamanho_x = len(x)

# quantos itens estão em cada posicao do vetor x
qtde_itens_x = len(x[0])


# pesos (sinapses)

import random
tam = 5
w = [0]*tam
for o in range(tam):
     w[o] = random.uniform(0,1)
     print("Peso Inicial " +str(o)+": %.4f"% w[o])
##w = [-1.5298, 0.7746, 1.2293, -0.3647]

# quantos itens tem o vetor w (3)
tamanho_w = len(w)

# respostas desejadas
#d = [0,0,0,1]
#d = [1,1,-1-1,-1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,-1,1,1,1,-1,-1,-1]

d = [1,0,0,0]


# taxa de aprendizado (n)
taxa_aprendizado = 0.0025

precisao = 0.05
eqmAnterior = 0 
eqmAtual = 0
eqm = 0
import math

#saida
y = 0

# resposta = acerto ou falha
resposta = ""

# soma
u = 0

#erro
e = 0

print("Treinando a rede")

# inicio do algoritmo
for k in range(1,max_int):
    acertos = 0    
    e = 0
    print("INTERACAO "+str(k)+"-----------------------------------")
    for t in range(0,tamanho_x):        
        u = 0

        # para calcular a saida do perceptron, cada entrada de x eh multiplicada
        # pelo seu peso w correspondente
        for j in range(0,qtde_itens_x):
            u += x[t][j] * w[j]

        y_in = u
      #  print("y_in = %.4f" % y_in)        

        # funcao de ativação
        if y_in >= 0:
            y = 1       
        else:
            y = 0
            
        # atualiza os pesos caso a saida nao corresponda ao valor esperado        
        if y == d[t]:
            resposta = "certo"
            acertos += 1
            e = 0            
        else:
            resposta = "errado"        
            # calculando o erro
        
            e = d[t] - y     
            
            
            
            
#        if (MSE > precisao):
        errom = 0
        for j in range(0,t):
            errom = errom + y/t

            
#                    math.fabs(eqmAnterior)
    
            # atualizando os pesos            
        for j in range (0,tamanho_w):
             w[j] = w[j] + taxa_aprendizado *e * x[t][j]
             print(resposta + " >>> u = " +str(u)+ ", y = "+ str(y)+ ", e = "+str(e))
                    
             while (math.fabs(eqmAtual - eqmAnterior)) > precisao:
           

              

                    if acertos == tamanho_x:
                        print("================================================ ")
                        print(" Rede Treinada com "+str(k)+" interacoes")
                        print("================================================ ")
                        print("                Pesos encontrados                ")
                        print("================================================ ")
                    for j in range (0,tamanho_w):
                        print("%.4f" % w[j])
                        break;

     
    print("")
    print("")
print("Finalizado")
