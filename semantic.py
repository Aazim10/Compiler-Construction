from finalLex import tokenlist
from seFunction import (
    scopeError,
    ptypeError,
    declarationError,
    highestScope,
    insertenumconst,
    createScope,
    destroyScope,
    insertAttribute,
    insertFunctionTable,
    insertMainTable,
    lookupAttributeTable,
    lookupFunctionTable,
    lookupMainTable,
    scopeStack_,
    binTypeCompatible,
    uniTypeCompatible,
    mainTable_,
    functionTable_,
    redeclarationError,
    destroyScope,
    lookupAttributeForType,
    typeMISmatchError,
    lookupAttributeForTypeDetail,
    lookupAttributeForFuncTypeDetail
)
from inspect import currentframe, getframeinfo


error = ""
errorList = []
currentFunction = 0
currentScope = 0
tokenType = []
tokenValue = []
i = 0
currentClass = ""
mainTableTypeMOD = ""
multipleInterface = []
extendingClass = ""
mainTableType = ""
enumlist = []
accessMODvalue = ""
isStatic = False
isFinal = False
isAbstract = False
signature = []
argsList = []
isFunc = False
for line in tokenlist:
    tokenType.append(line[0])
    tokenValue.append(line[1])

tokenType.append("EOF")
tokenValue.append("EOF")

print(tokenType)


def clearAccesandNonAccess():
    global accessMODvalue, isStatic, isFinal, isAbstract
    accessMODvalue = ""
    isStatic = False
    isFinal = False
    isAbstract = False


def calclateLineNo(itr):
    # allLines[itr] = allLines[itr].replace("(", "")
    # allLines[itr] = allLines[itr].replace(")", "")
    # theLine = tokenlist[itr].split(",")
    return tokenlist[itr][-1]


def errorMesssage(itr):
    errorString = (
        "invalid syntax at line :",
        calclateLineNo(itr),
        "the token : ",
        tokenlist[itr]
        # "after ",
        # allLines[itr + 1],
        # "before r ",
        # allLines[itr - 1],
    )
    errorList.append(errorString)

    # print('invalid syntax at line :' , calclateLineNo(itr) , 'the token : ', allLines[itr])


# --------------------
# resultFile = open("result.txt")

# a = resultFile.read()
# allLines = a.split("\n")
# tokenType = []
# tokenLine = []

# for line in allLines:
#     splitted = line.split(",")
#     if len(splitted) > 2:
#         tokenType.append(splitted[0])
#         tokenValue.append(splitted[1])

# tokenType.append("EOF")
# tokenValue.append("EOF")
# print("<<<<<<<<<<<<<<<<<<<<<<<<<EXTRAS START>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(tokenType)
# print("<<<<<<<<<<<<<<<<<<<<<<<<<EXTRAS END>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def MVA():
    global i, tokenType
    if func_def():
        return True
    elif Decl():
        return True
    elif abs_func_def():
        return True
    elif construct_def():
        return True
    else:
        return False


def MVC():
    global i, tokenType
    if func_def():
        return True
    elif Decl():
        return True
    elif construct_def():
        return True
    else:
        return False


def AM():
    global i, tokenType
    if tokenType[i] == "public":
        i = i + 1
        return True
    elif tokenType[i] == "private":
        i = i + 1
        return True
    else:
        return True


def NAMS():
    global i, tokenType, isStatic
    if tokenType[i] == "static":
        isStatic = True
        i = i + 1
        return True
    else:
        return True


def TSD():
    global i, tokenType
    chk, tsss = TS()
    if chk:
        print("TSSSSSS true")
        if tokenType[i] == "dot":
            i = i + 1
            return True
        else:
            print(tokenType[i], tokenValue[i])
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        print("tsd false")
        return False


def for_B():
    global i, tokenType
    if tokenType[i] == "equals":
        i = i + 1
        chk , tyoo= Exp()
        if chk:
            return True
        else:
            return False
    elif tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            i = i + 1
            if for_B():
                return True
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    elif tokenType[i] == "incDec":
        i = i + 1
        return True
    elif tokenType[i] == "openroundbrace":
        i = i + 1
        if Args():
            if tokenType[i] == "closeroundbrace":
                i = i + 1
                if FNB():
                    return True
                else:
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            return False
    elif tokenType[i] == "opensquarebrace":
        i = i + 1
        chk , tyoo= Exp()
        if chk:
            if tokenType[i] == "closesquarebrace":
                i = i + 1
                if D2DA():
                    if Ref2():
                        if ETExp():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False


def FNB():
    global i, tokenType
    if tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            i = i + 1
            if for_B():
                return True
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def Ref2():
    global i, tokenType
    if tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            i = i + 1
            if for_B():
                return True
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return True


def ETExp():
    global i, tokenType
    if tokenType[i] == "equals":
        i = i + 1
        chk , tyoo= Exp()
        if chk:
            return True
        else:
            return False
    else:
        return False


def mStringConst():
    global i, tokenType, enumlist
    if tokenType[i] == "comma":
        i = i + 1
        if tokenType[i] == "stringConst":
            enumlist.append(tokenValue[i])
            i = i + 1
            if mStringConst():
                return True
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return True


def TRAS():
    global i, tokenType, currentClass
    print("IN TRASSSSSSS 3333333333", tokenValue[i])
    if TSD():
        print("TSD TRUEEEEEEEEEE", errorList)

        if tokenType[i] == "identifier":
            first = tokenValue[i]
            print("IN TRASSSSSSSSSSSSSSS")
            i = i + 1
            chk, tyoe = MAS(first)
            print("MAS AER", tyoe, first)
            if chk:
                return True, tyoe
            else:
                return False, "null"
        else:
            print("idFALSE", errorList)
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False, "null"
    elif tokenType[i] == "identifier":

        first = tokenValue[i]
        print("IN TRASSSSSSSSSSSSSSS", first)
        i = i + 1
        chk, tyoe = MAS(first)
        # if tyoe not in []:
        print("MAS AER", tyoe)
        # chkss = lookupFunctionTable(tyoe)
        # print("chks after function table___________", chkss)
        # if chkss == False:
        #     chkss = lookupAttributeForType(first, currentClass)
        # print(" in trasssssssss 00000000000000000", tyoe, chkss)
        if chk:
            # if check:
            return True, tyoe
        else:
            # errorList.append(declarationError(first))
            return False, "null"
    else:
        print("tras false")
        return False, "null"


def D2DA():
    global i, tokenType
    if tokenType[i] == "opensquarebrace":
        i = i + 1
        chk , tyoo= Exp()
        if chk:
            if tokenType[i] == "closesquarebrace":
                i = i + 1
                return True
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return True


def ADT(value):
    global i, tokenType, currentClass
    print("in ADT ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,", value, ";")
    if tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            if value == "this":
                tup = lookupAttributeForType(tokenValue[i], currentClass)
                if(tup==False):
                    sms = tokenType[i] +"Doesnot exist in current class"
                    errorList.append(sms)
                    return False
                print("##################### this match", tup)
            else:
                print("##################### super match")
                print("is super")
            i = i + 1
            # return True, tup
            chekerr, typpo = B(tup)
            if chekerr:
                return True
            else:
                return False
        else:
            print("the adt false $$$$$$$$$$$$$$$$$$$")
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    elif tokenType[i] == "openroundbrace":
        i = i + 1
        if Args():
            if tokenType[i] == "closeroundbrace":
                i = i + 1
                if tokenType[i] == "terminator":
                    i = i + 1
                    return True
                else:
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False


def TS():
    global i, tokenType
    print("IN TS", tokenType[i])
    if tokenType[i] in ["this"]:
        print(tokenType[i])
        i = i + 1
        return True, "this"
    elif tokenType[i] in ["super"]:
        i = i + 1
        return True, "super"
    else:
        print("ts false")
        return False, "null"


# def TAssign_st():
#     global i, tokenType
#     chk, value = TS()
#     if chk:
#         print("after ts", value)
#         chker = ADT(value)
#         if chker:
#             return True
#         else:
#             return False
#     else:
#         return False


def AOE():
    global i, tokenType
    if tokenType[i] == "equals":
        i=i+1
        chk , dt= Exp()
        print("TYOE IN ECPPPPPPPPP",dt)
        if chk:
            return True,dt
        else:
            return False,"null"
    elif  tokenType[i] == "openroundbrace":
        i=i+1
        if Args():
            if tokenType[i] == "closeroundbrace":
                i=i+1
                return True
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False

def RTS(value):
    global i, tokenType,currentClass
    if tokenType[i] == "dot":
        i = i + 1
        print("-----------IN TASSIGN ********************8",tokenType[i])
        typppp = ""
        if tokenType[i] == "identifier":
            cvar= tokenValue[i]
            i=i+1
            if value=="this":
                typppp = lookupAttributeForType(cvar,currentClass)
                print("**********TYPPPP",typppp)
                if typppp ==False:
                    sms = cvar + " doesnot exist in current class"
                    errorList.append(sms)
                    return False
                print('lok')
            elif value == "super":
                if extendingClass != "":
                    typppp = lookupAttributeForType(cvar,extendingClass)
                    if typppp ==False:
                        sms = cvar + " doesnot exist in parent class"
                        errorList.append(sms)
                        return False
            chk,dt= AOE()
            print("++++++++++++++ADEEEEEEEEEEE",dt)
            if chk:
                chkor = binTypeCompatible(typppp,dt,"=")
                print("++++++++++++++ADEEEEEEEEEEE",chkor)
                if chkor ==False:
                    sms = typeMISmatchError(typppp,dt) , calclateLineNo(i)
                    errorList.append(sms)
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    return False
                else:
                    return True
            else:
                
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False



