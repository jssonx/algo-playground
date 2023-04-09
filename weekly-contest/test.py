def find_overlaps(ranges):
    ranges.sort()
    start, end = ranges[0]
    overlaps = []
    items_num = 1
    for i in range(1, len(ranges)):
        left, right = ranges[i]
        if left <= end:
            end = max(end, right)
            # overlaps.append([left, right])
        else:
            overlaps.append([start, end])
            start, end = left, right
            items_num += 1
    overlaps.append([start, end])
    return items_num, overlaps


# ranges = [[1,3],[10,20],[2,5],[4,8]]
ranges = [[0,0],[8,9],[12,13],[1,3]]
overlaps = find_overlaps(ranges)
print(overlaps)  # 输出 [[1, 3], [2, 5], [4, 8]] 和 [[10, 20], [12, 15]]
