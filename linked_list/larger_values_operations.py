def add(a,b):
    l1 = []
    l2 = []
    result = []
    buffer = 0
    info_a = 0
    info_b = 0
    #currently not supporting decimal numbers in addition
    """ checking for decimal numbers
    count_a = 0 # holds the count of number of digits after decimal in a
    count_b = 0 # holds the count of number of digits after decimal in b
    # In case of decimal numbers ,counting number of digits after decimal
    w = 0 # holds the position of decimal in a
    v = 0 # holds the position of decimal in b
    count_ab = 0 # holds the count_a or count_b which ever is greater
    if "." in a:
        for i in range(len(a)):
            if a[i] == ".":
                w = i#print(i)
                break
        for i in range(w+1,len(a)):
            count_a += 1
        #print(count_a)

    elif "." in b:
        for i in range(len(b)):
            if b[i] == ".":
                p = i#print(i)
                break
        for i in range(v+1,len(b)):
            count_b += 1
        #print(count_b)
    if count_a > count_b:
        count_ab = count_a
    else:
        count_ab = count_b"""

    # Inserting values of a and b in l1 and l2 

    t = len(a)-1
    if a[0] == '-':
        while t >= 1:
            l1.append(a[t])
            t-=1
    else:
        while t >= 0:
            l1.append(a[t])
            t-=1


    y = len(b)-1
    if b[0] == '-':
        while y >= 1:
            l2.append(b[y])
            y-=1
    else:
        while y >= 0:
            l2.append(b[y])
            y-=1
    #print(l1)
    #print(l2)
    
    # Finding if a is greater than b or not
    
    if len(l1) !=  len(l2):
        if len(l1) > len(l2):
            info_a += 1
        else:
            info_b += 1
            
        # making lenth of list l1 and l2 equal

        if len(l1) > len(l2):
            k = len(l2)
            while k <= len(l1)-1:
                l2.append('0')
                k += 1
        else:
            k = len(l1)
            while k <= len(l2)-1:
                l1.append('0')
                k += 1
        
    else:
        r = len(l1) - 1
        while r >= 0:
            if int(l1[r]) > int(l2[r]):
                info_a += 1
                break
            elif int(l2[r]) > int(l1[r]):
                info_b += 1
                break
            r -= 1
    #print(info_a)
    #print(info_b)
    # checking fo the case where we need to subtract the two operands
    if a[0] == '-' and b[0] != '-':
        if info_a == 1:
            op1 = "".join(l1[::-1])
            op2 = "".join(l2[::-1])
        else:
            op1 = "".join(l2[::-1])
            op2 = "".join(l1[::-1])
        
        b = sub(op1,op2)
        #print(b)
        #sprint(info_a)
        if info_a == 1:
            return "-"+b
        else:
            return b
                       
    elif a[0] != '-' and b[0] == '-':
        if info_a == 1:
            op1 = "".join(l1[::-1])
            op2 = "".join(l2[::-1])
        else:
            op1 = "".join(l2[::-1])
            op2 = "".join(l1[::-1])

        b = sub(op1,op2)

        if info_b == 1:
            return "-"+b
        else:
            return b
    
    # process of addition
    i = 0
    while i <= len(l1) - 1:
        n = str(int(l1[i]) + int(l2[i]) + int(buffer))
        buffer = 0
        if len(n) > 1:
            result.append(int(n[1]))
            #print(result,type(result))
            buffer = int(n[0])
        else:
            result.append(int(n[0]))
        i += 1
        if i == len(l1) and buffer != 0:
            result.append(buffer)
    #print(type(result[0]))
    
    # Displaying the value after all the operation is done 
    if a[0] == '-' and b[0] == '-':
        """if '.' in a or '.' in b:
            result_var = "-"+"".join(str(u) for u in result[::-1])
            ad = len(result_var) - count_ab
            return result_var[0:ad+1] + '.' + result_var[ad+1:len(result_var)]
        else:"""
        return "-"+"".join(str(u) for u in result[::-1])
        
    elif a[0] != '-' and b[0] != '-':
        """if '.' in a or '.' in b:
            result_var = "".join(str(u) for u in result[::-1])
            ad = len(result_var) - count_ab
            return result_var[0:ad] + '.' + result_var[ad:len(result_var)]
        else:"""
        return "".join(str(u) for u in result[::-1])
    
    
        
#######################################################################################################

