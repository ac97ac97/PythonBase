def position(dt,speed):
    posx = dt *speed[0]
    posy = dt*speed[1]
    return (posx,posy)
move = position(60.0,(10,-5))
print("物体的位移：({0},{1})".format(move[0],move[1]))