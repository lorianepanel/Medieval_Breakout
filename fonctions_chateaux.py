def castle1() :

    castle1 = [[ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0 ],
            [ 0, 0, 0, 2, 3, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 2, 3, 2, 0, 0, 0 ],
            [ 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0 ],
            [ 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 2, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            ]
            
    all_bricks1 = []

    for y in range(0, len(castle1)) :
        for x in range(0, 35) :
            if castle1[y][x] == 0 :
                brick1 = Actor("brick2", anchor=["left","top"])
                brick1.pos = [(x*30) + 210 , (y*30) + 130]
                all_bricks1.append(brick1)

            if castle1[y][x] == 2 :
                brick1 = Actor("door", anchor=["left","top"])
                brick1.pos = [(x*30) + 210 , (y*30) + 130]
                all_bricks1.append(brick1)

            if castle1[y][x] == 3 :
                brick1 = Actor("window", anchor=["left","top"])
                brick1.pos = [(x*30) + 210 , (y*30) + 130]
                all_bricks1.append(brick1)



def castle2():

    n = None

    castle2 = [[ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0 ],
            [ 0, n, n, n, n, n, n, n, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, n, n, n, n, n, n, n, 0 ],
            [ 0, n, n, n, n, n, n, n, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, n, n, n, n, n, n, n, 0 ],
            [ 0, n, n, n, n, n, n, n, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, n, n, n, n, n, n, n, 0 ],
            [ 0, n, n, n, n, n, n, n, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, n, n, n, n, n, n, n, 0 ],
            [ 0, n, n, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, n, n, 0 ],
            [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
            [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
            [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
            [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
            [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
            [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
            [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 2, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
            [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 2, 2, 2, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
            [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 2, 2, 2, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            ]



    all_bricks2 = []



    for y in range(0, len(castle2)) :
        for x in range(0, 35) :


            if castle2[y][x] == None :

                n = randint(0,4)

                if n == 0 :
                    brick2 = Actor("brick2", anchor=["left","top"])
                    brick2.pos = [(x*30) + 60 , (y*30) + 60]
                    all_bricks2.append(brick2)


                if n == 2 :
                    brick2 = Actor("door", anchor=["left","top"])
                    brick2.pos = [(x*30) + 60 , (y*30) + 60]
                    all_bricks2.append(brick2)

                if n == 3 :
                    brick2 = Actor("window", anchor=["left","top"])
                    brick2.pos = [(x*30) + 60 , (y*30) + 60]
                    all_bricks2.append(brick2)


            else :
                        
                if castle2[y][x] == 0 :
                    brick2 = Actor("brick2", anchor=["left","top"])
                    brick2.pos = [(x*30) + 60 , (y*30) + 60]
                    all_bricks2.append(brick2)

                if castle2[y][x] == 2 :
                    brick2 = Actor("door", anchor=["left","top"])
                    brick2.pos = [(x*30) + 60 , (y*30) + 60]
                    all_bricks2.append(brick2)

                if castle2[y][x] == 3 :
                    brick2 = Actor("window", anchor=["left","top"])
                    brick2.pos = [(x*30) + 60 , (y*30) + 60]
                    all_bricks2.append(brick2)