def sub(a,b):
    l1 = []
    l2 = []
    result = []
    info_a = 0 # if this value changes to 1 then a is greater
    info_b = 0 # if this value changes to 1 then b is greater
    #currently not supporting decimal numbers in addition
    """checking for decimal numbers
    count_a = 0 # holds the count of number of digits after decimal in a
    count_b = 0 # holds the count of number of digits after decimal in b
    # In case of decimal numbers ,counting number of digits after decimal
    w = 0 # holds the position of decimal in a
    v = 0 # holds the position of decimal in b
    count_ab = 0 # holds the count_a or count_b which ever is greater
    if "." in a:
        for i in range(len(a)):
            if a[i] == ".":
                w = i#print(i)
                break
        for i in range(w+1,len(a)):
            count_a += 1
        #print(count_a)

    elif "." in b:
        for i in range(len(b)):
            if b[i] == ".":
                p = i#print(i)
                break
        for i in range(v+1,len(b)):
            count_b += 1
        #print(count_b)
    if count_a > count_b:
        count_ab = count_a
    else:
        count_ab = count_b"""
    
    # adding elements of a and b in list l1 and l2
    
    t = len(a)-1    
    if a[0] == '-':
        while t >= 1:
            l1.append(a[t])
            t-=1
    else:
        while t >= 0:
            l1.append(a[t])
            t-=1

    y = len(b)-1
    if b[0] == '-':
        while y >= 1:
            l2.append(b[y])
            y-=1
    else:
        while y >= 0:
            l2.append(b[y])
            y-=1
    #print(l2)
    #print(l1)

    # Finding if a is greater than b or not
    
    if len(l1) !=  len(l2):
        if len(l1) > len(l2):
            info_a += 1
        else:
            info_b += 1
            
        # making lenth of list l1 and l2 equal

        if len(l1) > len(l2):
            k = len(l2)
            while k <= len(l1)-1:
                l2.append('0')
                k += 1
        else:
            k = len(l1)
            while k <= len(l2)-1:
                l1.append('0')
                k += 1
        
    else:
        r = len(l1) - 1
        while r >= 0:
            if int(l1[r]) > int(l2[r]):
                info_a += 1
                break
            elif int(l2[r]) > int(l1[r]):
                info_b += 1
                break
            r -= 1
    #print(l2)
    #print(l1)
    # checking for the case where we need to add the two operands
    if a[0] == "-" and b[0] != "-":
        op1 = "".join(l1[::-1])
        op2 = "".join(l2[::-1])
        
        b = add(op1,op2)
        return "-"+b
        
                       
    elif a[0] != "-" and b[0] == "-":
        op1 = "".join(l1[::-1])
        op2 = "".join(l2[::-1])

        b = add(op1,op2)
        return b
    
    # subtraction process
    if info_a == 1 and info_b != 1:
        i = 0
        #x = 0
        while i <= len(l1) - 1:
            if int(l1[i]) >= int(l2[i]):
                x = int(l1[i]) - int(l2[i])
                result.append(x)
            else:
                x = (int(l1[i]) + 10) - int(l2[i])
                result.append(x)
                #print(result)
                if int(l1[i+1]) != 0 and i+1 <= len(l1):
                    l1[i+1] = int(l1[i+1]) - 1
                else:
                    j = i
                    while int(l1[j+1]) == 0 and j+1 <= len(l1):
                        j =+ 1
                    l1[j+1] = int(l1[j+1]) - 1
                    while j != i:
                        l1[j] = 9
                        j = j - 1
            i += 1
    else: # info_a != 1 and info_b == 1
        i = 0
        while i <= len(l2) - 1:
            if int(l2[i]) >= int(l1[i]):
                x = int(l2[i]) - int(l1[i])
                #print(x)
                result.append(x)
            else:
                x = (int(l2[i]) + 10) - int(l1[i])
                #print(x)
                result.append(x)
                #print(result)
                if int(l2[i+1]) != 0 and i+1 <= len(l2)-1:
                    l2[i+1] = int(l2[i+1]) - 1
                else:
                    j = i
                    while int(l2[j+1]) == 0 and j+1 <= len(l2)-1:
                        j =+ 1
                    l2[j+1] = int(l2[j+1]) - 1
                    while j != i:
                        l2[j] = 9
                        j = j - 1
            i += 1
            #print(l2[i])
    #print(result)
    #jk = "".join(str(u) for u in result[::-1])
    #print(type(jk))
    if (a[0] != '-' and b[0] != '-') and (info_a == 1 and info_b == 0):
        """if '.' in a or '.' in b:
            result_var = "".join(str(u) for u in result[::-1])
            ad = len(result_var) - count_ab# whcih ever is greater count_a or count_b
            return result_var[0:ad] + '.' + result_var[ad:len(result_var)]
        else:""" 
        return "".join(str(u) for u in result[::-1])
    elif (a[0] != '-' and b[0] != '-') and (info_a == 0 and info_b == 1):
        """if '.' in a or '.' in b:
            result_var = "-"+"".join(str(u) for u in result[::-1])
            ad = len(result_var) - count_ab
            return result_var[0:ad+1] + '.' + result_var[ad+1:len(result_var)]
        else:"""
        return "-"+"".join(str(u) for u in result[::-1])
    elif (a[0] == '-' and b[0] == '-') and (info_a == 0 and info_b == 1):
        """if '.' in a or '.' in b:
            result_var = "".join(str(u) for u in result[::-1])
            ad = len(result_var) - count_ab
            return result_var[0:ad] + '.' + result_var[ad:len(result_var)]
        else:"""
        return "".join(str(u) for u in result[::-1])
    elif (a[0] == '-' and b[0] == '-') and (info_a == 1 and info_b == 0):
        """if '.' in a or '.' in b:
            result_var = "-"+"".join(str(u) for u in result[::-1])
            ad = len(result_var) - count_ab
            return result_var[0:ad+1] + '.' + result_var[ad+1:len(result_var)]

        else:"""
        return "-"+"".join(str(u) for u in result[::-1])
        
