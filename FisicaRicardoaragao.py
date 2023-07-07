from vpython import *


scene = canvas(width=640, height=480, center=vector(8, 5, 0), range=8, background=color.orange)

#cena



#chao
ground_color = vector(0.545, 0.271, 0.075)  # Valor RGB para a cor marrom
ground = box(pos=vector(8, -5, 0), length=100, height=10, width=0.5, color=ground_color)









# Montanha
mountain = box(pos=vector(12, 0, -20), length=100, height=20, width=20, color=color.gray(0.6))

#   carro em cima da montanha
car = box(pos=vector(12, 11, -11), length=2, height=1, width=1, color=color.red)
pedra = box(pos=vector(2, 10, -15), length=2, height=1, width=1, color=color.yellow)
pedra1 = box(pos=vector(17, 10, -15), length=2, height=1, width=1, color=color.yellow)
pedra2 = box(pos=vector(6, 10, -15), length=2, height=1, width=1, color=color.yellow)

#sol
sun = sphere(pos=vector(40, 28, -20), radius=2, color=color.yellow)


#rodas ao carro
wheel_radius = 0.3
wheel_width = 0.2

front_left_wheel = cylinder(pos=vector(11.5, 10.5, -11.3), axis=vector(0, -wheel_width, 0), radius=wheel_radius, color=color.black)
front_right_wheel = cylinder(pos=vector(12.5, 10.5, -11.3), axis=vector(0, -wheel_width, 0), radius=wheel_radius, color=color.black)
rear_left_wheel = cylinder(pos=vector(11.5, 10.5, -10.7), axis=vector(0, -wheel_width, 0), radius=wheel_radius, color=color.black)
rear_right_wheel = cylinder(pos=vector(12.5, 10.5, -10.7), axis=vector(0, -wheel_width, 0), radius=wheel_radius, color=color.black)




#   árvore como obstáculo

trunk = cylinder(pos=vector(6, -4.5, 0), axis=vector(0, 4, 0), radius=0.3, color=vector(0.4, 0.2, 0))  # Tronco da árvore
foliage = cone(pos=vector(6, 0, 0), axis=vector(0, 2, 0), radius=0.6, color=color.green)  # Copa da árvore






#seta a apontar para o alvo

obstacle3 = ([box(pos=vector(20, -3, 0), length=1, height=1, width=1, color=color.yellow)])
obstacle4 = ([box(pos=vector(18, -4, 0), length=1, height=1, width=1, color=color.yellow)])
obstacle5 = ([box(pos=vector(16, -5, 0), length=1, height=1, width=1, color=color.yellow)])
obstacle6 = ([box(pos=vector(14, -6, 0), length=1, height=1, width=1, color=color.yellow)])
obstacle7 = ([box(pos=vector(12, -7, 0), length=1, height=1, width=1, color=color.yellow)])

obstacle2 = ([box(pos=vector(19, -6, 0), length=1, height=1, width=1, color=color.yellow)])
obstacle8 = ([box(pos=vector(17, -2, 0), length=1, height=1, width=1, color=color.yellow)])

#distancia do alvo
dist = 25
#alvo
target = box(pos=vector(dist,1,0), length=0.5, height=2, width=0.5, color=color.purple)



height = 1
platform = box(pos=vector(-2,height-0.25,0), length=4, height=0.5, width=0.5, color=color.white)
bird = sphere(pos=vector(0,height+0.3,0), radius=0.3, color=color.purple)


hit = 0

while hit == 0:
    # Solicitar velocidade e ângulo ao usuário
    v0 = float(input('Digite a velocidade: '))
    dtheta = float(input('Digite o ângulo: '))
    theta = radians(dtheta)  # Converter graus em radianos




    #Desenha a seta
    px = 0.1*v0*cos(theta) #calcula a posição inicial de x
    py = 0.1*v0*sin(theta) #calcula a posição inicial de y
    momentum = arrow(pos=bird.pos, axis=vector(px,py,0), shaftwidth=0.1, color=color.orange) #draw arrow representing projectiles initial momentum




    g1 = input('Diga um nome de um planeta do sistema solar:\nterra,marte,jupiter,mercurio,saturno,venus,neptuno,urano: ')
    if g1 == 'terra':
        g = 9.81
    elif g1 == 'marte':
        g = 3.72
    elif g1 == 'jupiter':
        g = 24.79
    elif g1 == 'mercurio':
        g = 3.7
    elif g1 =='saturno':
        g = 10.44
    elif g1 == 'venus':
        g = 8.87
    elif g1 == 'neptuno':
        g = 11.13
    elif g1 == 'urano':
        g = 8.87
    else : g = 70.70



    #Define parâmetros iniciais
    x = x0 = 0
    y = y0 = height
    dt = 0.0001 #timestep
    t = 0





    #condições que deixam a animação correr se não bater no alvo
    while (y > 0 and (x < dist-0.25 or x > dist+0.25)) or (y > 2 and x >= dist-0.25 and x<= dist+0.25):

            rate(5000) #fram-rate

            x = x0 + v0*t*cos(theta) # calcula nova posição x
            y = y0 + v0*t*sin(theta)-0.5*g*t**2 # calcula nova posição y
            bird.pos = vector(x,y,0) #redesenha a posição da bola no programa

            px = 0.1*v0*cos(theta) # calcula a posição em x da seta
            py = 0.1*v0*sin(theta)-0.1*g*t #calcula a posição em y da seta
            momentum.pos = bird.pos #redesenha a seta
            momentum.axis = vector(px,py,0) #redesenha com as posições

            t += dt # incrementa o tempo

            if x >= 6 - foliage.radius and x <= 6 + foliage.radius and y <= foliage.pos.y + foliage.axis.y:
                hit = True
                break

    momentum.visible = False #Se falhar o alvo, tira a seta
    if hit:
        # Código para quando a colisão ocorre
        print('A bola colidiu com a arvore!')
         

    #é definida uma condição inversa que define se o alvo voi acertado ou não
    if y >= 0 and y <= 2 and x >= dist-0.25 and x <= dist+0.25:

        #calcula se o alvo cai ou não
        trest = 0.5*100*g*0.5 #calcula o torque do alvo para a bola
        contact_t = 0.01 #define quanto tempo a bola está em contacto com o alvo
        fapp = vector(px, py, 0) / contact_t #calcula a força aplicada ao alvo
        tapp = cross(fapp, vector((dist+0.25)-x, -y, 0)) #calcula torque exercida pela bola ao alvo
        tappm = mag(tapp) #calcula a magnitude da força aplicada

        if tappm > trest: #alvo caiu

            target.pos = vector(dist+1.25,0.25,0)
            target.length = 2
            target.height =0.5
            print('Acertou!')
            hit = 1

        else: #não derrubou
            print('Acertou mas não caiu')

        #anima a bola a cair
        t=0 #reset do tempo
        y0=y #set do y0 para zero
        while y > 0.3:
            rate(5000)
            y = y0 - 0.5*g*t**2
            bird.pos = vector(x,y,0)
            t += dt

    else:
        print('Falhou, tente de novo.')

