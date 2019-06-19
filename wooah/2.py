def solution(lands, wells, point):
    x1,y1,x2,y2 = point
    for land in lands:
        if land == point: #기존의 토지와 완전 동일한 경우
            return False
        lx1, ly1, lx2, ly2 = land
        #기존의 토지에 걸쳐있는경우
        if (lx1<x1 and x1<lx2) or (lx1<x2 and x2<lx2):
            if (ly1<y1 and y1<ly2) or (ly1<y2 and y2<ly2):
                return False
        #기존의 토지를 감싸고 있는경우
        if (x1<lx1 and lx1<x2) or (x1<lx2 and lx2<x2):
            if (y1<ly1 and ly1<y2) or (y1<ly2 and ly2<y2):
                return False

    for well in wells:
        if well == point: #호수와 완전히 겹치는 경우
            return True
        wx1, wy1, wx2, wy2 = well
        #호수에 걸쳐있는 경우
        if (wx1<x1 and x1<wx2) or (wx1<x2 and x2<wx2):
            if (wy1<y1 and y1<wy2) or (wy1<y2 and y2<wy2):
                return True
        #호수를 감싸고 있는 경우
        if (x1<wx1 and wx1<x2) or (x1<wx2 and wx2<x2):
            if (y1<wy1 and wy1<y2) or (y1<wy2 and wy2<y2):
                return True
    return False