################################################################################
# supporting decimal numbers in operation
def mul(a,b):
    l1 = []
    l2 = []
    result_temp = []
    result = []
    buffer = 0
    count_a = 0 # holds the count of number of digits after decimal in a
    count_b = 0 # holds the count of number of digits after decimal in b
    # In case of decimal numbers ,counting number of digits after decimal
    w = 0 # holds the position of decimal in a
    p = 0 # holds the position of decimal in b
    if "." in a:
        for i in range(len(a)):
            if a[i] == ".":
                w = i#print(i)
                break
        for i in range(w+1,len(a)):
            count_a += 1
        #print(count_a)

    if "." in b:
        for i in range(len(b)):
            if b[i] == ".":
                p = i#print(i)
                break
        for i in range(p+1,len(b)):
            count_b += 1
        #print(count_b)
    
    # adding elements of a and b in list l1 and l2
    
    t = len(a)-1    
    if a[0] == '-':
        while t >= 1:
            if a[t] == ".":
                t-=1
                continue
            else:
                l1.append(a[t])
            #l1.append(a[t])
            t-=1
    else:
        while t >= 0:
            if a[t] == ".":
                t-=1
                continue
            else:
                l1.append(a[t])
            #l1.append(a[t])
            t-=1

    y = len(b)-1
    if b[0] == '-':
        while y >= 1:
            if b[y] == ".":
                y-=1
                continue
            else:
                l2.append(b[y])
            y-=1
    else:
        while y >= 0:
            if b[y] == ".":
                y-=1
                continue
            else:
                l2.append(b[y])
            y-=1
    #print(l1)
    #print(l2)
    
    # multiplication process
    for i in range(len(l2)):
        for j in range(len(l1)):
            x = str((int(l1[j]) * int(l2[i])) + int(buffer))
            #print(x)
            buffer = 0
            if len(x) > 1:
                result.append(x[1])
                buffer = x[0]
            else:
                result.append(x)
            if j == len(l1)-1 and buffer != 0:
                result.append(buffer)
                buffer = 0
            #print(buffer)
        result_temp.append(result)
        result = []
    #print(type(result_temp[0][0]))
    for i in range(len(result_temp)):
        result_temp[i] = result_temp[i][::-1]
    #print(result_temp)
    
    temp = add("0","".join(result_temp[len(result_temp)-1])+"0")
    #print(temp)
    #print("".join(result_temp[0]))
    
    j = len(result_temp)-2
    while j >= 0:
        s1 = "".join(result_temp[j])
        temp = add(s1,temp)
        
        if j == 0:
            if (a[0] != '-' and b[0] != '-') :
                if '.' in a or '.' in b:
                    #op = len(temp) - (count_a + count_b)
                    op = int(sub(str(len(temp)) , add(str(count_a),str(count_b))))
                    return temp[0:op] + '.' + temp[op:len(temp)]
                else:
                    return temp

            elif (a[0] == '-' and b[0] != '-'):
                if '.' in a or '.' in b:
                    #op = len(temp) - (count_a + count_b)
                    op = int(sub(str(len(temp)) , add(str(count_a),str(count_b))))
                    return '-' + temp[0:op] + '.' + temp[op:len(temp)]
                else:
                    return '-' + temp

            elif (a[0] != '-' and b[0] == '-') :
                if '.' in a or '.' in b:
                    op = int(sub(str(len(temp)) , add(str(count_a),str(count_b))))
                    #op = len(temp) - (count_a + count_b)
                    return '-' + temp[0:op] + '.' + temp[op:len(temp)]
                else:
                    return '-' + temp

            else:
                if '.' in a or '.' in b:
                    op = len(temp) - (count_a + count_b)
                    return temp[0:op] + '.' + temp[op:len(temp)]
                else:
                    return temp
        else:
            temp = temp+"0"
        j -= 1

    
    
        
a = input("enter first operand:")
b = input("Enter second operand:")
print("result of subtraction:",sub(a,b))    
print("result of addition:",add(a,b))
print("result of multiplication:",mul(a,b))

