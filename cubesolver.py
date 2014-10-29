

Top= ["W","W","W","W","W","W","W","W","W"]
Front=["B","B","B","B","B","B","B","B","B"]
Down= ["Y","Y","Y","Y","Y","Y","Y","Y","Y"]
Back= ["G","G","G","G","G","G","G","G","G"]
Right= ["O","O","O","O","O","O","O","O","O"]
Left=["R","R","R","R","R","R","R","R","R"]
Solution=Top+Front+Down+Back+Right+Left

import copy
def R(Cube):
    """R"""
    oldcube=copy.deepcopy(Cube)
    Moved=copy.deepcopy(Cube)
    
    Moved[2],Moved[5],Moved[8]=oldcube[11],oldcube[14],oldcube[17]
    
    Moved[11],Moved[14],Moved[17]= oldcube[20],oldcube[23],oldcube[26]
    
    Moved[20],Moved[23],Moved[26]=oldcube[33],oldcube[30],oldcube[27]

    Moved[27],Moved [30],Moved[33]=oldcube[8],oldcube[5],oldcube[2]

    Moved[36],Moved[38],Moved[44],Moved[42]= oldcube[42],oldcube[36],oldcube[38],oldcube[44]
    Moved[39],Moved[37],Moved[41],Moved[43]= oldcube[43],oldcube[39],oldcube[37],oldcube[41]
    
    return Moved

def FPrime(Cube):
    """FPrime"""
    oldcube=copy.deepcopy(Cube)
    Moved=copy.deepcopy(Cube)
    Moved[6],Moved[7],Moved[8]=oldcube[36],oldcube[39],oldcube[42]
    Moved[36],Moved[39],Moved[42]=oldcube[20],oldcube[19],oldcube[18]
    Moved[20],Moved[19],Moved[18]=oldcube[53],oldcube[50],oldcube[47]
    Moved[53],Moved[50],Moved[47]=oldcube[6],oldcube[7],oldcube[8]
    
    Moved[9],Moved[11],Moved[15],Moved[17]=oldcube[11],oldcube[17],oldcube[9],oldcube[15]
    Moved[10],Moved[12],Moved[14],Moved[16]=oldcube[14],oldcube[10],oldcube[16],oldcube[12]
    return Moved

def F2(Cube):
    """F2"""
    return FPrime(FPrime(Cube))

def F(Cube):
    """F"""
    return F2(FPrime(Cube))

def R2(Cube):
    """R2"""
    return R(R(Cube))

def RPrime(Cube):
    """RPrime"""
    return R2(R(Cube))

def B(Cube):
    """B"""
    oldcube=copy.deepcopy(Cube)
    Moved=copy.deepcopy(Cube)

    Moved[0],Moved[1],Moved[2]=oldcube[38],oldcube[41],oldcube[44]

    Moved[38],Moved[41],Moved[44]= oldcube[26],oldcube[25],oldcube[24]
    
    Moved[26],Moved[25],Moved[24]=oldcube[51],oldcube[48],oldcube[45]
    
    Moved[51],Moved [48],Moved[45]=oldcube[0],oldcube[1],oldcube[2]

    Moved[27],Moved[29],Moved[35],Moved[33]=oldcube[33],oldcube[27],oldcube[29],oldcube[35]
    Moved[28],Moved[30],Moved[32],Moved[34]=oldcube[30],oldcube[34],oldcube[28],oldcube[32]
    return Moved
    
    

def LPrime(Cube):
    """LPrime"""
    oldcube=copy.deepcopy(Cube)
    Moved=copy.deepcopy(Cube)

    Moved[0],Moved[3],Moved[6]=oldcube[9],oldcube[12],oldcube[15]

    Moved[9],Moved[12],Moved[15]= oldcube[18],oldcube[21],oldcube[24]
    
    Moved[18],Moved[21],Moved[24]=oldcube[35],oldcube[32],oldcube[29]
    
    Moved[29],Moved [32],Moved[35]=oldcube[6],oldcube[3],oldcube[0]

    Moved[45],Moved[47],Moved[51],Moved[53]=oldcube[47],oldcube[53],oldcube[45],oldcube[51]
    Moved[46],Moved[48],Moved[50],Moved[52]=oldcube[50],oldcube[46],oldcube[52],oldcube[48]
    return Moved
    

def L2(Cube):
    """L2"""
    return L(L(Cube))

def L(Cube):
    """L"""
    return LPrime(LPrime(LPrime(Cube)))

def U(Cube):
    """U"""
    oldcube=copy.deepcopy(Cube)
    Moved=copy.deepcopy(Cube)
    #Front top row becomes right top row
    Moved[9],Moved[10],Moved[11]=oldcube[36],oldcube[37],oldcube[38]
    #Right top row become back top row
    Moved[36],Moved[37],Moved[38]= oldcube[27],oldcube[28],oldcube[29]
    #Back top row become left top row
    Moved[27],Moved[28],Moved[29]=oldcube[45],oldcube[46],oldcube[47]
    #Left top row become front top row
    Moved[45],Moved [46],Moved[47]=oldcube[9],oldcube[10],oldcube[11]


    Moved[0],Moved[2],Moved[6],Moved[8]=oldcube[6],oldcube[0],oldcube[8],oldcube[2]
    Moved[1],Moved[3],Moved[5],Moved[7]=oldcube[3],oldcube[7],oldcube[1],oldcube[5]
    return Moved

def U2(Cube):
    """U2"""
    return U(U(Cube))

def UPrime(Cube):
    """UPrime"""
    return U(U2(Cube))

def D(Cube):
    """D"""
    oldcube=copy.deepcopy(Cube)
    Moved=copy.deepcopy(Cube)
    
    Moved[15],Moved[16],Moved[17]=oldcube[51],oldcube[52],oldcube[53]
    
    Moved[51],Moved[52],Moved[53]= oldcube[33],oldcube[34],oldcube[35]
    
    Moved[33],Moved[34],Moved[35]=oldcube[42],oldcube[43],oldcube[44]
    
    Moved[42],Moved[43],Moved[44]=oldcube[15],oldcube[16],oldcube[17]
    
    Moved[18],Moved[20],Moved[24],Moved[26]=oldcube[24],oldcube[18],oldcube[26],oldcube[20]
    Moved[19],Moved[21],Moved[23],Moved[25]=oldcube[21],oldcube[25],oldcube[19],oldcube[23]
    return Moved

def D2(Cube):
    """D2"""
    return D(D(Cube))

def DPrime(Cube):
    """DPrime"""
    return D(D2(Cube))

def BPrime(Cube):
    """BPrime"""
    return B2(B(Cube))
    
def B2(Cube):
    """B2"""
    return B(B(Cube))

def isCross(cube):
    if (cube[16]==cube[13] and cube[43]==cube[40] and cube[34]==cube[31] and cube[52]==cube[49] and
        cube[19]==cube[22] and cube[21]==cube[22] and cube[23]==cube[22] and cube[25]==cube[22]):
        return True
    else:
        return False
    