def TAssign_st():
    global i, tokenType
    chk, value = TS()
   
    if chk:
        chker = RTS(value)
        print("PPPPPPPPPPPPPPPPPP RTS TRUE",chker)
        if chker:
            if tokenType[i] == "terminator":
                i=i+1
                return True
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i) 
                return False
        else:
            return False
    else:
        return False





def FNA(parent):
    global i, tokenType
    if tokenType[i] == "terminator":
        if parent not in [
            "int",
            "string",
            "char",
            "bool",
            "float",
        ]:
            print("caannot return non primitive typeeee")
        i = i + 1
        return True , parent
    elif tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            theId = tokenValue[i]
            i = i + 1
            chk , typpp = B(parent , theId)
            if chk:
                return True , typpp
            else:
                return False , "null"
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False , "null"
    else:
        return False, "null"


def Ref():
    global i, tokenType
    if tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            i = i + 1
            if B():
                return True
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return True


def EExp():
    global i, tokenType
    if tokenType[i] == "equals":
        i = i + 1
        chk , tyoo= Exp()
        if chk:
            if tokenType[i] == "terminator":
                i = i + 1
                return True
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False


def B(pType , id2):
    global i, tokenType , argsList
    print("in b ",tokenValue[i],tokenType[i] )
    if tokenType[i] == "equals":
        print('after eqials =', tokenValue[i],tokenType[i])
        i = i + 1
        thDt,accessMod, static, abstract, final=lookupAttributeForTypeDetail(id2,pType)
        if thDt == False:
            print('not esixr')
            return False , "null"
        elif thDt not in [
            "int",
            "string",
            "char",
            "bool",
            "float",
        ]:
            print("caannot return non primitive typeeee")
            return False , "null"
        
        
        print("IN EQUALS", tokenType[i],tokenValue[i])
        chk, typ = Exp()

        if chk:
            kuchBhi = binTypeCompatible(thDt, typ, "=")
            print("IN EXPPPPP", tokenType[i], thDt, typ, kuchBhi)
            if kuchBhi == False:
                errorList.append(typeMISmatchError(thDt,typ))
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                return False, "null"
            if tokenType[i] == "terminator":
                i = i + 1
                return True, kuchBhi
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False ,"null"
        else:
            return False, "null"
    elif tokenType[i] == "dot":
        i = i + 1
        chkORtype = lookupAttributeForTypeDetail(id2,pType)
        print("&&&&&&&&&&&&&&&&&&&&&&&dot true : parent in mas ", parent, chkORtype)
        if chkORtype == False:

            print("not access able in currrent scope declaration error")
            errorList.append(scopeError(id2))
            return False, "null"
        elif chkORtype in [
            "int",
            "string",
            "char",
            "bool",
            "float",
        ]:

            errorList.append(ptypeError(id2))
            print("cannot refer premittive type")
            return False
        if tokenType[i] == "identifier":
            idValue =tokenValue[i]
            # chker = lookupAttributeTable(tokenValue[i], "~", chkORtype)
            i = i + 1
            chk, tyoe = B(chkORtype,idValue)
            if chk:
                print("inBBBBBBBBBBB ")
                return True, tyoe
            else:
                return False, "null"
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False, "null"
    elif tokenType[i] == "incDec":
        i = i + 1
        if tokenType[i] == "terminator":
            return True
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False, "null"
    elif tokenType[i] == "openroundbrace":
        i = i + 1
        if Args():
            thDt,accessMod, static, abstract, final  = lookupAttributeForFuncTypeDetail(id2,pType)
            print("ARGSSSSSS TRUEEEEEEEEEE", tokenType[i])
            if thDt == False:
                print("method doesnaot exist-----00")
                return False, "null"
            # elif thDt in [
            # "int",
            # "string",
            # "char",
            # "bool",
            # "float",
            # ]:
            #     print("tyoasodoasdsadsd type is premittive")
            # else:
            #     print('type is found')
            if tokenType[i] == "closeroundbrace":
                argsList = []
                i = i + 1
                if FNA(thDt):
                    return True
                else:
                    return False, "null"
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False, "null"
        else:
            return False, "null"
    elif tokenType[i] == "opensquarebrace":
        i = i + 1
        chk , tyoo= Exp()
        if chk:
            if tokenType[i] == "closesquarebrace":
                i = i + 1
                if D2DA():
                    if Ref():
                        if EExp():
                            return True
                        else:
                            return False, "null"
                    else:
                        return False, "null"
                else:
                    return False, "null"
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False, "null"
        else:
            return False, "null"
    else:
        return False, "null"


