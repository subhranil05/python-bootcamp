if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    x1 = [i for i in range(x+1) ]
    
    y1 = [j for j in range(y+1) ]
    
    z1 = [k for k in range(z+1) ]
    
    
    req_list = [[i,j,k] for i in x1 for j in y1 for k in z1]
    
    out_list = [l for l in req_list if sum(l) != n]
    
    print(out_list)