def makeCross(scrambledCube):
    cube=scrambledCube
    moveList=[]
    moves=[F,R,B,L,U,D,UPrime,RPrime,DPrime,FPrime,LPrime,L2,F2,D2,R2,U2,B2]
    
    ###Making the Cross is split into two parts:
    ###one, bringing all the down face edges up to the top face and correctly flipping them
    ###second, making the cross by doing R2,L2,F2,D2 with appropriate turns

    
    #DO R MOVES TO SEE IF YOU CAN BRING A YELLOW EDGE UP TO THE TOP RIGHT EDGE SPOT
    for x in xrange(4):
        if cube[5]==cube[22]:
            break
        else:
            newcube=R(cube)
            cube=newcube
            moveList+=[R]
            if x==3:
                del moveList[-1]
                del moveList[-1]
                del moveList[-1]
                del moveList[-1]
                
    ##Doing R turns was not good enough to place a cross edge on the top right edge spot.
    ##Lets do combos of moves to try to fix it
    if moveList==[]:
        if cube[5]!=cube[22]:
            for move in xrange(len(moves)):
                newcube=moves[move](cube)
                cube,List=getRightCrossPieceInPlaceOnce(newcube)
            #if move==RPrime and moveList==[]:
             #   moveList=moveList+[moves[move]]+List
              #  break
                if cube[5]==cube[22]:
                    moveList=moveList+[moves[move]]+List
                    break
                cube=scrambledCube
    currentcube=cube
    #return cube
    
    ###At this point the right top edge is a yellow edge with the yellow sticker facing upwards


    ###TRY DOING F MOVES TO PLACE A CROSS EDGE ON THE TOP FRONT
    ## note unflipped edge still counts
    for x in xrange(4):
        if ((cube[7]==cube[22] or (cube[7]==cube[13] and cube[10]==cube[22])
        or (cube[7]==cube[40] and cube[10]==cube[22])
        or (cube[7]==cube[31] and cube[10]==cube[22]))
        or (cube[7]==cube[49] and cube[10]==cube[22])):
            break
        else:
            newcube=F(cube)
            cube=newcube
            moveList+=[F]
            if x==3:
                del moveList[-1]
                del moveList[-1]
                del moveList[-1]
                del moveList[-1]
    currentcube=cube
              
    ##DOING JUST F'S DIDNT WORK
    ##note for simplicity, the edge does not have to be oriented properly
    for x in xrange(1):
        if ((cube[7]==cube[22]) or (cube[7]==cube[13] and cube[10]==cube[22])
        or (cube[7]==cube[40] and cube[10]==cube[22])
        or (cube[7]==cube[31] and cube[10]==cube[22])
        or (cube[7]==cube[49] and cube[10]==cube[22])):
            break
        limitedmoves=[L,D,DPrime,LPrime,L2,D2]
        for move in xrange(len(limitedmoves)):
            newcube=limitedmoves[move](cube)
            cube,List=getFrontCrossPieceInPlace(newcube)
            if ((cube[7]==cube[22] or (cube[7]==cube[13] and cube[10]==cube[22])
            or (cube[7]==cube[40] and cube[10]==cube[22])
            or (cube[7]==cube[31] and cube[10]==cube[22]))
            or (cube[7]==cube[49] and cube[10]==cube[22])):
                moveList=moveList+[limitedmoves[move]]+List
                break
            cube=currentcube
    currentcube=cube
    cube=U2(cube)
    moveList+=[U2]
    currentcube=cube
    
    ###Front, Right top edges are both yellow edges at this point. U2 makes way for putting another yellow edge on the top right spot
    ##note the edge does not have to be oriented properly
    
    ##Try doing R moves
    for x in xrange(4):
        if ((cube[5]==cube[22] or (cube[5]==cube[40] and cube[37]==cube[22])
        or (cube[5]==cube[13] and cube[37]==cube[22])
        or (cube[5]==cube[31] and cube[37]==cube[22]))
        or (cube[5]==cube[49] and cube[37]==cube[22])):
            break
        else:
            newcube=R(cube)
            cube=newcube
            moveList+=[R]
            if x==3:
                del moveList[-1]
                del moveList[-1]
                del moveList[-1]
                del moveList[-1]
    
    #Try doing a move and then R moves
    for x in xrange(1):
        if (cube[5]==cube[22] or (cube[5]==cube[40] and cube[37]==cube[22])
        or (cube[5]==cube[13] and cube[37]==cube[22])
        or (cube[5]==cube[31] and cube[37]==cube[22])
        or (cube[5]==cube[49] and cube[37]==cube[22])):
            break
        movesnow=[D,F,FPrime,F2,DPrime,D2,]
        for move in xrange(len(movesnow)):
            newcube=movesnow[move](cube)
            cube,List=getRightCrossPieceInPlace(newcube)
            if ((cube[5]==cube[22] or (cube[5]==cube[40] and cube[37]==cube[22])
            or (cube[5]==cube[13] and cube[37]==cube[22])
            or (cube[5]==cube[31] and cube[37]==cube[22]))
            or (cube[5]==cube[49] and cube[37]==cube[22])):
                moveList=moveList+[movesnow[move]]+List
                break
            cube=currentcube
    currentcube=cube
    
    #Three edges are in place ready to go
    #last step is finding the last edge

    if cube[32]==cube[22] or cube[30]==cube[22] or cube[41]==cube[22] or cube[48]==cube[22]:
        if cube[32]==cube[22] or cube[48]==cube[22]:
            alg=[LPrime,D,L,F2]
            for moves in xrange(len(alg)):
                newcube=alg[moves](cube)
                cube=newcube
                moveList+=[alg[moves]]
        else:
            alg=[R,DPrime,RPrime,F2]
            for moves in xrange(len(alg)):
                newcube=alg[moves](cube)
                cube=newcube
                moveList+=[alg[moves]]
    else:
        for x in xrange(4):
            if (cube[7]==cube[22] or (cube[7]==cube[13] and cube[10]==cube[22])
            or (cube[7]==cube[40] and cube[10]==cube[22])
            or (cube[7]==cube[31] and cube[10]==cube[22])
            or (cube[7]==cube[49] and cube[10]==cube[22])):
                break
            else:
                newcube=F(cube)
                cube=newcube
                moveList+=[F]
            if x==3:
                del moveList[-1]
                del moveList[-1]
                del moveList[-1]
                del moveList[-1]
                
        for x in xrange(1):
            if (cube[7]==cube[22] or (cube[7]==cube[13] and cube[10]==cube[22])
            or (cube[7]==cube[40] and cube[10]==cube[22])
            or (cube[7]==cube[31] and cube[10]==cube[22])
            or (cube[7]==cube[49] and cube[10]==cube[22])):
                break
            mnow=[D,DPrime,D2]
            for move in xrange(len(mnow)):
                newcube=mnow[move](cube)
                cube,List=getFrontCrossPieceInPlace(newcube)
                if (cube[7]==cube[22] or (cube[7]==cube[13] and cube[10]==cube[22])
                or (cube[7]==cube[40] and cube[10]==cube[22])
                or (cube[7]==cube[31] and cube[10]==cube[22])
                or (cube[7]==cube[49] and cube[10]==cube[22])):
                    moveList=moveList+[mnow[move]]+List
                    break
                cube=currentcube
    ###correctly orient edges on top
    if cube[1]!=cube[22] or cube[3]!=cube[22] or cube[5]!=cube[22] or cube[7]!=cube[22]:
        if cube[1]!=cube[22]:
            alg=[B,UPrime,L,U]
            for moves in xrange(len(alg)):
                newcube=alg[moves](cube)
                cube=newcube
                moveList+=[alg[moves]]
        if cube[3]!=cube[22]:
            alg=[L,UPrime,F,U]
            for moves in xrange(len(alg)):
                newcube=alg[moves](cube)
                cube=newcube
                moveList+=[alg[moves]]
        if cube[5]!=cube[22]:
            alg=[R,UPrime,B,U]
            for moves in xrange(len(alg)):
                newcube=alg[moves](cube)
                cube=newcube
                moveList+=[alg[moves]]
        if cube[7]!=cube[22]:
            alg=[F,UPrime,R,U]
            for moves in xrange(len(alg)):
                newcube=alg[moves](cube)
                cube=newcube
                moveList+=[alg[moves]]
                
    ##Time to make the cross :)           
    rightDone=0
    leftDone=0
    frontDone=0
    backDone=0
    if cube[37]==cube[40]:
        moveList+=[R2]
        cube=R2(cube)
        rightDone=1
    if cube[10]==cube[13]:
        moveList+=[F2]
        cube=F2(cube)
        frontDone=1
    if cube[46]==cube[49]:
        moveList+=[L2]
        cube=L2(cube)
        leftDone=1
    if cube[28]==cube[31]:
        moveList+=[B2]
        cube=B2(cube)
        backDone=1
    while rightDone==0 or frontDone==0 or leftDone==0 or backDone==0:
        cube=U(cube)
        moveList+=[U]
        if cube[37]==cube[40] and cube[5]==cube[22]:
            moveList+=[R2]
            cube=R2(cube)
            rightDone=1
        if cube[10]==cube[13] and cube[7]==cube[22]:
            moveList+=[F2]
            cube=F2(cube)
            frontDone=1
        if cube[46]==cube[49] and cube[3]==cube[22]:
            moveList+=[L2]
            cube=L2(cube)
            leftDone=1
        if cube[28]==cube[31] and cube[1]==cube[22]:
            moveList+=[B2]
            cube=B2(cube)
            backDone=1
    return cube,moveList