def LAS(parent):
    global i, tokenType, highestScope, accessMODvalue, isStatic, isAbstract, isFinal, currentClass
    if tokenType[i] == "equals":
        i = i + 1
        if isFunc == True:
            leftType = lookupFunctionTable(parent)
            print("tttttttttttttttttttttttttttttttttttttttttttttttttt", leftType)
            if leftType == False:
                print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy", parent)

                print("not declared")
                return False
            elif leftType not in [
            "int",
            "string",
            "char",
            "bool",
            "float",
            ]:
                print("caannot return non primitive typeeee")
                return False , "null"
            else:
                check, rightType = Exp()

                print("+++++++++++++++type of Expt", rightType)
                if check:
                    print(leftType, rightType, "=")
                    theType = binTypeCompatible(leftType, rightType, "=")
                    print(" ------------------------ Type after EQUALS -------------", theType)
                    if theType != False:
                        typ = theType
                    else:
                        theErroro = typeMISmatchError(leftType, rightType)
                        frameinfo = getframeinfo(currentframe())
                        print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                        # theErroro = typeMISmatchError(leftType, rightType), calclateLineNo[i]
                        errorList.append(theErroro)
                        print("type mis match-=============---------=+++++++++++++++++++")
                        return False
                    print("after exp in las", tokenType[i])
                    if tokenType[i] == "terminator":
                        i = i + 1
                        return True 
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                        errorMesssage(i)
                        return False
                else:
                    return False
        else:
            leftType = lookupAttributeForType(parent,currentClass)
            print("tttttttttttttttttttttttttttttttttttttttttttttttttt", leftType)
            if leftType == False:
                print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy", parent)

                print("not declared")
                return False
            elif leftType not in [
            "int",
            "string",
            "char",
            "bool",
            "float",
            ]:
                print("caannot return non primitive typeeee")
                return False , "null"
            else:
                check, rightType = Exp()

                print("+++++++++++++++type of Expt", rightType)
                if check:
                    print(leftType, rightType, "=")
                    theType = binTypeCompatible(leftType, rightType, "=")
                    print(" ------------------------ Type after EQUALS -------------", theType)
                    if theType != False:
                        typ = theType
                    else:
                        theErroro = typeMISmatchError(leftType, rightType)
                        frameinfo = getframeinfo(currentframe())
                        print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                        # theErroro = typeMISmatchError(leftType, rightType), calclateLineNo[i]
                        errorList.append(theErroro)
                        print("type mis match-=============---------=+++++++++++++++++++")
                        return False
                    print("after exp in las", tokenType[i])
                    if tokenType[i] == "terminator":
                        i = i + 1
                        return True 
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                        errorMesssage(i)
                        return False
                else:
                    return False
        # print("+++++++++++++++type of parent", parent)
        
        # print("going in exp", tokenType[i])
        
    elif tokenType[i] == "dot":
        i = i + 1
        print("dot trueeeee")
        #lookup in main not in functable
       
        if tokenType[i] == "identifier":
            theIdentifier = tokenValue[i]
            i = i+1
            if isFunc == True:
                chkORtype = lookupFunctionTable(parent)
                print("&&&&&&&&&&&&&&&&&&&&&&&dot true : parent in mas ", parent, chkORtype)
                if chkORtype == False:
                    sms = parent+"not declared in currrent scope" 
                    errorList.append(sms)
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    return False , "null"
                elif chkORtype  in ["int","float","string","char"]:
                    print(' in att ')
                    # vark,accessMod, static, abstract, final  = lookupAttributeForTypeDetail(theIdentifier,choker)
                    # if vark == False:
                    #     sms = theIdentifier+"is not declared in parent  scope" 
                    #     errorList.append(sms)
                    print("type no referncial")
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    return False , "null"
                else:

                    chk, tyoe = B(chkORtype,theIdentifier)
                    if chk:
                        return True ,tyoe
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                        return False , "null"
            else:
                chkORtype = lookupAttributeForType(parent,currentClass)
                if chkORtype == False:
                    sms = parent+"not declared in currrent scope" 
                    errorList.append(sms)
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    return False , "null"
                elif chkORtype  in ["int","float","string","char"]:
                    print(' in att ')
                    print("type no referncial")
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    return False , "null"
                else:

                    chk, tyoe = B(chkORtype,theIdentifier)
                    if chk:
                        return True ,tyoe
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                        return False , "null"
                    # if(accessMod == "private" and choker != currentClass):
                    # sms = theIdentifier+"is privat in" + choker+ "  scope" 
                    #     errorList.append(sms)
                    #     frameinfo = getframeinfo(currentframe())
                    #     print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    #     return False , "null"
                    # elif final:
                    #         sms = theIdentifier+"is final in and cannot be changed" 
                    #         errorList.append(sms)
                    #         frameinfo = getframeinfo(currentframe())
                    #         print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    #         return False , "null"
                    #     elif vark != parent and static:
                    #         sms = theIdentifier+" variable can not be refernced bcz static" 
                    #         errorList.append(sms)
                    #         frameinfo = getframeinfo(currentframe())
                    #         print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    #         return False , "null"
                    #     else:
                    #         chk, tyoe = B(vark)
                    #         if chk:
                    #             return True ,tyoe
                    #         else:
                    #             frameinfo = getframeinfo(currentframe())
                    #             print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    #             return False , "null"
                    # else: 
                    #     print('cannot refer premitive typo=e')
                # else:
                #     vark,accessMod, static, abstract, final = lookupAttributeForTypeDetail(theIdentifier,chkORtype)
                #     if vark == False:
                #         sms = theIdentifier+"is not declared in parent  scope" 
                #         errorList.append(sms)
                #         frameinfo = getframeinfo(currentframe())
                #         print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                #         return False , "null"
                #     elif(accessMod == "private" and choker != currentClass):
                #         sms = theIdentifier+"is privat in" + choker+ "  scope" 
                #         errorList.append(sms)
                #         frameinfo = getframeinfo(currentframe())
                #         print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                #         return False , "null"
                #     elif final:
                #         sms = theIdentifier+"is final in and cannot be changed" 
                #         errorList.append(sms)
                #         frameinfo = getframeinfo(currentframe())
                #         print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                #         return False , "null"
                #     elif vark != parent and static:
                #         sms = theIdentifier+" variable can not be refernced bcz static" 
                #         errorList.append(sms)
                #         frameinfo = getframeinfo(currentframe())
                #         print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                #         return False , "null"
                #     else:
                #         chk, tyoe = B(vark)
                #         if chk:
                #             return True ,tyoe
                #         else:
                #             frameinfo = getframeinfo(currentframe())
                #             print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                #             return False , "null"
                
                # if chkORtype in [
                #     "intConst",
                #     "stringConst",
                #     "charConst",
                #     "boolConst",
                #     "floatConst",
                # ]:

                #     errorList.append(ptypeError(parent))
                #     print("cannot refer premittive type")

            # chker = lookupAttributeTable(tokenValue[i], "~", chkORtype)
            # i = i + 1
            # chk, tyoe = B(chker)
            # if chk:
            #     print("inBBBBBBBBBBB ")
            #     return True, tyoe
            # else:
            #     return False , "null"
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    elif tokenType[i] == "incDec":
        i = i + 1
        if tokenType[i] == "terminator":
            i = i + 1
            return True
        else:
            print("NOT TERMMMMMMMMMMMMMM")
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    elif tokenType[i] == "identifier":
        iDforType = tokenValue[i]
        if isFunc:
            #check if parent class is not abstract
            check2 = lookupMainTable(parent)
            if check2.typeMod == "abstract":
                sms =  parent + " cannot be instantiated"
                errorList.append(sms)
                return False
            check = insertFunctionTable(iDforType, parent, highestScope)
        else:
            #check if parent class is not abstract
            check2 = lookupMainTable(parent)
            if check2.typeMod == "abstract":
                sms =  parent + " cannot be instantiated"
                errorList.append(sms)
                return False
            check = insertAttribute(
                iDforType,
                parent,
                accessMODvalue,
                isStatic,
                isAbstract,
                isFinal,
                currentClass,
            )
        i = i + 1
        if OBJR() and check and check2:
            return True
        else:
            if check2 == False:
                errorList.append(declarationError(parent))
                return False
            if check == False:
                errorList.append(redeclarationError(iDforType))
                return False
            return False
    elif tokenType[i] == "openroundbrace":
        i = i + 1
        if Args():
            print("ERRRRRAAGHAHGA", tokenType[i])
            if tokenType[i] == "closeroundbrace":
                #check if parent exist in current class AT
                i = i + 1
                if FNA():
                    return True
                else:
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            return False
    elif tokenType[i] == "opensquarebrace":
        i = i + 1
        chk , tyoo= Exp()
        if chk:
            if tokenType[i] == "closesquarebrace":
                i = i + 1
                if D2DA():
                    if Ref():
                        if EExp():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False


def Assign_st():
    global i, tokenType
    if tokenType[i] == "identifier":
        iDforType = tokenValue[i]
        # lookup
        i = i + 1
        print("IN IDDDDDDDDDDDDDDD", tokenType[i],iDforType)
        check = LAS(iDforType)
        if check:
            print("LAS TRUEEEEEEEEEEEEE", tokenType[i])
            return True
        else:
            return False
    else:
        return False


def VAS():
    global i, tokenType
    if tokenType[i] == "equals":
        i = i + 1
        chk , tyoo= Exp()
        if chk:
            return True
        else:
            return False
    elif tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            i = i + 1
            if for_B():
                return True
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    elif tokenType[i] == "incDec":
        i = i + 1
        return True
    else:
        return False


def OBJ():
    global i, tokenType
    if tokenType[i] == "identifier":
        i = i + 1
        if OBJR():
            return True
        else:
            return False
    else:
        return False


def OBJR():
    global i, tokenType
    if tokenType[i] == "equals":
        i = i + 1
        if tokenType[i] == "new":
            i = i + 1
            if tokenType[i] == "identifier":
                i = i + 1
                if tokenType[i] == "openroundbrace":
                    i = i + 1
                    if Args():
                        if tokenType[i] == "closeroundbrace":
                            i = i + 1
                            if tokenType[i] == "terminator":
                                i = i + 1
                                return True
                            else:
                                frameinfo = getframeinfo(currentframe())
                                print(
                                    "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                    frameinfo.lineno,
                                )
                                errorMesssage(i)
                                return False
                        else:
                            frameinfo = getframeinfo(currentframe())
                            print(
                                "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                frameinfo.lineno,
                            )
                            errorMesssage(i)
                            return False
                    else:
                        return False
                else:
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    elif tokenType[i] == "terminator":
        i = i + 1
        return True
    else:
        return False


def Ref1():
    global i, tokenType
    if tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            first = tokenValue[i]
            i = i + 1
            chk, tyoe = MAS(first)
            if chk:
                return True, tyoe
            else:
                return False
        else:
            errorMesssage(i)
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            return False
    else:
        return True
def BAS(pType,id2):
    global i, tokenType, currentClass
    # searchIn = parent
    # theType = ""
    print("IN BAS", pType,id2,tokenType[i])
    if tokenType[i] == "dot":
        i = i + 1
        chkORtype = lookupAttributeForTypeDetail(id2,pType)
        print("&&&&&&&&&&&&&&&&&&&&&&&dot true : parent in mas ", parent, chkORtype)
        if chkORtype == False:

            print("not access able in currrent scope declaration error")
            errorList.append(scopeError(id2))
            return False, "null"
        elif chkORtype in [
            "int",
            "string",
            "char",
            "bool",
            "float",
        ]:

            errorList.append(ptypeError(id2))
            print("cannot refer premittive type")
            return False
        if tokenType[i] == "identifier":
            idValue =tokenValue[i]
            # chker = lookupAttributeTable(tokenValue[i], "~", chkORtype)
            i = i + 1
            chk, tyoe = BAS(chkORtype,idValue)
            if chk:
                print("inBBBBBBBBBBBqqqqq ")
                return True, tyoe
            else:
                return False, "null"
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False, "null"

    elif tokenType[i] == "incDec":
        i = i + 1
        return True
    elif tokenType[i] == "openroundbrace":
        i = i + 1
        if Args():
            print("AFTER ARGS", tokenType[i])
            if tokenType[i] == "closeroundbrace":
                i = i + 1
                if Ref1():
                    print("efhjsfgwiufg")
                    return True
                else:
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            return False
    elif tokenType[i] == "opensquarebrace":
        i = i + 1
        chk , tyoo= Exp()
        if chk:
            if tokenType[i] == "closesquarebrace":
                i = i + 1
                if D2DA():
                    if Ref1():
                        print("ras true")
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            return False
    else:
        abd= lookupAttributeForType(id2,pType)
        print('printing bsdbsd',abd)
        if abd not in ["int",
            "string",
            "char",
            "bool",
            "float",]:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            smms = "cannot return non-primitive BAS"
            errorList.append(smms)
            return False, "null"
        # if(theType != ""):
        #     return True , theType
        return True, abd


