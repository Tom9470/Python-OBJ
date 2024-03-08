def _Min(dat):
    """
    returns minimum value of nested list
    """
    curr = min(dat[0])
    for i in dat:
        temp = min(i)
        if curr>temp:curr=temp
    return curr

def CreateSurface(filename,data):
    """
    Creates a Surface from a heightmap. File created is a Wavefront .OBJ object.

    :parameters:
        `filename` : the filename to store the object in.
        `data` : a list of lists, containing the heightmap.
    """
    vertices=dict()
    counter = 1
    obj=open(filename,"w+")

    #vertices
    for index,i in enumerate(data):
        for jindex,j in enumerate(i):
            obj.write(f"v {jindex} {index} {0.2*j}\n")
            vertices[(jindex,index)] = str(counter)
            counter+=1
    
    #surface
    dimy,dimx=len(data)-1,len(data[0])-1
    for y in range(dimy):
        for x in range(dimx):
            obj.write(f"f {vertices[(x,y)]} {vertices[(x+1,y)]} {vertices[(x,y+1)]}\n")
            obj.write(f"f {vertices[(x+1,y)]} {vertices[(x+1,y+1)]} {vertices[(x,y+1)]}\n")
    #obj.write(f"f {vertices[(0,0)]} {vertices[(dimx,0)]} {vertices[(0,dimy)]} {vertices[(dimx,dimy)]}")
    obj.close()

def CreateObject(filename,data):
    """
    Creates a 3D object from a heightmap. File created is a Wavefront OBJ object.

    :parameters:
        `filename` : the filename to store the object in.
        `data` : a list of lists, containing the heightmap.
    """

    width=len(data[0])
    height=len(data)

    vertices=dict()
    base=dict()
    counter = 5
    obj=open(filename,"w+")
    minimum=_Min(data)
    dimy,dimx=len(data)-1,len(data[0])-1
    obj.write(f"v 0 0 {minimum}\nv 0 {dimy} {minimum}\nv {dimx} 0 {minimum}\nv {dimx} {dimy} {minimum}\n")
    #vertices
    for index,i in enumerate(data):
        for jindex,j in enumerate(i):
            obj.write(f"v {jindex} {index} {0.2*j}\n")
            vertices[(jindex,index)] = str(counter)
            counter+=1
    for z in range(int(height)):
        obj.write(f"v 0 {z} {minimum}\n")
        base[(0,z)] = counter
        counter +=1
        obj.write(f"v {dimx} {z} {minimum}\n")
        base[(dimx,z)] = counter
        counter +=1
    for z in range(int(width)):
        obj.write(f"v {z} 0 {minimum}\n")
        base[(z,0)] = counter
        counter +=1
        obj.write(f"v {z} {dimy} {minimum}\n")
        base[(z,dimy)] = counter
        counter +=1

    #top
    obj.write("\nf 1 2 3\nf 2 3 4\n")

    for y in range(dimy):
        for x in range(dimx):
            obj.write(f"f {vertices[(x,y)]} {vertices[(x+1,y)]} {vertices[(x,y+1)]}\n")
            obj.write(f"f {vertices[(x+1,y)]} {vertices[(x+1,y+1)]} {vertices[(x,y+1)]}\n")

    for i in range(dimx):
        #top face
        obj.write(f"f {base[(i,0)]} {base[(i+1,0)]} {vertices[(i,0)]}\nf {base[(i+1,0)]} {vertices[(i,0)]} {vertices[(i+1,0)]}\n")
        #bottom face
        obj.write(f"f {base[(i,dimy)]} {base[(i+1,dimy)]} {vertices[(i,dimy)]}\nf {base[(i+1,dimy)]} {vertices[(i,dimy)]} {vertices[(i+1,dimy)]}\n")
    for i in range(dimy):
        #left
        obj.write(f"f {base[(0,i)]} {base[(0,i+1)]} {vertices[(0,i)]}\nf {base[(0,i+1)]} {vertices[(0,i)]} {vertices[(0,i+1)]}\n")
        #right
        obj.write(f"f {base[(dimx,i)]} {base[(dimx,i+1)]} {vertices[(dimx,i)]}\nf {base[(dimx,i+1)]} {vertices[(dimx,i)]} {vertices[(dimx,i+1)]}\n")
    obj.close()