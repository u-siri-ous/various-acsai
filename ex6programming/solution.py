import images
def ex15(fimm1,fimm2,fimm3):
    img1 = images.load(fimm1)
    img2 = images.load(fimm2)
    height = max(len(img1), len(img2))
    width = max(len(img1[0]), len(img2[0]))
    counter = 0
    result = []
    for h in range(0, height):
      row = []
      for w in range(0, width):
        if(is_inside(h, w, img1) and is_inside(h, w, img2)):
          row.append((0,0,0))
          counter += 1
        elif(not is_inside(h, w, img1) and not is_inside(h, w, img2)):
          row.append((0,0,0))
          counter += 1
        elif(is_inside(h, w, img1) and not is_inside(h, w, img2)):
          row.append(img1[h][w])
          if(img1[h][w] == (0,0,0)):
            counter += 1
        elif(is_inside(h, w, img2) and not is_inside(h, w, img1)):
          row.append(img2[h][w])
          if(img2[h][w] == (0,0,0)):
            counter += 1
      result.append(row)
    images.save(result, fimm3)
    return counter
    

def is_inside(x, y, l):
    if(x<len(l) and y<len(l[0])):
        return True
    return False