def MAS(parent):
    global i, tokenType, currentClass,isFunc
    searchIn = parent
    theType = lookupFunctionTable(parent)
    

    print("IN MAS", tokenType[i])
    if tokenType[i] == "dot":
        i = i + 1
        print("dot trueeeee")
        #lookup in main not in functable
       
        if tokenType[i] == "identifier":
            theIdentifier = tokenValue[i]
            i = i + 1
            if isFunc == True:
                chkORtype = lookupFunctionTable(parent)
                print("&&&&&&&&&&&&&&&&&&&&&&&dot true : parent in mas ", parent, chkORtype)
                if chkORtype == False:
                    sms = parent+"not declared in currrent scope" 
                    errorList.append(sms)
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    return False , "null"
                elif chkORtype  in ["int","float","string","char"]:
                    print(' in att ')
                    # vark,accessMod, static
                    print("type no referncial")
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    return False , "null"
                else:
                    # theType=chkORtype
                    print("going in bas")
                    chk, tyoe = BAS(chkORtype,theIdentifier)
                    if chk:
                        return True ,tyoe
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                        return False , "null"
            else:
                return False , "null"
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False , "null"
    elif tokenType[i] == "incDec":
        i = i + 1
        return True
    elif tokenType[i] == "openroundbrace":
        i = i + 1
        if Args():
            print("AFTER ARGS", tokenType[i])
            if tokenType[i] == "closeroundbrace":
                i = i + 1
                if Ref1():
                    print("efhjsfgwiufg")
                    return True
                else:
                    return False , "null"
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False , "null"
        else:
            return False , "null"
    elif tokenType[i] == "opensquarebrace":
        i = i + 1
        chk , tyoo= Exp()
        if chk:
            if tokenType[i] == "closesquarebrace":
                i = i + 1
                if D2DA():
                    if Ref1():
                        print("ras true")
                        return True
                    else:
                        return False , "null"
                else:
                    return False , "null"
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False , "null"
        else:
            return False , "null"
    else:
        print('im amamsdsdfsdf',parent)
        if isFunc == False:
            theType = lookupAttributeForType(parent,currentClass)
        # else:
        #     abd= lookupFunctionTable(parent)
        if theType not in ["int",
            "string",
            "char",
            "bool",
            "float",]:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            smms = "cannot return non-primitive mas"
            errorList.append(smms)
            return False, "null"
        # if(theType != ""):
        #     return True , theTyp
        print('sssssssssssssssssssssssssssssssssssssssssssss',theType)
        return True, theType



def Decl():
    global i, tokenType, currentClass, accessMODvalue, isStatic, isFinal, isAbstract, isFunc, highestScope
    if tokenType[i] in ["dataType" , "string"]:
        dt = tokenValue[i]
        i = i + 1
        if tokenType[i] == "identifier":
            mainID = tokenValue[i]
            i = i + 1

            check, arrDimen = AR(dt)
            print("akter ar 000000000000000000")
            if check:
                if arrDimen != "":
                    dt = arrDimen
                print(
                    "oppppppppppppppppppp",
                    dt,
                    mainID,
                    arrDimen,
                    accessMODvalue,
                    isStatic,
                    isFinal,
                    isAbstract,
                    currentClass,
                )
                if isFunc == False:
                    isInserted = insertAttribute(
                        mainID,
                        dt,
                        accessMODvalue,
                        isStatic,
                        isAbstract,
                        isFinal,
                        currentClass,
                    )
                else:
                    isInserted = insertFunctionTable(mainID, dt, highestScope)
                dt=dt.split("[")[0]
                initchk , initType = init1(dt) 
                if initchk and isInserted:
                    if list1(initType):
                        return True
                    else:
                        return False
                else:
                    if isInserted == False:
                        sms = redeclarationError(mainID)
                        errorList.append(sms)
                    return False
            else:
                return False
        else:
            return False

    else:
        return False