def getRightCrossPieceInPlace(cube):
    ##try doing R turns to move piece up
    List=[]
    for x in xrange(4):
        if ((cube[5]==cube[22] or (cube[5]==cube[40] and cube[37]==cube[22])
        or (cube[5]==cube[13] and cube[37]==cube[22])
        or (cube[5]==cube[31] and cube[37]==cube[22]))
        or (cube[5]==cube[49] and cube[37]==cube[22])):
            break
        else:
            newcube=R(cube)
            cube=newcube
            List+=[R]
            if x==3:
                List=[]
    return cube,List

def getRightCrossPieceInPlaceOnce(cube):
    ##try doing R turns to move piece up
    List=[]
    for x in xrange(4):
        if cube[5]==cube[22]:
            break
        else:
            newcube=R(cube)
            cube=newcube
            List+=[R]
            if x==3:
                List=[]
    return cube,List     


def getFrontCrossPieceInPlace(cube):
    ##try doing F turns to move piece up
    List=[]
    for x in xrange(4):
        if (cube[7]==cube[22] or (cube[7]==cube[13] and cube[10]==cube[22])
            or (cube[7]==cube[40] and cube[10]==cube[22])
            or (cube[7]==cube[31] and cube[10]==cube[22])
            or (cube[7]==cube[49] and cube[10]==cube[22])):
            break
        else:
            newcube=F(cube)
            cube=newcube
            List+=[F]
            if x==3:
                List=[]
    return cube,List


def solveFirstLayer(cube,moveList):
    FrontRight=False
    FrontLeft=False
    BackRight=False
    BackLeft=False
    
    if cube[20]==cube[22] and cube[17]==cube[13] and cube[42]==cube[40]:
        FrontRight=True
    if cube[18]==cube[22] and cube[15]==cube[13] and cube[53]==cube[49]:
        FrontLeft=True
    if cube[24]==cube[22] and cube[51]==cube[49] and cube[35]==cube[31]:
        BackLeft=True
    if cube[26]==cube[22] and cube[44]==cube[40] and cube[33]==cube[31]:
        BackRight=True
        
    
        
    ##look at  front top right corner, top left corner,  front top left corner, back top right corner, back top left corner
    
    ## see if a yellow corner on top layer
    ##if the following breaks, then there is a yellow corner on the top right corner
    ###

    count=0
    while FrontLeft==False or FrontRight==False or BackRight==False or BackLeft==False:
        for x in xrange(4):
            if cube[8]==cube[22] or cube[11]==cube[22] or cube[36]==cube[22]:
                count=0
                break
            cube=U(cube)
            moveList+=[U]
            count+=1
     ##the top right corner is a yellow corner

        if cube[8]==cube[22]:
        #bottom front right
            if cube[11]==cube[40] and cube[36]==cube[13]:
                cube,moveList=insertRightBottomFrontCorner(cube,moveList)
                FrontRight=True
            #bottom front left
            elif (cube[11]==cube[13] and cube[36]==cube[49]):
                cube=U(cube)
                moveList+=[U]
                cube,moveList=insertLeftBottomFrontCorner(cube,moveList)
                FrontLeft=True
                #bottom back left
            elif cube[11]==cube[49] and cube[36]==cube[31]:
                cube=U2(cube)
                moveList+=[U2]
                cube,moveList=insertLeftBottomBackCorner(cube,moveList)
                BackLeft=True
                #bottom back right
            elif cube[11]==cube[31] and cube[36]==cube[40]:
                cube=UPrime(cube)
                moveList+=[UPrime]
                cube,moveList=insertRightBottomBackCorner(cube,moveList)
                BackRight=True
        #So the there is not a yellow sticker on top but its on the right
        elif cube[36]==cube[22]:
                #front right
            if cube[8]==cube[40] and cube[11]==cube[13]:
                cube,moveList=insertRightBottomFrontCorner(cube,moveList)
                FrontRight=True
            #front left
            elif cube[8]==cube[13] and cube[11]==cube[49]:
                    cube=U(cube)
                    moveList+=[U]
                    cube,moveList=insertLeftBottomFrontCorner(cube,moveList)
                    FrontLeft=True
            #bottom back left
            elif cube[8]==cube[49] and cube[11]==cube[31]:
                cube=U2(cube)
                moveList+=[U2]
                cube,moveList=insertLeftBottomBackCorner(cube,moveList)
                BackLeft=True
            #bottom back right
            elif cube[8]==cube[31] and cube[11]==cube[40]:
                cube=UPrime(cube)
                moveList+=[UPrime]
                cube,moveList=insertRightBottomBackCorner(cube,moveList)
                BackRight=True
                
        elif cube[11]==cube[22]:
            
            if cube[8]==cube[13] and cube[36]==cube[40]:
                cube,moveList=insertRightBottomFrontCorner(cube,moveList)
                FrontRight=True
            #front left
            elif cube[8]==cube[49] and cube[36]==cube[13]:
                cube=U(cube)
                moveList+=[U]
                cube,moveList=insertLeftBottomFrontCorner(cube,moveList)
                FrontLeft=True
            #bottom back left
            elif cube[8]==cube[31] and cube[36]==cube[49]:
                cube=U2(cube)
                moveList+=[U2]
                cube,moveList=insertLeftBottomBackCorner(cube,moveList)
                BackLeft=True
            #bottom back right
            elif cube[8]==cube[40] and cube[36]==cube[31]:
                cube=UPrime(cube)
                moveList+=[UPrime]
                cube,moveList=insertRightBottomBackCorner(cube,moveList)
                BackRight=True

        ###Need to bring up corners at this point.
        if count>0:
            if FrontRight==False:
                alg=[R,U,RPrime]
                for move in xrange(len(alg)):
                    newcube=alg[move](cube)
                    moveList+=[alg[move]]
                    cube=newcube
            elif FrontLeft==False:
                alg=[LPrime,UPrime,L]
                for move in xrange(len(alg)):
                    newcube=alg[move](cube)
                    moveList+=[alg[move]]
                    cube=newcube
            elif BackRight==False:
                alg=[B,U,BPrime]
                for move in xrange(len(alg)):
                    newcube=alg[move](cube)
                    moveList+=[alg[move]]
                    cube=newcube
            elif BackLeft==False:
                alg=[BPrime,UPrime,B]
                for move in xrange(len(alg)):
                    newcube=alg[move](cube)
                    moveList+=[alg[move]]
                    cube=newcube
    return cube,moveList                
            #corner happens to be ready to go
            
        ##place it above the right corner for insertion
        
       # if cube[11]==cube[22]
      #  if cube[8]==cube[22]:
      
def insertRightBottomFrontCorner(cube,moveList):
    alg=[R,U,RPrime,UPrime]
    for x in xrange(5):
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
            if cube[20]==cube[22] and cube[17]==cube[13] and cube[42]==cube[40]:
                return cube,moveList
    return cube,moveList

def insertLeftBottomFrontCorner(cube,moveList):
    alg=[LPrime,UPrime,L,U]
    for x in xrange(5):
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
            if cube[18]==cube[22] and cube[15]==cube[13] and cube[53]==cube[49]:
                return cube,moveList
    return cube,moveList

def insertLeftBottomBackCorner(cube,moveList):
    alg=[BPrime,UPrime,B,U]
    for x in xrange(5):
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
            if cube[24]==cube[22] and cube[51]==cube[49] and cube[35]==cube[31]:
                 return cube,moveList
    return cube,moveList

def insertRightBottomBackCorner(cube,moveList):
    alg=[B,U,BPrime,UPrime]
    for x in xrange(5):
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
            if cube[26]==cube[22] and cube[44]==cube[40] and cube[33]==cube[31]:
                return cube,moveList
    return cube,moveList
    
            
#test=R(D(L(B2(F(U(R(Solution)))))))
#t#est2=U2(B(D(L2(R(F(U(Solution)))))))
test9=FPrime(L(F2(R(U(D(Solution))))))
test10=B2(L2(R(D(U(F(Solution))))))



def firstLayerDone(cube):
    if isCross(cube):
        if (cube[20]==cube[22] and cube[17]==cube[13] and cube[42]==cube[40] and
        cube[18]==cube[22] and cube[15]==cube[13] and cube[53]==cube[49] and
        cube[24]==cube[22] and cube[51]==cube[49] and cube[35]==cube[31] and
        cube[26]==cube[22] and cube[44]==cube[40] and cube[33]==cube[31]):
            return True
    return False
    
