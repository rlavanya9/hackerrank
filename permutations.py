def permutations(x,y,z,n):
    output = []
    for i in [x,y,z]:
        for j in [x,y,z]:
                output.append([i,j])
    return output

print(permutations(1,0,3,2))
    