def AR(dt):
    global i, tokenType
    arryDimension = ""
    print("IN AR4RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    if tokenType[i] == "opensquarebrace":
        i = i + 1
        print("AFTER OSBBBBBBBBBBBBBBBBBBBBBBB")
        chk,typ= ExpN()
        if chk :
            if typ!="int" and typ!="null" :
                print("tyooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
                a= "Araay size dhould be integer",calclateLineNo(i)
                errorList.append(a)
                return False , arryDimension
            print("EXPNNMNNNNNNNNNNNNNNNNNNNNNNNNNN")
            if tokenType[i] == "closesquarebrace":

                arryDimension = "%s[]" % (dt)
                print("the arr dimansion", arryDimension)
                i = i + 1
                check, arryDimension2 = D2DB(dt)
                if check:
                    if arryDimension2 == "":
                        return True, arryDimension
                    return True, arryDimension2
                else:
                    return False, arryDimension
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False, arryDimension
        else:
            return False, arryDimension
    else:
        return True, arryDimension


def D2DB(dt):
    global i, tokenType
    arryDimension = ""
    if tokenType[i] == "opensquarebrace":
        i = i + 1
        chk,typ= ExpN()
        if chk :
            if typ!="int":
                a= "Araay size dhould be integer",calclateLineNo(i)
                errorList.append(a)
                return False , arryDimension
            if tokenType[i] == "closesquarebrace":
                arryDimension =  "%s[][]" % (dt)
                print("the assdfwdf arraydimension", arryDimension, dt)
                i = i + 1
                return True, arryDimension
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False , "null"
        else:
            return False, "null"
    else:
        return True, arryDimension


def list1(dt):
    global i, tokenType, accessMODvalue, isStatic, isFinal, isAbstract
    if tokenType[i] == "terminator":
        i = i + 1
        return True 
    elif tokenType[i] == "comma":
        i = i + 1
        if tokenType[i] == "identifier":
            theID = tokenValue[i]
            i = i + 1
            check, arrDimen = AR(dt)
            if check:
                if arrDimen != "":
                    dt = arrDimen
                print(
                    "oppppppppppppppppppp list mod",
                    dt,
                    theID,
                    arrDimen,
                    accessMODvalue,
                    isStatic,
                    isFinal,
                    isAbstract,
                    currentClass,
                )
                if isFunc == False:
                    isInserted = insertAttribute(
                        theID,
                        dt,
                        accessMODvalue,
                        isStatic,
                        isAbstract,
                        isFinal,
                        currentClass,
                    )
                else:
                    isInserted = insertFunctionTable(theID, dt, highestScope)
                
                dt=dt.split("[")[0]
                initchk , initType = init1(dt) 
                if initchk and isInserted:
                    if list1(initType):
                        return True
                    else:
                        return False
                else:
                    if isInserted == False:
                        sms = redeclarationError(theID)
                        errorList.append(sms)
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def init1(dt):
    global i, tokenType
    if tokenType[i] == "equals":
        i = i + 1
        print("AFTER DECL EQUALS", tokenType[i])
        # chk = initD(dt)
        chk , tope = initD(dt)
        if chk:
            return True , tope
        else:

            return False , "null"
    else:
        return True, dt


def initD(dt):
    global i, tokenType
    chk, dts = Exp()
    typemis = binTypeCompatible(dt,dts,"=")
    if chk:
        if typemis == False:
            asd = typeMISmatchError(dt,dts) , calclateLineNo(i)
            errorList.append(asd)
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            return False, "null"
        print("check is tru")
        chak , tops = init1(dts)
        if chak:
            return True , tops
        else:
            return False , "null"
    # elif tokenType[i] in [
    #     "intConst",
    #     "stringConst",
    #     "charConst",
    #     "boolConst",
    #     "floatConst",
    # ]:
    #     rightType = tokenType[i].split("C")[0]
    #     thessss = binTypeCompatible(dt, rightType, "=")
    #     print(
    #         "-----------------after dec ++++++++++++++++++++++++",
    #         thessss,
    #         dt,
    #         rightType,
    #     )
    #     if thessss == False:
    #         theErroro = typeMISmatchError(dt, rightType)
    #         # theErroro = typeMISmatchError(dt, rightType) + calclateLineNo[i]
    #         errorList.append(theErroro)
    #     i = i + 1
    #     return True, thessss
    # elif tokenType[i] == "opensquarebrace":
    #     i = i + 1
    #     if Args():
    #         if tokenType[i] == "closesquarebrace":
    #             i = i + 1
    #             return True 
    #         else:
    #             frameinfo = getframeinfo(currentframe())
    #             print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
    #             errorMesssage(i)
    #             return False
    #     else:
    #         return False
    else:
        return False , "null"


def while_st():
    global i, tokenType,highestScope
    if tokenType[i] == "while":
        i = i + 1
        if tokenType[i] == "openroundbrace":
            i = i + 1
            chk , tyoo= Exp()
            if chk:
                if tokenType[i] == "closeroundbrace":
                    i = i + 1
                    highestScope = createScope()
                    if tokenType[i] == "opencurlybrace":
                        i = i + 1
                        if MST():
                            if tokenType[i] == "closecurlybrace":
                                destroyScope()
                                i = i + 1
                                return True
                            else:
                                frameinfo = getframeinfo(currentframe())
                                print(
                                    "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                    frameinfo.lineno,
                                )
                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def for_st():
    global i, tokenType,highestScope
    print("in for", tokenType[i])
    if tokenType[i] == "for":
        print("for true")
        i = i + 1
        if tokenType[i] == "openroundbrace":
            i = i + 1
            if P1():
                print("p1 tru", tokenType[i])
                if P2():
                    print("p2 tru", tokenType[i])
                    if tokenType[i] == "terminator":
                        i = i + 1
                        if P3():
                            print("p3 tru", tokenType[i])
                            if tokenType[i] == "closeroundbrace":
                                i = i + 1
                                if tokenType[i] == "opencurlybrace":
                                    i = i + 1
                                    if MST():
                                        if tokenType[i] == "closecurlybrace":
                                            i = i + 1
                                            print("for endeddddddd")
                                            return True
                                        else:
                                            frameinfo = getframeinfo(currentframe())
                                            print(
                                                "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                                frameinfo.lineno,
                                            )
                                            errorMesssage(i)
                                            return False
                                    else:
                                        return False
                                else:
                                    frameinfo = getframeinfo(currentframe())
                                    print(
                                        "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                        frameinfo.lineno,
                                    )
                                    errorMesssage(i)
                                    return False
                            else:
                                frameinfo = getframeinfo(currentframe())
                                print(
                                    "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                    frameinfo.lineno,
                                )
                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def P1():
    global i, tokenType
    if Decl():
        return True
    elif Assign_st():
        return True
    elif tokenType[i] == "terminator":
        i = i + 1
        return True
    elif TAssign_st():
        return True
    else:
        return False


def P2():
    global i, tokenType
    chk , tyoo= Exp()
    if chk:
        return True
    else:
        return True


def P3():
    global i, tokenType
    if for_assign():
        return True
    elif inc_dec():
        print("DECCCCCCCCCCC TRUUUEEE")
        return True
    else:
        return True


def for_assign():
    global i, tokenType
    if TSD():
        if tokenType[i] == "identifier":
            i = i + 1
            if VAS():
                return True
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def inc_dec():
    global i, tokenType
    if tokenType[i] == "incDec":
        i = i + 1
        print("DECCCCCCCCC", tokenType[i])
        if tokenType[i] == "identifier":
            # look type

            # dt = tokenValue[i]
            i = i + 1
            return True, dt
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def switch_st():
    global i, tokenType
    if tokenType[i] == "switch":
        i = i + 1
        if tokenType[i] == "openroundbrace":
            i = i + 1
            if switch_in():
                if tokenType[i] == "closeroundbrace":
                    i = i + 1
                    if tokenType[i] == "opencurlybrace":
                        i = i + 1
                        if switch_B():
                            if tokenType[i] == "closecurlybrace":
                                i = i + 1
                                return True
                            else:
                                frameinfo = getframeinfo(currentframe())
                                print(
                                    "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                    frameinfo.lineno,
                                )
                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def switch_in():
    global i, tokenType
    if tokenType[i] in [
        "identifier",
        "intConst",
        "floatConst",
        "charConst",
        "stringConst",
        "boolConst",
    ]:
        i = i + 1
        return True
    else:
        return False


def switch_B():
    global i, tokenType
    if condition():
        if tokenType[i] == "opencurlybrace":
            i = i + 1
            if MST():
                if tokenType[i] == "closecurlybrace":
                    i = i + 1
                    if switch_B():
                        return True
                    else:
                        return False
                else:
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return True


def condition():
    global i, tokenType
    if tokenType[i] == "case":
        i = i + 1
        if tokenType[i] in {
            "intConst",
            "floatConst",
            "charConst",
            "stringConst",
            "boolConst",
        }:
            i = i + 1
            if tokenType[i] == "colon":
                i = i + 1
                return True
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False

    elif tokenType[i] == "default":
        i = i + 1
        if tokenType[i] == "colon":
            i = i + 1
            return True
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def if_else_elif():
    global i, tokenType ,highestScope
    if tokenType[i] == "if":
        i = i + 1
        chk , tyoo= Exp()
        if chk:
            highestScope = createScope()
            if tokenType[i] == "opencurlybrace":
                i = i + 1
                if MST():
                    if tokenType[i] == "closecurlybrace":
                        destroyScope()
                        i = i + 1
                        if elif_st():
                            if else_st():
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False


def elif_st():
    global i, tokenType ,highestScope
    if tokenType[i] == "elif":
        i = i + 1
        chk , tyoo= Exp()
        if chk:
            highestScope = createScope()
            if tokenType[i] == "opencurlybrace":
                i = i + 1
                if MST():
                    if tokenType[i] == "closecurlybrace":
                        destroyScope()
                        i = i + 1
                        if elif_st():
                            return True
                        else:
                            return False
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return True


def else_st():
    global i, tokenType , highestScope
    if tokenType[i] == "else":
        i = i + 1
        if tokenType[i] == "colon":
            i = i + 1
            highestScope = createScope()
            if tokenType[i] == "opencurlybrace":
                i = i + 1
                if MST():
                    if tokenType[i] == "closecurlybrace":
                        destroyScope()
                        i = i + 1
                        return True
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return True


def break_st():
    global i, tokenType
    if tokenType[i] == "break":
        i = i + 1
        if tokenType[i] == "terminator":
            i = i + 1
            return True
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def continue_st():
    global i, tokenType
    if tokenType[i] == "continue":
        i = i + 1
        if tokenType[i] == "terminator":
            i = i + 1
            return True
        else:
            return False
    else:
        return False


def return_st():
    global i, tokenType
    if tokenType[i] == "return":
        i = i + 1
        if ExpN():
            if tokenType[i] == "terminator":
                i = i + 1
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def ExpN():
    global i, tokenType
    print("IN EXPNNNNNNNNNNNNNNNNNNNN")
    chkk ,tyur =Exp()
    if chkk:
        print("exp trueeeeeeeeeeeeeeeeeeeeeeee")
        return True ,tyur
    else:
        return True , "null"


def Args():
    global i, tokenType,argsList
    print("in argssssssss", tokenType[i])
    chk , tyoo= Exp()
    argsList.append(tyoo)
    if chk:
        print("exp trueeeeee")
        if ArgsD():
            return True
        else:
            return False
    else:
        print(errorList)
        print("EXP FALSEEEEE", tokenType[i])
        return True


def ArgsD():
    global i, tokenType,argsList
    print("in argsd")
    if tokenType[i] == "comma":
        i = i + 1
        chk , tyoo= Exp()
        argsList.append(tyoo)
        if chk:
            if ArgsD():
                return True
            else:
                return False
        else:
            return False
    else:
        return True


def try_catch_st():
    global i, tokenType
    if tokenType[i] == "try":
        i = i + 1
        if tokenType[i] == "opencurlybrace":
            i = i + 1
            if MST():
                if tokenType[i] == "closecurlybrace":
                    i = i + 1
                    if OTC():
                        return True
                    else:
                        return False
                else:
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def OTC():
    global i, tokenType
    if tokenType[i] == "catch":
        i = i + 1
        if tokenType[i] == "openroundbrace":
            i = i + 1
            if tokenType[i] == "Exception":
                i = i + 1
                if tokenType[i] == "identifier":
                    i = i + 1
                    if tokenType[i] == "closeroundbrace":
                        i = i + 1
                        if tokenType[i] == "opencurlybrace":
                            i = i + 1
                            if MST():
                                if tokenType[i] == "closecurlybrace":
                                    i = i + 1
                                    if OTFD():
                                        return True
                                    else:
                                        return False
                                else:
                                    frameinfo = getframeinfo(currentframe())
                                    print(
                                        "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                        frameinfo.lineno,
                                    )
                                    errorMesssage(i)
                                    return False
                            else:
                                return False
                        else:
                            frameinfo = getframeinfo(currentframe())
                            print(
                                "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                frameinfo.lineno,
                            )
                            errorMesssage(i)
                            return False
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            return False
    elif OTF():
        return True
    else:
        return False


def OTF():
    global i, tokenType
    if tokenType[i] == "finally":
        i = i + 1
        if tokenType[i] == "opencurlybrace":
            i = i + 1
            if MST():
                if tokenType[i] == "closecurlybrace":
                    i = i + 1
                else:
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def OTFD():
    global i, tokenType
    if tokenType[i] == "finally":
        i = i + 1
        if tokenType[i] == "opencurlybrace":
            i = i + 1
            if MST():
                if tokenType[i] == "closecurlybrace":
                    i = i + 1
                else:
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return True


def Exp():
    global i, tokenType
    print("in exp00000000",tokenType[i])
    chkk, typp = ANDOP()
    if chkk:
        chker, types = ExpD(typp)
        if chker:
            return True, types
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            return False, "null"
    else:
        return False, "null"


def ExpD(leftType):
    global i, tokenType
    if tokenType[i] == "OR":
        op = tokenValue[i]
        i = i + 1
        chk, rightType = ANDOP()
        if chk:
            print(leftType, rightType, op)
            theType = binTypeCompatible(leftType, rightType, op)
            print(
                " ------------------------ Type after comparisio -------------", theType
            )
            if theType != False:
                typ = theType
            else:
                print("type mis match-=============---------=+++++++++++++++++++")
            chk, tope = ExpD(typ)
            if chk and tope != False:
                return True, tope
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                return False, "null"
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            return False, "null"
    else:
        return True, leftType


def ANDOP():
    print("IN ANDOP")
    global i, tokenType
    chk, typ = ROPOP()
    if chk:
        chhk, tyyyp = ANDOPD(typ)
        if chhk:
            return True, tyyyp
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            return False, "null"
    else:
        return False, "null"


def ANDOPD(leftType):
    global i, tokenType
    if tokenType[i] == "AND":
        op = tokenValue[i]
        i = i + 1
        chk, rightType = ROPOP()
        if chk:
            print(leftType, rightType, op)
            theType = binTypeCompatible(leftType, rightType, op)
            print(
                " ------------------------ Type after comparisio -------------", theType
            )
            if theType != False:
                typ = theType
            else:
                print("type mis match-=============---------=+++++++++++++++++++")
            chk, tope = ANDOPD(typ)
            if chk and tope != False:
                return True, tope
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                return False, "null"
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            return False, "null"
    else:
        return True, leftType


def ROPOP():
    print("IN ROPOP")
    global i, tokenType
    chkk, typp = E()
    if chkk:
        chker, types = ROPOPD(typp)
        if chker:
            return True, types
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            return False, "null"
    else:
        return False, "null"


def ROPOPD(leftType):
    global i, tokenType
    print("in ropopd", tokenType[i])
    # need to be check
    if tokenType[i] == "compareOp":
        op = tokenValue[i]
        i = i + 1
        chk, rightType = E()
        if chk:
            print(leftType, rightType, op)
            theType = binTypeCompatible(leftType, rightType, op)
            print(
                " ------------------------ Type after comparisio -------------", theType
            )
            if theType != False:
                typ = theType
            else:
                print("type mis match-=============---------=+++++++++++++++++++")
            chk, tope = ROPOPD(typ)
            if chk and tope != False:
                return True, tope
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                return False, "null"
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            return False, "null"
    else:
        return True, leftType


def E():
    print("IN E")
    global i, tokenType
    chk, typ = T()
    if chk:
        chker, typd = ED(typ)
        if chker:
            return True, typd
        else:
            return False, "null"
    else:
        return False, "null"


def ED(leftType):
    global i, tokenType
    if tokenType[i] == "PM":
        op = tokenValue[i]
        i = i + 1
        chk, rightType = T()
        if chk:
            print(leftType, rightType, op)
            theType = binTypeCompatible(leftType, rightType, op)
            print("-----------tyoe after comaoasdfsdf ------", theType)
            typ = ""
            if theType != False:
                typ = theType
            chsck, tope = ED(typ)
            if chsck and tope != False:
                return True, tope
            else:
                return False, "null"
        else:
            return False, "null"
    else:
        return True, leftType


def T():
    print("IN T")
    global i, tokenType
    chk, typ = F()
    if chk:
        chhk, typew = TD(typ)
        if chhk:
            return True, typew
        else:
            return False, "null"
    else:
        return False, "null"


def TD(leftType):
    global i, tokenType
    if tokenType[i] == "MDM":
        op = tokenValue[i]
        i = i + 1
        chk, rightType = F()
        if chk:
            print(leftType, rightType, op)
            theType = binTypeCompatible(leftType, rightType, op)
            print(
                " ------------------------ Type after comparisio -------------", theType
            )
            if theType != False:
                typ = theType
            else:
                print("type mis match-=============---------=+++++++++++++++++++")
            ccchk, tope = TD(leftType)
            if ccchk and tope != False:
                return True, tope
            else:
                return False, "null"
        else:
            return False, "null"
    else:
        return True, leftType


def F():
    print("IN F")
    global i, tokenType
    if tokenType[i] == "openroundbrace":
        i = i + 1
        chker , typp = Exp()
        if chker:
            # return laiga

            if tokenType[i] == "closeroundbrace":
                i = i + 1
                # will return function rdt
                return True
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False, "null"
        else:
            return False, "null"
    elif tokenType[i] in [
        "intConst",
        "stringConst",
        "charConst",
        "boolConst",
        "floatConst",
    ]:
        rightType = tokenType[i].split("C")[0]
        thessss = rightType
        # thessss = uniTypeCompatible(rightType, "=")
        # thessss = binTypeCompatible(dt, rightType, "=")
        print(
            "-----------------after const in F ++++++++++++++++++++++++",
            thessss,
            # dt,
            rightType,
        )
        if thessss == False:
            thelinesd = calclateLineNo(i)
            theErroro = "jani ye dekh aakr " , thelinesd
            # theErroro = typeMISmatchError(dt, rightType)
            # theErroro = typeMISmatchError(dt, rightType) + calclateLineNo[i]
            errorList.append(theErroro)
        i = i + 1
        return True, thessss
    elif tokenType[i] == "notOp":
        i = i + 1
        check, dtOut = F()
        if check:
            # f will return dt
            return True, dtOut

    elif inc_dec():
        return True
    # elif tokenType[i] == "opensquarebrace":
    #     i = i + 1
    #     if Args():
    #         if tokenType[i] == "closesquarebrace":
    #             i = i + 1
    #             # will return array dt
    #             return True
    #         else:
    #             frameinfo = getframeinfo(currentframe())
    #             print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
    #             errorMesssage(i)
    #             return False , "null"
    #     else:
    #         return False, "null"
    else:
        print("IN F TRAS")
        chk, tpe = TRAS()
        print("-----------000000000000000--------", chk)
        if chk:
            return True, tpe
        else:
            return False, "null"


def int_var():
    global i, tokenType
    if tokenType[i] == "public":
        print("public match")
        i = i + 1
        if tokenType[i] == "static":
            i = i + 1
            if tokenType[i] == "final":
                i = i + 1
                if tokenType[i] == "dataType":
                    i = i + 1
                    if tokenType[i] == "identifier":
                        i = i + 1
                        if tokenType[i] == "equals":
                            i = i + 1
                            chk , tyoo= Exp()
                            if chk:
                                if tokenType[i] == "terminator":
                                    i = i + 1
                                    return True
                                else:
                                    frameinfo = getframeinfo(currentframe())
                                    print(
                                        "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                        frameinfo.lineno,
                                    )
                                    errorMesssage(i)
                                    return False
                            else:
                                return False
                        else:
                            frameinfo = getframeinfo(currentframe())
                            print(
                                "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                frameinfo.lineno,
                            )
                            errorMesssage(i)
                            return False
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def int_B():
    global i, tokenType
    print("in interface b", tokenType[i])
    if abs_func_def():
        print("abs func match")
        if int_B():
            return True
        else:
            return False
    elif int_var():
        if int_B():
            return True
        else:
            return False
    else:
        return True


def idDash():
    global i, tokenType, multipleInterface
    if tokenType[i] == "comma":
        i = i + 1
        if tokenType[i] == "identifier":
            multipleInterface.append(tokenValue[i])
            i = i + 1
            if idDash():
                return True
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return True


def int_INH():
    global i, tokenType, extendingClass
    if tokenType[i] == "extends":
        i = i + 1
        if tokenType[i] == "identifier":
            extendingClass = tokenValue[i]
            i = i + 1
            if idDash():
                return True
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return True


def enum_body():
    global i, tokenType, enumlist
    if tokenType[i] == "stringConst":
        enumlist.append(tokenValue[i])
        i = i + 1
        if mStringConst():
            return True
        else:
            return False
    else:
        return True


def NAMF():
    global i, tokenType, mainTableTypeMOD, isFinal
    if tokenType[i] == "final":
        isFinal = True
        mainTableTypeMOD = "final"
        i = i + 1
        return True
    return True


def enum_def():
    global i, tokenType, mainTableType, currentClass, mainTableTypeMOD, enumlist
    if tokenType[i] == "enum":
        mainTableType = "enum"
        i = i + 1
        if tokenType[i] == "identifier":
            currentClass = tokenValue[i]
            notExist = insertMainTable(
                currentClass,
                mainTableType,
                mainTableTypeMOD,
                extendingClass,
                multipleInterface,
            )
            print(notExist, "the result")
            print("after insertion")
            i = i + 1
            if tokenType[i] == "opencurlybrace" and notExist:
                i = i + 1
                if enum_body():
                    print(enumlist)
                    success = insertenumconst(currentClass, enumlist)
                    if tokenType[i] == "closecurlybrace" and success:
                        currentClass = ""
                        mainTableType = ""
                        i = i + 1
                        return True
                    else:
                        if not success:
                            print("attribute not inrted")
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                if notExist == False:
                    errorList.append(redeclarationError(currentClass))
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def imp():
    global i, tokenType, multipleInterface

    if tokenType[i] == "implements":
        i = i + 1
        if tokenType[i] == "identifier":
            multipleInterface.append(tokenValue[i])
            i = i + 1
            if idDash():
                return True
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return True


def INH():
    global i, tokenType, extendingClass
    if tokenType[i] == "extends":
        i = i + 1
        if tokenType[i] == "identifier":
            extendingClass = tokenValue[i]
            i = i + 1
            if imp():
                return True
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    elif imp():
        return True
    else:
        return True


def AN(dataTy):
    global i, tokenType
    cons = ""
    if tokenType[i] == "opensquarebrace":
        i = i + 1
        if tokenType[i] == "closesquarebrace":
            i = i + 1
            cons = dataTy + "[]"
            return True, cons
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return True, cons


def RDT():
    global i, tokenType
    dt = ""
    if tokenType[i] == "void":
        dt = "void"
        i = i + 1
        return True, dt
    elif tokenType[i] == "dataType":
        dt = tokenValue[i]
        i = i + 1
        chker, rdddt = AN(dt)
        if chker:
            if rdddt != "":
                dt = rdddt
            return True, dt
    elif tokenType[i] == "identifier":
        # search type in ftable
        i = i + 1
        return True, dt
    else:
        return False, dt


def Dec():
    global i, tokenType, signature
    if tokenType[i] == "dataType":
        fdt = tokenValue[i]
        i = i + 1
        if tokenType[i] == "identifier":
            yid = tokenValue[i]
            # insertFunctionTable()
            i = i + 1
            chk, fadt = AN(fdt)
            if fadt != "":
                fdt = fadt
            if chk:
                signature.append(fdt)
                cheker = insertFunctionTable(yid, fdt, highestScope)
                if cheker:
                    print("success append in fyncrion ----------------")
                    print("appende from declaration -----------------")
                    return True
                else:
                    sms= yid + "redeclaration error"
                    errorList.append(sms)
                    return False
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def obj():
    global i, tokenType
    if tokenType[i] == "identifier":
        fdt = tokenValue[i]
        i = i + 1
        if tokenType[i] == "identifier":
            yid = tokenValue[i]
            i = i + 1
            signature.append(fdt)
            fins = lookupMainTable(fdt)
            if fins.typeMod == "abstract":
                sms =  fdt + " cannot be instantiated"
                errorList.append(sms)
                return False
            cheker = insertFunctionTable(yid, fdt, highestScope)
            if cheker:
                print("success append in fyncrion ----------------")
                print("appende from declaration -----------------")
                return True
            else:
                sms= yid + "redeclaration error"
                errorList.append(sms)
                return False
            
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def Dec_Obj():
    global i, tokenType
    if Dec():
        return True
    elif obj():
        return True
    else:
        return False


def PARAM1():
    global i, tokenType
    if tokenType[i] == "comma":
        i = i + 1
        if Dec_Obj():
            if PARAM1():
                return True
        else:
            return False
    else:
        return True


def PARAM():
    global i, tokenType
    if Dec():
        if PARAM1():
            return True
    elif obj():
        if PARAM1():
            return True
    else:
        return True


def func_def():
    global i, tokenType, currentClass, signature, accessMODvalue, isStatic, isAbstract, isFinal,  highestScope, isFunc
    if tokenType[i] == "basic":
        i = i + 1
        check, retdt = RDT()
        if check:
            if tokenType[i] == "def":
                i = i + 1
                if tokenType[i] == "identifier":
                    funcId = tokenValue[i]
                    i = i + 1
                    if tokenType[i] == "openroundbrace":
                        highestScope = createScope()
                        isFunc = True
                        i = i + 1
                        if PARAM():
                            if tokenType[i] == "closeroundbrace":

                                signature.append("->")
                                signature.append(retdt)
                                chk = insertAttribute(
                                    funcId,
                                    signature,
                                    accessMODvalue,
                                    isStatic,
                                    isAbstract,
                                    isFinal,
                                    currentClass,
                                )
                                signature = []
                                i = i + 1
                                if tokenType[i] == "opencurlybrace" and chk == True:
                                    i = i + 1
                                    if MST():
                                        if tokenType[i] == "closecurlybrace":
                                            destroyScope()
                                            isFunc = False
                                            i = i + 1
                                            print("close curly truuu", tokenType[i])
                                            return True
                                        else:
                                            frameinfo = getframeinfo(currentframe())
                                            print(
                                                "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                                frameinfo.lineno,
                                            )
                                            errorMesssage(i)
                                            return False
                                    else:
                                        return False
                                else:
                                    if chk == False:
                                        errorList.append(
                                            redeclarationError(currentClass)
                                        )
                                        return False
                                    frameinfo = getframeinfo(currentframe())
                                    print(
                                        "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                        frameinfo.lineno,
                                    )
                                    errorMesssage(i)
                                    return False
                            else:
                                frameinfo = getframeinfo(currentframe())
                                print(
                                    "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                    frameinfo.lineno,
                                )
                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            if check == False:
                print("type error")
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def construct_def():
    global i, tokenType, currentClass, signature, accessMODvalue, isStatic, isAbstract, isFinal, createScope, highestScope, isFunc
    if tokenType[i] == "def":
        i = i + 1
        if tokenType[i] == "identifier":
            if tokenValue[i] != currentClass:
                print("constructor syntax error")
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
            i = i + 1
            if tokenType[i] == "openroundbrace":
                print("-------SCOPE BEFORE-------", highestScope)
                highestScope = createScope()
                isFunc = True
                print("--------SCOPE AFTER---------", highestScope)
                i = i + 1
                if PARAM():
                    if tokenType[i] == "closeroundbrace":
                        signature.append("->")
                        chk = insertAttribute(
                            currentClass,
                            signature,
                            accessMODvalue,
                            isStatic,
                            isAbstract,
                            isFinal,
                            currentClass,
                        )
                        signature = []
                        i = i + 1
                        if tokenType[i] == "opencurlybrace" and chk == True:
                            i = i + 1
                            print("cdsfojvfuovhefuovheuo",tokenType[i])
                            print("elseeeeeeeeeeeeee", tokenType[i])
                            if MST():
                                if tokenType[i] == "closecurlybrace":
                                    destroyScope()
                                    isFunc = False
                                    i = i + 1
                                    return True
                                else:
                                    print("elseeeeeeeeeeeeee closecurly", tokenType[i])
                                    frameinfo = getframeinfo(currentframe())
                                    print(
                                        "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                        frameinfo.lineno,
                                    )
                                    errorMesssage(i)
                                    return False
                            else:
                                return False
                        else:
                            if chk == False:
                                errorList.append(redeclarationError(currentClass))
                                return False
                            frameinfo = getframeinfo(currentframe())
                            print(
                                "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                frameinfo.lineno,
                            )
                            errorMesssage(i)
                            return False
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def SST():
    global i, tokenType
    print("sst")
    if tokenType[i] == "while":
        if while_st():
            return True
        else:
            return False
    elif tokenType[i] == "for":
        if for_st():
            return True
        else:
            return False
    elif tokenType[i] == "switch":
        if switch_st():
            return True
        else:
            return False
    elif tokenType[i] == "if":
        if if_else_elif():
            return True
        else:
            return False
    elif tokenType[i] == "break":
        if break_st():
            return True
        else:
            return False
    elif tokenType[i] == "continue":
        if continue_st():
            return True
        else:
            return False
    elif tokenType[i] == "return":
        if return_st():
            return True
        else:
            return False
    elif tokenType[i] == "identifier":
        if Assign_st():
            print("assign truuuuuuuuu")
            return True
        else:
            return False
    elif tokenType[i] in ["this", "super"]:
        if TAssign_st():
            print("@@@@@@@@@@@@@@@@@@",tokenType[i])

            return True
        else:
            return False
    elif Decl():
        return True
    elif tokenType[i] == "try":
        if try_catch_st():
            return True
        else:
            return False
    else:
        return False


def MST():
    global i, tokenType
    if SST():
        if MST():
            return True
        else:
            return False
    else:
        return True


def CB():
    global i, tokenType, accessMODvalue, isStatic, isFinal, isAbstract
    if Assign_st():
        if CB():
            return True
        else:
            return False
    elif TAssign_st():
        if CB():
            return True
        else:
            return False
    elif tokenType[i] == "public":
        accessMODvalue = "public"
        print("update to p :", accessMODvalue)
        i = i + 1
        if NAMS():
            print("static true")
            if NAMF():
                print("final true")
                if MVC():
                    print("mvc true")
                    clearAccesandNonAccess()
                    # false
                    if CB():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokenType[i] == "private":
        accessMODvalue = "private"
        i = i + 1
        if NAMS():
            print("static true")
            if NAMF():
                print("final true")
                if MVC():
                    print("mvc true")
                    clearAccesandNonAccess()
                    # false
                    if CB():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokenType[i] == "static":
        isStatic = True
        i = i + 1
        if NAMF():
            print("static true")
            if MVC():
                print("mvc true")
                clearAccesandNonAccess()
                # false
                if CB():
                    return True
                else:
                    return False
            else:
                return False
    elif tokenType[i] == "final":
        i = i + 1
        if MVC():
            print("mvc true")
            if CB():
                return True
            else:
                return False
        else:
            return False
    elif MVC():
        if CB():
            return True
        else:
            return False
    else:
        return True


def class_def():
    global i, tokenType, extendingClass, multipleInterface, mainTableTypeMOD, mainTableType, currentClass
    if tokenType[i] == "final":
        print("final read")
        mainTableTypeMOD = "final"
        i = i + 1
        if tokenType[i] == "class":
            print("class match")
            mainTableType = "class"
            i = i + 1
            if tokenType[i] == "identifier":
                currentClass = tokenValue[i]
                i = i + 1
                if INH():
                    notExist, theRanError = insertMainTable(
                        currentClass,
                        mainTableType,
                        mainTableTypeMOD,
                        extendingClass,
                        multipleInterface,
                    )
                    print(notExist, "the result")
                    print("after insertion")
                    if tokenType[i] == "opencurlybrace" and notExist:
                        i = i + 1
                        if CB():
                            print("CB TRUE")
                            if tokenType[i] == "closecurlybrace":
                                currentClass = ""
                                extendingClass = ""
                                multipleInterface = []
                                mainTableTypeMOD = ""
                                mainTableType = ""
                                print("class curly")
                                i = i + 1
                                return True
                            else:
                                frameinfo = getframeinfo(currentframe())
                                print(
                                    "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                    frameinfo.lineno,
                                )
                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        if notExist == False:
                            theERROR = theRanError , calclateLineNo(i)
                            errorList.append(theERROR)
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    elif tokenType[i] == "class":
        mainTableType = "class"
        i = i + 1
        if tokenType[i] == "identifier":
            currentClass = tokenValue[i]
            i = i + 1
            if INH():
                notExist , theRanError = insertMainTable(
                    currentClass,
                    mainTableType,
                    mainTableTypeMOD,
                    extendingClass,
                    multipleInterface,
                )
                print(notExist, "the result")
                print("after insertion")
                if tokenType[i] == "opencurlybrace" and notExist:
                    i = i + 1
                    if CB():
                        print("CB TRUE",tokenType[i])
                        if tokenType[i] == "closecurlybrace":
                            currentClass = ""
                            extendingClass = ""
                            multipleInterface = []
                            mainTableTypeMOD = ""
                            mainTableType = ""
                            print("class curly")
                            i = i + 1
                            return True
                        else:
                            frameinfo = getframeinfo(currentframe())
                            print(
                                "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                frameinfo.lineno,
                            )
                            errorMesssage(i)
                            return False
                    else:
                        return False
                else:
                    if notExist == False:
                        theError = theRanError , calclateLineNo(i)
                        errorList.append(theError)
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def interface_def():
    global i, tokenType, extendingClass, multipleInterface, mainTableTypeMOD, mainTableType, currentClass
    if tokenType[i] == "interface":
        mainTableType = "interface"
        i = i + 1
        if tokenType[i] == "identifier":
            currentClass = tokenValue[i]
            i = i + 1
            if int_INH():
                notExist, theRanError = insertMainTable(
                    currentClass,
                    mainTableType,
                    mainTableTypeMOD,
                    extendingClass,
                    multipleInterface,
                )
                print(notExist, "the result")
                if tokenType[i] == "opencurlybrace" and notExist:
                    i = i + 1
                    if int_B():
                        if tokenType[i] == "closecurlybrace":
                            currentClass = ""
                            extendingClass = ""
                            multipleInterface = []
                            mainTableTypeMOD = ""
                            mainTableType = ""
                            print("class curly interface")
                            i = i + 1
                            return True
                        else:
                            frameinfo = getframeinfo(currentframe())
                            print(
                                "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                frameinfo.lineno,
                            )
                            errorMesssage(i)
                            return False
                    else:
                        return False
                else:
                    if notExist == False:
                        theERROR = theRanError , calclateLineNo(i)
                        errorList.append(theERROR)
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def abs_func_def():
    global i, tokenType,highestScope
    if tokenType[i] == "abstract":
        print("BAS MATCH")
        i = i + 1
        if RDT():
            if tokenType[i] == "def":
                i = i + 1
                if tokenType[i] == "identifier":
                    i = i + 1
                    if tokenType[i] == "openroundbrace":
                        highestScope = createScope()
                        i = i + 1
                        if PARAM():
                            if tokenType[i] == "closeroundbrace":
                                destroyScope()
                                i = i + 1
                                if tokenType[i] == "terminator":
                                    i = i + 1
                                    return True
                                else:
                                    frameinfo = getframeinfo(currentframe())
                                    print(
                                        "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                        frameinfo.lineno,
                                    )
                                    errorMesssage(i)
                                    return False
                            else:
                                frameinfo = getframeinfo(currentframe())
                                print(
                                    "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                    frameinfo.lineno,
                                )
                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    frameinfo = getframeinfo(currentframe())
                    print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                    errorMesssage(i)
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def abs_B():
    global i, tokenType
    print("in abs")
    if Assign_st():
        if abs_B():
            return True
        else:
            return False
    elif TAssign_st():
        if abs_B():
            return True
        else:
            return False
    elif tokenType[i] == "public":
        i = i + 1
        if NAMS():
            print("static true")
            if NAMF():
                print("final true")
                if MVA():
                    print("mvc true")
                    if abs_B():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokenType[i] == "private":
        i = i + 1
        if NAMS():
            print("static true")
            if NAMF():
                print("final true")
                if MVA():
                    print("mvc true")
                    if abs_B():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokenType[i] == "static":
        i = i + 1
        if NAMF():
            print("static true")
            if MVA():
                print("mvc true")
                if abs_B():
                    return True
                else:
                    return False
            else:
                return False
    elif tokenType[i] == "final":
        i = i + 1
        if MVA():
            print("mvc true")
            if abs_B():
                return True
            else:
                return False
        else:
            return False
    elif MVA():
        if abs_B():
            return True
        else:
            return False
    else:
        return True


def abs_class_def():
    global i, tokenType, extendingClass, multipleInterface, mainTableTypeMOD, mainTableType, currentClass
    if tokenType[i] == "abstract":
        mainTableTypeMOD = "abstract"
        i = i + 1
        if tokenType[i] == "class":
            mainTableType = "class"
            i = i + 1
            if tokenType[i] == "identifier":
                currentClass = tokenValue[i]
                i = i + 1
                if INH():
                    notExist, extendsClass = insertMainTable(
                        currentClass,
                        mainTableType,
                        mainTableTypeMOD,
                        extendingClass,
                        multipleInterface,
                    )
                    print(notExist, "the result")
                    if tokenType[i] == "opencurlybrace" and notExist:
                        i = i + 1
                        if abs_B():
                            if tokenType[i] == "closecurlybrace":
                                currentClass = ""
                                extendingClass = ""
                                multipleInterface = []
                                mainTableTypeMOD = ""
                                mainTableType = ""
                                print("abstract class curly")
                                i = i + 1
                                return True
                            else:
                                frameinfo = getframeinfo(currentframe())
                                print(
                                    "ERROR MESSAGE LINE NUMBER IN SMEANTIC:",
                                    frameinfo.lineno,
                                )
                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        if notExist == False:
                            theERROR = extendsClass , calclateLineNo(i)
                            errorList.append(theERROR)
                        frameinfo = getframeinfo(currentframe())
                        print(
                            "ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno
                        )
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                frameinfo = getframeinfo(currentframe())
                print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
                errorMesssage(i)
                return False
        else:
            frameinfo = getframeinfo(currentframe())
            print("ERROR MESSAGE LINE NUMBER IN SMEANTIC:", frameinfo.lineno)
            errorMesssage(i)
            return False
    else:
        return False


def defs():
    global i, tokenType
    if class_def():
        print("norm")
        if defs():
            return True
    elif interface_def():
        print("int is true")
        if defs():
            return True
    elif abs_class_def():
        print("abs class")
        if defs():
            return True
    elif enum_def():
        if defs():
            return True
    else:
        return True


def NAM():
    global i, tokenType
    if tokenType[i] == "final":
        i = i + 1
        return True
    else:
        return True


def structure():
    global i, tokenType

    if defs():
        if tokenType[i] == "EOF":
            print("defs true")
            return True
        else:
            return False
    else:
        return False


def syntaxAnalyzer():
    if structure():
        return True
    else:
        return False


result = syntaxAnalyzer()
mainCount = 0
print(
    "                           -------------BACK tracking Print Statement----------------------------------"
)
print("*****************************************************************************")
if result and len(errorList)>0:
    print("parsed unconditionaly!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")

if result and len(errorList) == 0:
    print("                         >>>>>>>>>>>Parsed Successfully<<<<<<<<<<<<<")
elif len(errorList) != 0:
    print("ERROR <>>>>>>>>>>>", errorList[0])
else:
    print("error in line :", calclateLineNo(i))
    # print("error in line :", calclateLineNo(i), allLines[i])
print(
    "                             -------------------ERROR LIST------------------------------------------------"
)
print(errorList)
print(
    "                              -------------------MAIN TABLES------------------------------------------------"
)
print("TOTAL OBJ REF <>>>>>>>> :", len(mainTable_))
for i in mainTable_:
    print("---------CLASS NAME:", i.getName())
    print("-----------------------------------------START OF MAIN TABLE ------------------------------------------------")
    print(vars(i))
    print("-----------------------------------------END OF MAIN TABLE ------------------------------------------------")
    # print("-----------------------------------------END OF MAIN & START OF DATA TABLE ------------------------------------------------")
    for j in i.attrTable:
        # print("-----------------------------------------START OF DATA TABLE ------------------------------------------------")
        if j.name == "main" and j.type == ['->',"void"] and j.static == True and j.accessMod == "public" :
            mainCount  = mainCount+1
        print("attributes---")
        print(vars(j))
    print("-----------------------------------------END OF DATA TABLE ------------------------------------------------")
print(
    "                            -------------------function TABLE------------------------------------------------"
)
if mainCount == 0:
    print("---------------------------------------NO MAIN METHOD FOUND !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
if mainCount > 1:
    print("-----------------------------------------MULTIPLR MAIN METHOD FOUND !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for i in functionTable_:
    print(vars(i))
print("************************************ EOC *****************************************")