#cubed=["O","W","O","B","W","W","R","Y","W","Y","O","O","R","B","R","Y","O","R","R","W","B","O","Y",'Y','O','Y','R','B','B','Y','R','G','Y','W','G','Y',
  #     'G','G','W','G','O','W','W','B','G','G','O','G','R','R','B','B','G','B']
#print firstLayerDone(f[0])
#print firstLayerDone(cubed)


def solveSecondLayer(cube,moveList):
    frontRight=False
    frontLeft=False
    backRight=False
    backLeft=False
    
    if cube[14]==cube[13] and cube[39]==cube[40]:
        frontRight=True
    if cube[12]==cube[13] and cube[50]==cube[49]:
        frontLeft=True
    if cube[32]==cube[31] and cube[48]==cube[49]:
        backLeft=True
    if cube[30]==cube[31] and cube[41]==cube[40]:
        backRight=True
        
    while backRight==False or frontRight==False or frontLeft==False or backLeft==False:
    #FRONT RIGHT INSERTION
        switch=0
        for x in xrange(4):
            if cube[5]==cube[13] and cube[37]==cube[40] and frontRight==False:
                print "hi"
                cube,moveList=frontRightInsert(cube,moveList)
                frontRight=True
                switch=1
            elif cube[7]==cube[40] and cube[10]==cube[13] and frontRight==False:
                cube,moveList=frontRightInsertv2(cube,moveList)
                frontRight=True
                switch=1
    #FRONT LEFT INSERTION
            if cube[3]==cube[13] and cube[46]==cube[49] and frontLeft==False:
                cube,moveList=frontLeftInsert(cube,moveList)
                frontLeft=True
                switch=1
            elif cube[10]==cube[13] and cube[7]==cube[49] and  frontLeft==False:
                cube,moveList=frontLeftInsertv2(cube,moveList)
                frontLeft=True
                switch=1
    #BACK LEFT INSERTION
            if cube[3]==cube[31] and cube[46]==cube[49] and backLeft==False:
                cube,moveList=backLeftInsert(cube,moveList)
                backLeft=True
                switch=1
            elif cube[1]==cube[49] and cube[28]==cube[31] and backLeft==False:
                cube,moveList=backLeftInsertv2(cube,moveList)
                backLeft=True
                switch=1
    #BACK RIGHT INSERTION
            if cube[5]==cube[31] and cube[37]==cube[40] and backRight==False:
                cube,moveList=backRightInsert(cube,moveList)
                backRight=True
                switch=1
            elif cube[1]==cube[40] and cube[28]==cube[31] and backRight==False:
                cube,moveList=backRightInsertv2(cube,moveList)
                backRight=True
                switch=1
            cube=U(cube)
            moveList+=[U]
            
        ###Just in case if no middle edges are on the top layer
        #if ((cube[1]==cube[4] and cube[3]==cube[4] and cube[5]==cube[4] and cube[7]==cube[4] )or
        #(cube[28]==cube[4] and cube[37]==cube[4]  and cube[10]==cube[4] and cube[46]==cube[4]))::
        if switch==0:
            if frontLeft==False:
                alg=[LPrime,UPrime,L,U,F,U,FPrime]
                for move in xrange(len(alg)):
                    newcube=alg[move](cube)
                    moveList+=[alg[move]]
                    cube=newcube
            elif frontRight==False:
                alg=[R,U,RPrime,UPrime,FPrime,UPrime,F]
                for move in xrange(len(alg)):
                    newcube=alg[move](cube)
                    moveList+=[alg[move]]
                    cube=newcube
            elif backRight==False:
                alg=[B,U,BPrime,UPrime,RPrime,UPrime,R]
                for move in xrange(len(alg)):
                    newcube=alg[move](cube)
                    moveList+=[alg[move]]
                    cube=newcube
            elif backLeft==False:
                alg=[BPrime,UPrime,B,U,L,U,LPrime]
                for move in xrange(len(alg)):
                    newcube=alg[move](cube)
                    moveList+=[alg[move]]
                    cube=newcube
    return cube,moveList

def frontRightInsert(cube,moveList):
    alg=[UPrime,FPrime,U,F,U,R,UPrime,RPrime]
    for move in xrange(len(alg)):
        newcube=alg[move](cube)
        moveList+=[alg[move]]
        cube=newcube
    return cube,moveList

def frontRightInsertv2(cube,moveList):
    alg=[U,R,U,RPrime,UPrime,FPrime,UPrime,F]
    for move in xrange(len(alg)):
        newcube=alg[move](cube)
        moveList+=[alg[move]]
        cube=newcube
    return cube,moveList

def frontLeftInsert(cube,moveList):
    alg=[U,F,UPrime,FPrime,UPrime,LPrime,U,L]
    for move in xrange(len(alg)):
        newcube=alg[move](cube)
        moveList+=[alg[move]]
        cube=newcube
    return cube,moveList

def frontLeftInsertv2(cube,moveList):
    alg=[UPrime,LPrime,U,L,U,F,UPrime,FPrime]
    for move in xrange(len(alg)):
        newcube=alg[move](cube)
        moveList+=[alg[move]]
        cube=newcube
    return cube,moveList

def backLeftInsert(cube,moveList):
    alg=[UPrime,BPrime,U,B,U,L,UPrime,LPrime]
    for move in xrange(len(alg)):
        newcube=alg[move](cube)
        moveList+=[alg[move]]
        cube=newcube
    return cube,moveList

def backLeftInsertv2(cube,moveList):
    alg=[U,L,UPrime,LPrime,UPrime,BPrime,U,B]
    for move in xrange(len(alg)):
        newcube=alg[move](cube)
        moveList+=[alg[move]]
        cube=newcube
    return cube,moveList

def backRightInsert(cube,moveList):
    alg=[U,B,U,BPrime,UPrime,RPrime,UPrime,R]
    for move in xrange(len(alg)):
        newcube=alg[move](cube)
        moveList+=[alg[move]]
        cube=newcube
    return cube,moveList

def backRightInsertv2(cube,moveList):
    print "here"
    alg=[UPrime,RPrime,U,R,U,B,UPrime,BPrime]
    for move in xrange(len(alg)):
        newcube=alg[move](cube)
        moveList+=[alg[move]]
        cube=newcube
    return cube,moveList


