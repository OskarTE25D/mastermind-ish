def hitta_pos(box,sub):
    pos_list=[]
    for pos, zombiecat in enumerate(box):
        if zombiecat==sub:
            pos_list.append(pos)
    return pos_list

#sub = det du vill hitta positionerna av
#box = strängen eller listan som du vill söka igenom (alltså lådan som håller informationen)
#pos_list = lista med alla positioner av sub