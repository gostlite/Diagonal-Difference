def diagonalDiffernce(arr):
    left_to_right =0
    right_to_left = 0
    k = 0
    #  getting the first. second and last elements
    for a in arr:       
        # print(a[k]) 
        left_to_right+=a[k]      
        k+=1 
        #  getting the last. second and first elements
    for b in arr:
        k-=1
        print(b[k])
        right_to_left+=b[k]
    # teturn the absolute value
    return abs(left_to_right - right_to_left)
        