def OLL(cube,moveList):
    edgesDone=False
    ##cross already done
    if cube[1]==cube[4] and cube[3]==cube[4] and cube[5]==cube[4] and cube[7]==cube[4]:
        edgesDone=True
    while edgesDone==False:
        if cube[3]==cube[4] and cube[5]==cube[4]:
            print "first"
            alg=[F,R,U,RPrime,UPrime,FPrime]
            for move in xrange(len(alg)):
                newcube=alg[move](cube)
                moveList+=[alg[move]]
                cube=newcube
            edgesDone=True
        elif cube[1]==cube[4] and cube[3]==cube[4]:
            alg=[F,R,U,RPrime,UPrime,FPrime,F,R,U,RPrime,UPrime,FPrime]
            for move in xrange(len(alg)):
                newcube=alg[move](cube)
                moveList+=[alg[move]]
                cube=newcube
            edgesDone=True
        elif cube[28]==cube[4] and cube[37]==cube[4] and cube[10]==cube[4] and cube[46]==cube[4]:
            alg=[F,R,U,RPrime,UPrime,FPrime,U2,F,R,U,RPrime,UPrime,FPrime,F,R,U,RPrime,UPrime,FPrime]
            for move in xrange(len(alg)):
                newcube=alg[move](cube)
                moveList+=[alg[move]]
                cube=newcube
            edgesDone=True
        cube=U(cube)
        moveList+=[U]
        #return cube,readableList(moveList)
    ####Cross on top at this point
    cornersDone=False
    if cube[0]==cube[4] and cube[2]==cube[4] and cube[6]==cube[4] and cube[8]==cube[4]:
        cornersDone==True
    while cornersDone==False:
        if cube[11]==cube[4] and cube[38]==cube[4] and cube[29]==cube[4]:
            alg=[R,U,RPrime,U,R,U2,RPrime]
            for move in xrange(len(alg)):
                newcube=alg[move](cube)
                moveList+=[alg[move]]
                cube=newcube
            if cube[0]==cube[4] and cube[2]==cube[4] and cube[6]==cube[4] and cube[8]==cube[4]:
                return cube,moveList
        elif cube[27]==cube[4] and cube[36]==cube[4] and cube[9]==cube[4]:
            alg=[RPrime,UPrime,R,UPrime,RPrime,U2,R]
            for move in xrange(len(alg)):
                newcube=alg[move](cube)
                moveList+=[alg[move]]
                cube=newcube
            if cube[0]==cube[4] and cube[2]==cube[4] and cube[6]==cube[4] and cube[8]==cube[4]:
                return cube,moveList
        elif cube[9]==cube[4] and cube[11]==cube[4] and cube[27]==cube[4] and cube[29]==cube[4]:
            alg=[F,R,U,RPrime,UPrime,R,U,RPrime,UPrime,R,U,RPrime,UPrime,FPrime]
            for move in xrange(len(alg)):
                newcube=alg[move](cube)
                moveList+=[alg[move]]
                cube=newcube
            if cube[0]==cube[4] and cube[2]==cube[4] and cube[6]==cube[4] and cube[8]==cube[4]:
                return cube,moveList
        elif cube[11]==cube[4] and cube[27]==cube[4] and cube[45]==cube[4] and cube[47]==cube[44]:
            alg=[R,U2,R2,UPrime,R2,UPrime,R2,U2,R]
            for move in xrange(len(alg)):
                newcube=alg[move](cube)
                moveList+=[alg[move]]
                cube=newcube
            if cube[0]==cube[4] and cube[2]==cube[4] and cube[6]==cube[4] and cube[8]==cube[4]:
                return cube,moveList
        elif cube[9]==cube[4] and cube[11]==cube[4]:
            alg=[R2,D,RPrime,U2,R,DPrime,RPrime,U2,RPrime]
            for move in xrange(len(alg)):
                newcube=alg[move](cube)
                moveList+=[alg[move]]
                cube=newcube
            if cube[0]==cube[4] and cube[2]==cube[4] and cube[6]==cube[4] and cube[8]==cube[4]:
                return cube,moveList
        elif cube[45]==cube[4] and cube[11]==cube[4]:
            alg=[FPrime,L,F,RPrime,FPrime,LPrime,F,R]
            for move in xrange(len(alg)):
                newcube=alg[move](cube)
                moveList+=[alg[move]]
                cube=newcube
            if cube[0]==cube[4] and cube[2]==cube[4] and cube[6]==cube[4] and cube[8]==cube[4]:
                return cube,moveList
        elif cube[9]==cube[4] and cube[29]==cube[4]:
            alg=[L,F,RPrime,FPrime,LPrime,F,R,FPrime]
            for move in xrange(len(alg)):
                newcube=alg[move](cube)
                moveList+=[alg[move]]
                cube=newcube
            if cube[0]==cube[4] and cube[2]==cube[4] and cube[6]==cube[4] and cube[8]==cube[4]:
                return cube,moveList
        cube=U(cube)
        moveList+=[U]

    
def PLL(cube,moveList):
    ##Do corners first
    
    ##keep doing U until you run into a case
    rightFront=False
    leftFront=False
    rightBack=False
    leftBack=False
    
    ####The right front corner is done
    if cube[11]==cube[13] and cube[36]==cube[40] and cube[8]==cube[4]:
        rightFront=True
    
    ##if its not done, keep doing U to get it so that its done
    while rightFront==False:
        cube=U(cube)
        moveList+=[U]
        if cube[11]==cube[13] and cube[36]==cube[40] and cube[8]==cube[4]:
            rightFront=True
            
            
    if cube[47]==cube[49] and cube[6]==cube[4] and cube[9]==cube[13]:
        leftFront=True
    if cube[2]==cube[4] and cube[27]==cube[31] and cube[38]==cube[40]:
        rightBack=True
    if cube[0]==cube[4] and cube[29]==cube[31] and cube[45]==cube[49]:
        leftBack=True
    
        
    ### if front two corners are done, make a U turn do T perm and then do UPrime
    if leftFront==True and rightFront==True and rightBack==False and leftBack==False:
        print "in here?"
        alg=[U,R,U,RPrime,UPrime,RPrime,F,R2,UPrime,RPrime,UPrime,R,U,RPrime,FPrime,UPrime]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
        leftFront=True
        rightBack=True
        leftBack=True
    
    ##front corners is done and back right corner is done. Do U2 do T Perm undo U2
        
    if rightBack==True and rightFront==True and leftFront==False and leftBack==False:
        print "should be in here"
        alg=[U2,R,U,RPrime,UPrime,RPrime,F,R2,UPrime,RPrime,UPrime,R,U,RPrime,FPrime,U2]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
        leftFront=True
        rightBack=True
        leftBack=True
    
        
    ##front is done and back left is done. Do U and do a t perm, do UPrime
        
    if rightFront==True and leftBack==True and rightBack==False and leftFront==False:
        alg=[U,R,U,RPrime,UPrime,RPrime,F,R2,UPrime,RPrime,UPrime,R,U,RPrime,FPrime,UPrime]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
    
        
    while leftFront==False or rightBack==False or leftBack==False:
        alg=[U2,R,BPrime,R,F2,RPrime,B,R,F2,R2,U2]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube        
        if (cube[47]==cube[49] and cube[6]==cube[4] and cube[9]==cube[13]
        and cube[0]==cube[4] and cube[29]==cube[31] and cube[45]==cube[49]
        and cube[2]==cube[4] and cube[27]==cube[31] and cube[38]==cube[40]):
            leftFront=True
            rightBack=True
            leftBack=True
            
    ##EDGES
    if cube[28]==cube[31] and cube[37]==cube[40] and cube[10]==cube[13] and cube[46]==cube[49]:
        return cube,moveList
    #Front done, counter clockwise 3 cycle
    if cube[10]==cube[13] and cube[28]==cube[49] and cube[46]==cube[40] and cube[37]==cube[31]:
        print "1"
        alg=[R2,UPrime,RPrime,UPrime,R,U,R,U,R,UPrime,R]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
            return cube,moveList
    #Front done, clockwise 3 cycle
    elif cube[10]==cube[13] and cube[28]==cube[40] and cube[46]==cube[31] and cube[37]==cube[49]:
        print "22"
        alg=[RPrime,U,RPrime,UPrime,RPrime,UPrime,RPrime,U,R,U,R2]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
        return cube,moveList
       ##Z PERM
    elif cube[10]==cube[40] and cube[28]==cube[49] and cube[46]==cube[31] and cube[37]==cube[13]:
        print "y"
        alg=[R,U,RPrime,U,RPrime,UPrime,RPrime,U,R,UPrime,RPrime,UPrime,R2,U,R,U2]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
        return cube,moveList
    ##H Perm
    elif cube[10]==cube[31] and cube[28]==cube[13] and cube[46]==cube[40] and cube[37]==cube[49]:
        print "3"
        alg=[R2 ,U2, R2, U2, R2, U ,R2, U2, R2, U2 ,R2 ,UPrime]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
        return cube,moveList
    ##Weird cases, just U turns of above cases
    elif cube[46]==cube[49] and cube[28]==cube[40] and cube[37]==cube[13] and cube[10]==cube[31]:
        alg=[UPrime,RPrime,U,RPrime,UPrime,RPrime,UPrime,RPrime,U,R,U,R2,U]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
        return cube,moveList
    elif cube[46]==cube[49] and cube[28]==cube[13] and cube[37]==cube[31] and cube[10]==cube[40]:
        alg=[UPrime,R2,UPrime,RPrime,UPrime,R,U,R,U,R,UPrime,R,U]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
        return cube,moveList
    
    elif cube[10]==cube[49] and cube[46]==cube[31] and cube[28]==cube[13] and cube[37]==cube[49]:
        alg=[U,RPrime,U,RPrime,UPrime,RPrime,UPrime,RPrime,U,R,U,R2,UPrime]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
        return cube,moveList
    
    elif cube[10]==cube[31] and cube[46]==cube[13] and cube[28]==cube[49] and cube[37]==cube[40]:
        print "should be herr"
        alg=[U,R2,UPrime,RPrime,UPrime,R,U,R,U,R,UPrime,R,UPrime]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
            return cube,moveList
    elif cube[10]==cube[49] and cube[46]==cube[40] and cube[28]==cube[31] and cube[37]==cube[13]:
        alg=[U2,RPrime,U,RPrime,UPrime,RPrime,UPrime,RPrime,U,R,U,R2,U2]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
        return cube,moveList
    
    elif cube[10]==cube[40] and cube[46]==cube[13] and cube[28]==cube[31] and cube[37]==cube[49]:
        print "1"
        alg=[U2,R2,UPrime,RPrime,UPrime,R,U,R,U,R,UPrime,R,U2]
        for move in xrange(len(alg)):
            newcube=alg[move](cube)
            moveList+=[alg[move]]
            cube=newcube
        return cube,moveList
    
    
            
    
                
        
    
    
        


