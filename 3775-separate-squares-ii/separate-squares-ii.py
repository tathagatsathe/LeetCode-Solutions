class SegmentTree:
    def __init__(self, cords):
        self.cords = cords
        n = len(cords)
        self.tree = [0]*(4*n)
        self.total_len = [0]*(4*n)
    
    def update(self, node, start, end, min_idx, max_idx, count):
        if max_idx <= start or min_idx >= end :
            return

        if min_idx>=start and max_idx<=end:
            self.tree[node]+=count
        else:
            mid = (min_idx + max_idx)//2
            self.update(2*node, start, end, min_idx, mid, count)
            self.update(2*node + 1, start, end, mid, max_idx, count)

        if self.tree[node] > 0:
            self.total_len[node] = self.cords[max_idx] - self.cords[min_idx]
        else:
            if max_idx - min_idx == 1:
                self.total_len[node] = 0
            else:
                self.total_len[node] = self.total_len[2*node] + self.total_len[2*node + 1]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        x_cords = set()
        y_cords = set()
        events = []

        for x, y, side in squares:
            x_cords.add(x)
            x_cords.add(x+side)
            y_cords.add(y)
            y_cords.add(y+side)
            events.append([y, 1, x, x+side])
            events.append([y+side, -1, x, x+side])

        events.sort()

        x_cords = sorted(list(x_cords))
        x_map = {val:i for i, val in enumerate(x_cords)}

        totalArea = 0

        sgtree = SegmentTree(x_cords)
        prev = events[0][0]
    
        low, high = min(y_cords), max(y_cords)
        strips = []
        for i in range(len(events)-1):
            y_curr, typ, x1, x2 = events[i]
            y_next = events[i+1][0]
            sgtree.update(1, x_map[x1], x_map[x2], 0, len(x_cords)-1, typ)
            if y_next > y_curr:
                width = sgtree.total_len[1]
                totalArea+= width*(y_next - y_curr)
                strips.append((y_curr, y_next, width))

        
        halfArea = totalArea/2

        area = 0

        for y_start, y_end, width in strips:
            curr_area = width * (y_end - y_start)
            if area + curr_area >= halfArea:
                return y_start + (halfArea - area)/width

            area+=curr_area

        return 0


