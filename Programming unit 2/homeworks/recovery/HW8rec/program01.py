import images

def controlOneColor(lst, color): 
    for i in lst:
        if i!= color:
            return False
    else:
        return True

def processImage(matrix, color, colorlist): #startimage 
 
    for el, line in enumerate(matrix):
        if controlOneColor(line, line[0]):
            if line[0] == color:
                return colorlist
            else:    
                colorlist.append(line[0])
                for v in range(len(line)):
                    if matrix[el-1][v]!= line[0]:
                        continue
                    else:
                        break
    
                updx = [sect[v+1:] for sect in matrix[:el]]
                upsx = [sect[:v] for sect in matrix[:el]]
                ddx = [sect[v+1:] for sect in matrix[el+1:]]
                dsx = [sect[:v] for sect in matrix[el+1:]]
                
                colorlist = processImage(ddx, color, colorlist)
                colorlist = processImage(dsx, color, colorlist)                
                colorlist = processImage(updx, color, colorlist)
                colorlist = processImage(upsx, color, colorlist)
             
    return colorlist 

def ex1(input_file,  output_file):
 
    matrix = images.load(input_file)
    bgcol = matrix[0][0]
    colorlist = processImage(matrix, bgcol, [bgcol])
    images.save([colorlist], output_file)
    return ((len(colorlist)-1)*3)+1

if __name__ == '__main__':
    # write your tests here
    pass