#x=makeCross(test2)
#y=makeCross(test9)
#a=makeCross(test8)
#b=makeCross(cube)

def solveCube(cube):
    a=makeCross(cube)
    print "cross done"
    b=solveFirstLayer(a[0],a[1])
    print "first layer done"
    c=solveSecondLayer(b[0],b[1])
    print "second layer done"
    d=OLL(c[0],c[1])
    print "OLL Done"
    print  d[0]
    e=PLL(d[0],d[1])
    print "PLL Done"
    return e[1]


def applyMoves(cube,moves):
    for x in xrange(len(moves)):
        newcube=moves[x](cube)
        cube=newcube
    return cube
def isSecondLayerDone(cube):
    if isCross(cube)==True:
        if firstLayerDone(cube)==True:
            if cube[14]==cube[13] and cube[39]==cube[40]:
                pass
                if cube[12]==cube[13] and cube[50]==cube[49]:
                    pass
                if cube[32]==cube[31] and cube[48]==cube[49]:
                    pass
                    if cube[30]==cube[31] and cube[41]==cube[40]:
                        return True
    return False



def readableList(y):
    nL=[]
    for x in xrange(len(y)):
        s=str(y[x])
        i=s.index(" ")+1
        i2=s[i::].index(" ")
        nL.append(s[i:i+i2])
    return nL
    

