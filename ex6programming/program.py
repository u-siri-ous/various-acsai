

import images
def ex15(fimm1,fimm2,fimm3):
    
    '''Design a function ex15(fimm1,fimm2,fimm3) such that:
    - it receives as arguments three filenames of .PNG files. The
      files 'fimm1' and 'fimm2' store two images WITH DIFFERENT
      DIMENSIONS
    - it creates a third image and saves it in a .PNG file with name
      'fimm3'
    - it returns the number of black pixels in the created image.
    The third image is obtained from the first two. Its width is the
    maximum width between the widths of fimm1 and fimm2 and its height
    is the maximum height between the heights of fimm1 and fimm2.
    Each pixel [y][x] of the third image will be:
    - of black color (0,0,0) if a pixel [y][x] exists in both or none
      of the first two images
    - of the same color of the pixel in the only image where such a
      pixel exists.
    
    To load and save the image in PNG files, use the load and save
    functions of the images.py library.

    '''
    im1 = images.load(fimm1)
    im2 = images.load(fimm2)
    im3 = []
    
    total_w = max(len(im1[0]), len(im2[0])) #columns
    total_h = max(len(im1), len(im2)) #rows
    
    counter = 0
    black = (0,0,0)
    
    for row_i in range(total_h):
#            im1[row_i][col_i] exists
#            im1[row_i][col_i] not exists
#            one of the two exist or don't exist
        new_row = []
        for col_i in range(total_w):
            if exists(im1, row_i, col_i) and exists(im2, row_i, col_i) or not exists(im1, row_i, col_i) and not exists(im2, row_i, col_i):
                new_row.append(black)
                counter += 1
            elif exists(im1, row_i, col_i):
                new_row.append(im1[row_i][col_i])
            else:
                new_row.append(im2[row_i][col_i])
            if new_row[-1] == black:
                counter += 1
        im3.append(new_row)
    images.save(im3, fimm3)
    
    return counter

            
def exists(im, row, col):
    
    return row < len(im) and col < len(im[0])
    
    
    