import time
from Tkinter import *
import tkMessageBox
class solveScreen(object):
    def keyPressed(self,event):
        if (event.keysym == "f"):
            self.canvas.data.showhelpon=not self.canvas.data.showhelpon
            if self.canvas.data.showhelpon:
                self.canvas.b=self.canvas.create_text(165,100,text="BACK",font=("Helvetica", 12, "bold"))
                self.canvas.l=self.canvas.create_text(75,200,text="LEFT",font=("Helvetica", 12, "bold"))
                self.canvas.t=self.canvas.create_text(165,200,text="TOP",font=("Helvetica", 12, "bold"))
                self.canvas.r=self.canvas.create_text(250,200,text="RIGHT",font=("Helvetica", 12, "bold"))
                self.canvas.d=self.canvas.create_text(350,200,text="DOWN",font=("Helvetica", 12, "bold"))
                self.canvas.f=self.canvas.create_text(165,280,text="FRONT",font=("Helvetica", 12, "bold"))
            else:    
                self.canvas.delete(self.canvas.b)
                self.canvas.delete(self.canvas.l)
                self.canvas.delete(self.canvas.t)
                self.canvas.delete(self.canvas.r)
                self.canvas.delete(self.canvas.d)
                self.canvas.delete(self.canvas.f)
        if event.keysym=="i":
            text = """ Please begin by using your mouse to paint the empty cube to your left.
                    Input each face as you would look at it from the front"""
            title = "Welcome to Aditya's Rubiks cube solver"
            tkMessageBox.showinfo(title, text)
            #self.canvas.data.givencube=54*[0]
            
        
    def mousePressed(self,event):
        (self.canvas.data.x,self.canvas.data.y)=(event.x, event.y)
        if self.canvas.data.showhelpon==False and self.canvas.data.statesentered==False:
            if 525<self.canvas.data.x<575 and 325<self.canvas.data.y<375:
                self.currentColor("Blue")
                self.canvas.data.pickedcolor="Blue"
            if 525<self.canvas.data.x<575 and 400<self.canvas.data.y<450:
                self.currentColor("Red")
                self.canvas.data.pickedcolor="Red"
            if 525<self.canvas.data.x<575 and 475<self.canvas.data.y<525:
                self.currentColor("Green")
                self.canvas.data.pickedcolor="Green"
            if 600<self.canvas.data.x<650 and 325<self.canvas.data.y<375:
                self.currentColor("Orange")
                self.canvas.data.pickedcolor="Orange"
            if 600<self.canvas.data.x<650 and 400<self.canvas.data.y<450:
                self.currentColor("Yellow")
                self.canvas.data.pickedcolor="Yellow"
            if 600<self.canvas.data.x<650 and 475<self.canvas.data.y<525:
                self.currentColor("White")
                self.canvas.data.pickedcolor="White"
            self.paintTopFace(self.canvas.data.x,self.canvas.data.y)
            self.paintRightFace(self.canvas.data.x,self.canvas.data.y)
            self.paintDownFace(self.canvas.data.x,self.canvas.data.y)
            self.paintFrontFace(self.canvas.data.x,self.canvas.data.y)
            self.paintLeftFace(self.canvas.data.x,self.canvas.data.y)
            self.paintBackFace(self.canvas.data.x,self.canvas.data.y)
    def run(self,rows,cols):
    
    # create the root and the canvas
        root = Tk()
        margin = 5
        cellSize = 40
        canvasWidth = 10*margin + cols*cellSize
        canvasHeight = 10*margin + rows*cellSize
        self.canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
        self.canvas.pack()
        root.resizable(width=0, height=0)
    # Store canvas in root and in canvas itself for callbacks
        root.canvas = self.canvas.canvas = self.canvas
    # Set up canvas data and call init
        class Struct: pass
        self.canvas.data = Struct()
        self.canvas.data.pickedcolor="White"
        self.canvas.data.width=canvasWidth
        self.canvas.data.height=canvasHeight
        self.canvas.data.margin = margin
        self.canvas.data.cellSize = cellSize
        self.canvas.data.rows = rows
        self.canvas.data.cols = cols
        self.init()
        root.bind("<Button-1>", lambda event: self.mousePressed(event))
        root.bind("<Key>", lambda event: self.keyPressed(event))
        b2 = Button(self.canvas, text="Cube entered", command=self.button1Pressed)
        self.canvas.create_window(300, 300, window=b2)
        root.mainloop()
    def button1Pressed(self):
        if 0 in self.canvas.data.givencube:
            message = "Please fill in the configuration of your cube"
            title = "Caution"
            tkMessageBox.showwarning(title, message)
        else:
            self.canvas.data.statesentered=True
            b3 = Button(self.canvas, text="Click for next move in solution", command=self.nextPressed)
            self.canvas.create_window(160, 380, window=b3)
            copycube=self.canvas.data.givencube
            self.canvas.data.solution=solveCube(copycube)
            self.canvas.data.readablesolution=readableList(self.canvas.data.solution)
            self.movedisplay=self.canvas.create_text(0,0, text="o", font=("Helvetica", 0, "bold"))
            self.movecounter=self.canvas.create_text(0,0, text="o", font=("Helvetica", 0, "bold"))
        
        
    def nextPressed(self):
        self.canvas.delete(self.movecounter)
        self.canvas.delete(self.movedisplay)
        cxx = self.canvas.data.width/4
        cyy= self.canvas.data.height/4
        self.canvas.create_text(cxx+200,cyy+220, text="Next move:", font=("Helvetica", 14, "bold"))
        self.canvas.create_text(cxx+200,cyy+280, text="Number of Moves made:", font=("Helvetica", 14, "bold"))
        if self.canvas.data.moveindex<len(self.canvas.data.solution):        
            self.movedisplay=self.canvas.create_text(cxx+200,cyy+250, text=self.canvas.data.readablesolution[self.canvas.data.moveindex], font=("Helvetica", 15, "bold"))
            self.movecounter=self.canvas.create_text(cxx+200,cyy+300, text=self.canvas.data.moveindex+1, font=("Helvetica", 15, "bold"))
            self.canvas.data.givencube=self.canvas.data.solution[self.canvas.data.moveindex](self.canvas.data.givencube)
            self.canvas.data.fillList=self.canvas.data.solution[self.canvas.data.moveindex](self.canvas.data.fillList)
            self.makeCube()
            self.canvas.data.moveindex+=1
        
                
    def redrawAll(self):
        cx = self.canvas.data.width/2
        cy = self.canvas.data.height/2
        self.canvas.create_text(cx+0.1*self.canvas.data.width, cy-0.4*self.canvas.data.height, text="Rubik's Cube Solver", font=("Helvetica", 18, "bold"))
        self.canvas.create_text(cx+0.1*self.canvas.data.width, cy-0.45*self.canvas.data.height, text="Press i for help", font=("Helvetica", 14, "bold"))
        self.canvas.create_text(cx+0.1*self.canvas.data.width, cy-0.3*self.canvas.data.height, text="Press f to toggle face displays", font=("Helvetica", 14, "bold"))
        self.drawColorPallettes()
        self.currentColor(self.canvas.data.pickedcolor)
        self.makeCube()
    
    def currentColor(self,color):
        cx = self.canvas.data.width/2
        cy = self.canvas.data.height/2
        self.canvas.create_text(cx+230,cy-120, text="Current Selected Color", font=("Helvetica", 12, "bold"))
        self.canvas.create_rectangle(cx+240,cy-100,cx+290,cy-50,fill=color)
    
    def init(self):
        self.canvas.data.givencube=54*[0]
        self.canvas.data.fillList=[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
        self.canvas.data.moveindex=0
        self.canvas.data.showhelpon=False
        self.canvas.data.statesentered=False
        self.redrawAll()
        
    def makeCube(self):
        cxx = self.canvas.data.width/4
        cyy= self.canvas.data.height/4
        fillList=self.canvas.data.fillList

        self.LeftFace(cxx,cyy)
        self.TopFace(cxx,cyy)
        self.RightFace(cxx,cyy)
        self.DownFace(cxx,cyy)
        self.FrontFace(cxx,cyy)
        self.BackFace(cxx,cyy)
        
    def paintTopFace(self,x,y):
    ###TOP FACE
        if 117<x<147 and 147<y<177:
            self.canvas.data.fillList[0]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[0]=self.canvas.data.pickedcolor[0]
            self.makeCube()
            
        if 147<x<177 and 147<y<177:
            self.canvas.data.fillList[1]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[1]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 177<x<207 and 147<y<177:
            self.canvas.data.fillList[2]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[2]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        
        if 117<x<147 and 177<y<207:
            self.canvas.data.fillList[3]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[3]=self.canvas.data.pickedcolor[0]
            self.makeCube()
            
        if 147<x<177 and 177<y<207:
            self.canvas.data.fillList[4]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[4]=self.canvas.data.pickedcolor[0]
            self.makeCube()
            
        if 177<x<207 and 177<y<207:
            self.canvas.data.fillList[5]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[5]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        
        if 117<x<147 and 207<y<237:
            self.canvas.data.fillList[6]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[6]=self.canvas.data.pickedcolor[0]
            self.makeCube()
            
        if 147<x<177 and 207<y<237:
            self.canvas.data.fillList[7]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[7]=self.canvas.data.pickedcolor[0]
            self.makeCube()
            
        if 177<x<207 and 207<y<237:
            self.canvas.data.fillList[8]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[8]=self.canvas.data.pickedcolor[0]
            self.makeCube()
            
    def paintRightFace(self,x,y):
        if 212<x<242 and 147<y<177:
            self.canvas.data.fillList[36]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[36]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 212<x<242 and 177<y<207:
            self.canvas.data.fillList[39]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[39]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 212<x<242 and 207<y<237:
            self.canvas.data.fillList[42]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[42]=self.canvas.data.pickedcolor[0]
            self.makeCube()    
        if 242<x<272 and 147<y<177:
            self.canvas.data.fillList[37]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[37]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 242<x<272 and 177<y<207:
            self.canvas.data.fillList[40]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[40]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 242<x<272 and 207<y<237:
            self.canvas.data.fillList[43]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[43]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 272<x<302 and 147<y<177:
            self.canvas.data.fillList[38]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[38]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 272<x<302 and 177<y<207:
            self.canvas.data.fillList[41]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[41]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 272<x<302 and 207<y<237:
            self.canvas.data.fillList[44]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[44]=self.canvas.data.pickedcolor[0]
            self.makeCube()
    def paintDownFace(self,x,y):
    ###Down Face
        if 307<x<337 and 147<y<177:
            self.canvas.data.fillList[18]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[18]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 307<x<337 and 177<y<207:
            self.canvas.data.fillList[21]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[21]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 307<x<337 and 207<y<237:
            self.canvas.data.fillList[24]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[24]=self.canvas.data.pickedcolor[0]
            self.makeCube()    
        if 337<x<367 and 147<y<177:
            self.canvas.data.fillList[19]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[19]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 337<x<367 and 177<y<207:
            self.canvas.data.fillList[22]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[22]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 337<x<367 and 207<y<237:
            self.canvas.data.fillList[25]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[25]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 367<x<397 and 147<y<177:
            self.canvas.data.fillList[20]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[20]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 367<x<397 and 177<y<207:
            self.canvas.data.fillList[23]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[23]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 367<x<397 and 207<y<237:
            self.canvas.data.fillList[26]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[26]=self.canvas.data.pickedcolor[0]
            self.makeCube()
    def paintLeftFace(self,x,y):
        if 22<x<52 and 147<y<177:
            self.canvas.data.fillList[45]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[45]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        
        if 22<x<52 and 177<y<207:
            self.canvas.data.fillList[48]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[48]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        
        if 22<x<52 and 207<y<237:
            self.canvas.data.fillList[51]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[51]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        
        if 52<x<82 and 147<y<177:
            self.canvas.data.fillList[46]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[46]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        
        if 52<x<82 and 177<y<207:
            self.canvas.data.fillList[49]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[49]=self.canvas.data.pickedcolor[0]
            self.makeCube()
    
        if 52<x<82 and 207<y<237:
            self.canvas.data.fillList[52]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[52]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        
        if 82<x<112 and 147<y<177:
            self.canvas.data.fillList[47]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[47]=self.canvas.data.pickedcolor[0]
            self.makeCube()
            
        if 82<x<112 and 177<y<207:
            self.canvas.data.fillList[50]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[50]=self.canvas.data.pickedcolor[0]
            self.makeCube()
            
        if 82<x<112 and 207<y<237:
            self.canvas.data.fillList[53]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[53]=self.canvas.data.pickedcolor[0]
            self.makeCube()
    def paintBackFace(self,x,y):
        if 117<x<147 and 52<y<82:
            self.canvas.data.fillList[27]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[27]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 147<x<177 and 52<y<82:
            self.canvas.data.fillList[28]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[28]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 177<x<207 and 52<y<82:
            self.canvas.data.fillList[29]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[29]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        
        if 117<x<147 and 82<y<112:
            self.canvas.data.fillList[30]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[30]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 147<x<177 and 82<y<112:
            self.canvas.data.fillList[31]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[31]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 177<x<217 and 82<y<112:
            self.canvas.data.fillList[32]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[32]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        
        if 117<x<147 and 112<y<142:
            self.canvas.data.fillList[33]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[33]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 147<x<177 and 112<y<142:
            self.canvas.data.fillList[34]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[34]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 177<x<207 and 112<y<142:
            self.canvas.data.fillList[35]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[35]=self.canvas.data.pickedcolor[0]
            self.makeCube()
    

    def paintFrontFace(self,x,y):
        if 117<x<147 and 242<y<272:
            self.canvas.data.fillList[9]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[9]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 147<x<177 and 242<y<272:
            self.canvas.data.fillList[10]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[10]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 177<x<207 and 242<y<272:
            self.canvas.data.fillList[11]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[11]=self.canvas.data.pickedcolor[0]
            self.makeCube()
            
        if 117<x<147 and 272<y<302:
            self.canvas.data.fillList[12]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[12]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 147<x<177 and 272<y<302:
            self.canvas.data.fillList[13]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[13]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 177<x<207 and 272<y<302:
            self.canvas.data.fillList[14]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[14]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        
        if 117<x<147 and 302<y<332:
            self.canvas.data.fillList[15]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[15]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 147<x<177 and 302<y<332:
            self.canvas.data.fillList[16]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[16]=self.canvas.data.pickedcolor[0]
            self.makeCube()
        if 177<x<207 and 302<y<332:
            self.canvas.data.fillList[17]=self.canvas.data.pickedcolor
            self.canvas.data.givencube[17]=self.canvas.data.pickedcolor[0]
            self.makeCube()
    def LeftFace(self,cxx,cyy):
    ###Left Face
        fillList=self.canvas.data.fillList
        self.canvas.create_rectangle(cxx-140,cyy-15,cxx-110,cyy+15,fill=fillList[45])
        self.canvas.create_rectangle(cxx-140,cyy+15,cxx-110,cyy+45,fill=fillList[48])
        self.canvas.create_rectangle(cxx-140,cyy+45,cxx-110,cyy+75,fill=fillList[51])
    
        self.canvas.create_rectangle(cxx-110,cyy-15,cxx-80,cyy+15,fill=fillList[46])
        self.canvas.create_rectangle(cxx-110,cyy+15,cxx-80,cyy+45,fill=fillList[49])
        self.canvas.create_rectangle(cxx-110,cyy+45,cxx-80,cyy+75,fill=fillList[52])
    
        self.canvas.create_rectangle(cxx-80,cyy-15,cxx-50,cyy+15,fill=fillList[47])
        self.canvas.create_rectangle(cxx-80,cyy+15,cxx-50,cyy+45,fill=fillList[50])
        self.canvas.create_rectangle(cxx-80,cyy+45,cxx-50,cyy+75,fill=fillList[53])

    def TopFace(self,cxx,cyy):
    ####Top Face
        fillList=self.canvas.data.fillList
        self.canvas.create_rectangle(cxx-45,cyy-15,cxx-15,cyy+15,fill=fillList[0])
        self.canvas.create_rectangle(cxx-15,cyy-15,cxx+15,cyy+15,fill=fillList[1])
        self.canvas.create_rectangle(cxx+15,cyy-15,cxx+45,cyy+15,fill=fillList[2])
    
        self.canvas.create_rectangle(cxx-45,cyy+15,cxx-15,cyy+45,fill=fillList[3])
        self.canvas.create_rectangle(cxx-15,cyy+15,cxx+15,cyy+45,fill=fillList[4])
        self.canvas.create_rectangle(cxx+15,cyy+15,cxx+45,cyy+45,fill=fillList[5])

    
        self.canvas.create_rectangle(cxx-45,cyy+45,cxx-15,cyy+75,fill=fillList[6])
        self.canvas.create_rectangle(cxx-15,cyy+45,cxx+15,cyy+75,fill=fillList[7])
        self.canvas.create_rectangle(cxx+15,cyy+45,cxx+45,cyy+75,fill=fillList[8])
    
    def RightFace(self,cxx,cyy):
    ###################### Right Face
        fillList=self.canvas.data.fillList
        self.canvas.create_rectangle(cxx+50,cyy-15,cxx+80,cyy+15,fill=fillList[36])
        self.canvas.create_rectangle(cxx+50,cyy+15,cxx+80,cyy+45,fill=fillList[39])
        self.canvas.create_rectangle(cxx+50,cyy+45,cxx+80,cyy+75,fill=fillList[42])
    
        self.canvas.create_rectangle(cxx+80,cyy-15,cxx+110,cyy+15,fill=fillList[37])
        self.canvas.create_rectangle(cxx+80,cyy+15,cxx+110,cyy+45,fill=fillList[40])
        self.canvas.create_rectangle(cxx+80,cyy+45,cxx+110,cyy+75,fill=fillList[43])
    
        self.canvas.create_rectangle(cxx+110,cyy-15,cxx+140,cyy+15, fill=fillList[38])
        self.canvas.create_rectangle(cxx+110,cyy+15,cxx+140,cyy+45, fill=fillList[41])
        self.canvas.create_rectangle(cxx+110,cyy+45,cxx+140,cyy+75,fill=fillList[44])
        
    def DownFace(self,cxx,cyy):
    ######################### Down Face
        fillList=self.canvas.data.fillList
        self.canvas.create_rectangle(cxx+145,cyy-15,cxx+175,cyy+15,fill=fillList[18])
        self.canvas.create_rectangle(cxx+145,cyy+15,cxx+175,cyy+45,fill=fillList[21])
        self.canvas.create_rectangle(cxx+145,cyy+45,cxx+175,cyy+75,fill=fillList[24])
    
        self.canvas.create_rectangle(cxx+175,cyy-15,cxx+205,cyy+15,fill=fillList[19])
        self.canvas.create_rectangle(cxx+175,cyy+15,cxx+205,cyy+45,fill=fillList[22])
        self.canvas.create_rectangle(cxx+175,cyy+45,cxx+205,cyy+75,fill=fillList[25])
    
        self.canvas.create_rectangle(cxx+205,cyy-15,cxx+235,cyy+15,fill=fillList[20])
        self.canvas.create_rectangle(cxx+205,cyy+15,cxx+235,cyy+45,fill=fillList[23])
        self.canvas.create_rectangle(cxx+205,cyy+45,cxx+235,cyy+75,fill=fillList[26])
    
    

    ####################
    def FrontFace(self,cxx,cyy):
        ###Front Face
        fillList=self.canvas.data.fillList
        self.canvas.create_rectangle(cxx-45,cyy+80,cxx-15,cyy+110,fill=fillList[9])#cube
        self.canvas.create_rectangle(cxx-15,cyy+80,cxx+15,cyy+110,fill=fillList[10])#cube[10] fill
        self.canvas.create_rectangle(cxx+15,cyy+80,cxx+45,cyy+110,fill=fillList[11])#cube[11] fill

        self.canvas.create_rectangle(cxx-45,cyy+110,cxx-15,cyy+140,fill=fillList[12])#cube[12] fill
        self.canvas.create_rectangle(cxx-15,cyy+110,cxx+15,cyy+140,fill=fillList[13])#cube[13] fill
        self.canvas.create_rectangle(cxx+15,cyy+110,cxx+45,cyy+140,fill=fillList[14])#cube[14] fill
    
        self.canvas.create_rectangle(cxx-45,cyy+140,cxx-15,cyy+170,fill=fillList[15]) #cube[15] fill
        self.canvas.create_rectangle(cxx-15,cyy+140,cxx+15,cyy+170,fill=fillList[16]) #cube[16] fill
        self.canvas.create_rectangle(cxx+15,cyy+140,cxx+45,cyy+170,fill=fillList[17])  #cube[17] fill

    def BackFace(self,cxx,cyy):
    ###Back face
        fillList=self.canvas.data.fillList
        self.canvas.create_rectangle(cxx-45,cyy-110,cxx-15,cyy-80,fill=fillList[27])
        self.canvas.create_rectangle(cxx-15,cyy-110,cxx+15,cyy-80,fill=fillList[28])
        self.canvas.create_rectangle(cxx+15,cyy-110,cxx+45,cyy-80,fill=fillList[29])
    
        self.canvas.create_rectangle(cxx-45,cyy-80,cxx-15,cyy-50,fill=fillList[30])
        self.canvas.create_rectangle(cxx-15,cyy-80,cxx+15,cyy-50,fill=fillList[31])
        self.canvas.create_rectangle(cxx+15,cyy-80,cxx+45,cyy-50,fill=fillList[32])

        self.canvas.create_rectangle(cxx-45,cyy-50,cxx-15,cyy-20,fill=fillList[33])
        self.canvas.create_rectangle(cxx-15,cyy-50,cxx+15,cyy-20,fill=fillList[34])
        self.canvas.create_rectangle(cxx+15,cyy-50,cxx+45,cyy-20,fill=fillList[35])
    
    def drawColorPallettes(self):
        cx = self.canvas.data.width/2
        cy = self.canvas.data.height/2
    
        self.canvas.create_rectangle(cx+200,cy,cx+250,cy+50,fill="blue")
        self.canvas.create_rectangle(cx+200,cy+75,cx+250,cy+125,fill="red")   
        self.canvas.create_rectangle(cx+200,cy+150,cx+250,cy+200,fill="green")
        self.canvas.create_rectangle(cx+275,cy,cx+320,cy+50,fill="orange")
        self.canvas.create_rectangle(cx+275,cy+75,cx+320,cy+125,fill="yellow")
        self.canvas.create_rectangle(cx+275,cy+150,cx+320,cy+200,fill="white")
            
    
    
    

s=solveScreen()
s.run(15,15)
    
    
    

    
    
    
    

    
   # ['Y', 'W', 'W', 'R', 'W', 'W', 'R', 'Y', 'O', 'Y', 'O', 'B', 'Y', 'B', 'R', 'Y', 'B', 'W', 'O', 'O', 'B', 'O', 'Y', 'O', 'O', 'B', 'W', 'B', 'G', 'B', 'R', 'G', 'R', 'G', 'Y', 'W', 'Y', 'B', 'R', 'B', 'O', 'Y', 'O', 'W', 'R', 'R', 'G', 'G', 'W', 'R', 'G', 'G', 'G', 'G']

    



