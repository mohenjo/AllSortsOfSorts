# coding=utf-8
"""정렬 알고리즘 구현

다양한 in-place 정렬 알고리즘의 코드 구현입니다.

- 정렬 알고리즘에 따라 시퀀스의 길이 또는 오브젝트 요소 타입이 제한되는 경우도 있습니다.
- 오브젝트 및 요소 타입에 따른 유효성 검사 및 예외는 별도로 처리하지 않습니다.
"""

import sys

# 재귀 깊이 재설정
sys.setrecursionlimit(10 ** 6)


# region Selection Sort

def selection_sort(arr):
    """Selection Sort"""
    length = len(arr)
    for idx in range(length - 1):
        min_idx = idx
        for subidx in range(idx + 1, length):
            if arr[subidx] < arr[min_idx]:
                min_idx = subidx
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]


# endregion

# region Bubble_Sort

def bubble_sort(arr):
    """Bubble Sort"""
    length = len(arr)
    for idx in range(length):
        for subidx in range(length - idx - 1):
            if arr[subidx] > arr[subidx + 1]:
                arr[subidx], arr[subidx + 1] = arr[subidx + 1], arr[subidx]


# endregion

# region Quick Sort

def quick_sort(arr):
    """Quick SOrt"""
    _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, startidx, endidx):
    if startidx < endidx:
        partitionidx = _partition_array(arr, startidx, endidx)
        _quick_sort(arr, startidx, partitionidx - 1)
        _quick_sort(arr, partitionidx + 1, endidx)


def _partition_array(arr, startidx, endidx):
    pivot = arr[endidx]
    pivotidx = startidx - 1
    for idx in range(startidx, endidx):
        if arr[idx] <= pivot:
            pivotidx += 1
            arr[idx], arr[pivotidx] = arr[pivotidx], arr[idx]
    arr[pivotidx + 1], arr[endidx] = arr[endidx], arr[pivotidx + 1]
    return pivotidx + 1


# endregion

# region Insertion Sort

def insertion_sort(arr):
    """Insertion Sort"""
    length = len(arr)
    for idx in range(1, length):
        keyval = arr[idx]
        subidx = idx - 1
        while subidx >= 0 and arr[subidx] > keyval:
            arr[subidx + 1] = arr[subidx]
            subidx -= 1
        arr[subidx + 1] = keyval


# endregion

# region Merge Sort

def merge_sort(arr):
    """Merge Sort"""
    length = len(arr)
    if length > 1:
        mididx = length // 2
        larr = arr[:mididx]
        rarr = arr[mididx:]
        merge_sort(larr)
        merge_sort(rarr)

        lidx, ridx, idx = 0, 0, 0
        while lidx < len(larr) and ridx < len(rarr):
            if larr[lidx] <= rarr[ridx]:
                arr[idx] = larr[lidx]
                lidx += 1
            else:
                arr[idx] = rarr[ridx]
                ridx += 1
            idx += 1
        while lidx < len(larr):
            arr[idx] = larr[lidx]
            idx += 1
            lidx += 1
        while ridx < len(rarr):
            arr[idx] = rarr[ridx]
            idx += 1
            ridx += 1


# endregion

# region Heap Sort

def heap_sort(arr):
    """Heap Sort"""
    length = len(arr)
    for idx in range(length, -1, -1):
        _heapify(arr, idx, length)
    # 크기 순 정렬
    for idx in range(length - 1, 0, -1):
        arr[idx], arr[0] = arr[0], arr[idx]
        _heapify(arr, 0, idx)


def _heapify(arr, idx, heapsize):
    largest_idx = idx
    lidx = 2 * idx + 1
    ridx = 2 * idx + 2
    if lidx < heapsize and arr[lidx] > arr[largest_idx]:
        largest_idx = lidx
    if ridx < heapsize and arr[ridx] > arr[largest_idx]:
        largest_idx = ridx
    # 힙의 정렬이 필요할 경우
    if largest_idx != idx:
        arr[largest_idx], arr[idx] = arr[idx], arr[largest_idx]
        _heapify(arr, largest_idx, heapsize)


# endregion

# region Counting Sort

def counting_sort(arr):
    """Counting Sort

    Args:
        arr: 음이 아닌 정수를 요소로 가져야합니다.
    """
    length = len(arr)
    max_val = max(arr)
    # 정렬된 시퀀스
    output = [None for _ in range(length)]
    # 입력 리스트 각 요소의 개수를 저장할 시퀀스
    count = [0 for _ in range(max_val + 1)]

    # 입력 리스트 요소 값에 해당하는 카운트 시퀀스의 인덱스에 대해 값을 1 증가시킴
    for val in arr:
        count[val] += 1
    # 카운트 시퀀스 누적
    for idx in range(1, max_val + 1):
        count[idx] += count[idx - 1]
    # 카운트 시퀀스로부터 정렬 시퀀스 구성
    for idx in range(length - 1, -1, -1):
        idx_in_count = arr[idx]
        output[count[idx_in_count] - 1] = arr[idx]
        count[idx_in_count] -= 1
    # 입력 리스트 변경
    arr[:] = output[:]


# endregion

# region Radix Sort

def _count_sort_in_radix_sort(arr, exp):
    """Radix Sort에 사용되는 Counting Sort (자리수별)

    Args:
        arr: 정렬 대상 시퀀스
        exp: 10^n 자리를 나타냄. (100의 자리: exp = 10^2)
    """
    length = len(arr)
    # 정렬된 시퀀스
    output = [None for _ in range(length)]
    # 각 자리의 숫자 [0..10)에 대응하는 카운트 시퀀스
    count = [0 for _ in range(10)]
    # 입력 리스트 요소 값(자리수별)에 해당하는 카운트 시퀀스의 인덱스에 대해
    # 값을 1 증가시킴
    for idx in range(length):
        count[(arr[idx] // exp) % 10] += 1
    # 카운트 시퀀스 누적
    for idx in range(1, 10):
        count[idx] += count[idx - 1]
    # 정렬 시퀀스 구성
    for idx in range(length - 1, -1, -1):
        idx_in_count = (arr[idx] // exp) % 10
        output[count[idx_in_count] - 1] = arr[idx]
        count[idx_in_count] -= 1
    # 입력 리스트 변경
    arr[:] = output[:]


def radix_sort(arr):
    """Radix Sort

    Args:
        arr: 음이 아닌 정수를 요소로 가져야합니다.
    """
    import math

    max_val = max(arr)
    # int(math.log10(9999) -> 1000의 자리 = 10^3 -> = 3
    for digit in range(int(math.log10(max_val)) + 1):
        _count_sort_in_radix_sort(arr, 10 ** digit)


# endregion

# region Bucket Sort

def bucket_sort(arr):
    """Bucket Sort"""
    length = len(arr)
    max_val = max(arr)
    # 버킷 구성
    buckets = [[] for _ in range(length)]
    # 버킷에 값 할당
    for val in arr:
        bucket_idx = int(val * length / (max_val + 1))
        buckets[bucket_idx].append(val)
    # 각 버킷 정렬 및 정렬 시퀀스 재구성
    # - 각 버킷 내 정렬에는 퀵 정렬 사용
    pos = 0
    for bucket in buckets:
        quick_sort(bucket)
        blength = len(bucket)
        arr[pos: pos + blength] = bucket
        pos += blength


# endregion

# region Shell Sort

def shell_sort(arr):
    """Shell Sort"""
    length = len(arr)

    gap = length // 2  # 초기 간격
    # gap == 1 일 때까지 반복
    while gap > 0:
        for idx in range(gap, length):
            cur_val = arr[idx]
            pos = idx
            while pos >= gap and arr[pos - gap] > cur_val:
                arr[pos] = arr[pos - gap]
                pos -= gap
            arr[pos] = cur_val
        gap //= 2


# endregion

# region Tim Sort

def _insertion_sort_in_tim_sort(arr, lidx, ridx):
    """Insertion Sort for Tim Sort"""
    for idx in range(lidx + 1, ridx + 1):
        keyval = arr[idx]
        subidx = idx - 1
        while subidx >= lidx and arr[subidx] > keyval:
            arr[subidx + 1] = arr[subidx]
            subidx -= 1
        arr[subidx + 1] = keyval


def _merge_sort_in_tim_sort(arr, lidx, midx, ridx):
    """Merge Sort for Tim Sort"""
    llen = midx - lidx + 1
    rlen = ridx - midx
    larr = arr[lidx:midx + 1]
    rarr = arr[midx + 1:ridx + 1]

    sublidx, subridx, subidx = 0, 0, lidx
    while sublidx < llen and subridx < rlen:
        if larr[sublidx] <= rarr[subridx]:
            arr[subidx] = larr[sublidx]
            sublidx += 1
        else:
            arr[subidx] = rarr[subridx]
            subridx += 1
        subidx += 1
    while sublidx < llen:
        arr[subidx] = larr[sublidx]
        subidx += 1
        sublidx += 1
    while subridx < rlen:
        arr[subidx] = rarr[subridx]
        subidx += 1
        subridx += 1


def tim_sort(arr):
    """Tim Sort"""
    length = len(arr)
    run = 32

    for lidx in range(0, length, run):
        ridx = min(lidx + run - 1, length - 1)
        _insertion_sort_in_tim_sort(arr, lidx, ridx)

    cur_size = run
    while cur_size < length:
        for lidx in range(0, length, cur_size * 2):
            midx = min(lidx + cur_size - 1, length - 1)
            ridx = min(lidx + 2 * cur_size - 1, length - 1)
            _merge_sort_in_tim_sort(arr, lidx, midx, ridx)
        cur_size *= 2


# endregion

# region Comb Sort

def comb_sort(arr):
    """Comb Sort"""
    length = len(arr)
    gap = length
    is_swapped = True
    while gap > 1 or is_swapped:
        nextgap = gap / 1.3
        gap = int(nextgap) if nextgap > 1 else 1
        is_swapped = False
        for idx in range(length - gap):
            if arr[idx] > arr[idx + gap]:
                arr[idx], arr[idx + gap] = arr[idx + gap], arr[idx]
                is_swapped = True


# endregion

# region Pigeonhole Sort

def pigeonhole_sort(arr):
    """Pigeonhole Sort"""
    max_val, min_val = max(arr), min(arr)
    size = max_val - min_val + 1

    pigeonholes = [[] for _ in range(size)]
    for val in arr:
        pigeonholes[val - min_val].append(val)

    flatten = [item for sublist in pigeonholes for item in sublist]
    for idx, val in enumerate(flatten):
        arr[idx] = val


# endregion

# region Cycle Sort

def cycle_sort(arr):
    """Cycle Sort"""
    length = len(arr)
    for cyclestart in range(length - 1):
        cur_val = arr[cyclestart]

        pos = cyclestart
        for idx in range(cyclestart + 1, length):
            if arr[idx] < cur_val:
                pos += 1
        if pos == cyclestart:
            continue

        while cur_val == arr[pos]:
            pos += 1

        if pos != cyclestart:
            arr[pos], cur_val = cur_val, arr[pos]

        while pos != cyclestart:
            pos = cyclestart

            for idx in range(cyclestart + 1, length):
                if arr[idx] < cur_val:
                    pos += 1

            while cur_val == arr[pos]:
                pos += 1

            if cur_val != arr[pos]:
                arr[pos], cur_val = cur_val, arr[pos]


# endregion

# region Cocktail Sort

def cocktail_sort(arr):
    """Cocktail Sort (Bidirectional Bubble Sort)"""
    length = len(arr)
    startidx = 0
    endidx = length - 1
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for idx in range(startidx, endidx):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                is_swapped = True
        if not is_swapped:
            break

        is_swapped = False
        endidx -= 1
        for idx in range(endidx, startidx - 1, -1):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                is_swapped = True

        startidx += 1


# endregion

# region Strand Sort

def strand_sort(arr):
    """Strand Sort"""
    outputarr = _strand_sort(arr[:])
    arr[:] = outputarr[:]


def _strand_sort(inputarr):
    import heapq

    outputarr = []

    while inputarr:
        sublist = [inputarr.pop(0)]
        idx = 0
        while idx < len(inputarr):
            curval = inputarr[idx]
            compareval = sublist[-1]
            if curval > compareval:
                sublist.append(inputarr.pop(idx))
            else:
                idx += 1

        # 정렬 머징
        outputarr = list(heapq.merge(outputarr, sublist))

    return outputarr


# endregion

# region Bitonic Sort

def bitonic_sort(arr):
    """Bitonic Sort

    Args:
        arr: 시퀀스의 길이는 2**k의 값이어야 함
    """
    _bitonic_sort(arr, 0, len(arr), "up")


def _bitonic_merge(arr, lowidx, mididx, direction: str):
    direction = direction.lower()
    if mididx > 1:
        midx = mididx // 2
        for idx in range(lowidx, lowidx + midx):
            if (direction == "up" and arr[idx] > arr[idx + midx]) or \
                    (direction == "down" and arr[idx] < arr[idx + midx]):
                arr[idx], arr[idx + midx] = arr[idx + midx], arr[idx]

        _bitonic_merge(arr, lowidx, midx, direction)
        _bitonic_merge(arr, lowidx + midx, midx, direction)


def _bitonic_sort(arr, lowidx, mididx, direction):
    if mididx > 1:
        midx = mididx // 2
        _bitonic_sort(arr, lowidx, midx, "up")
        _bitonic_sort(arr, lowidx + midx, midx, "down")
        _bitonic_merge(arr, lowidx, mididx, direction)


# endregion

# region Pancake Sort

def pancake_sort(arr):
    """Pancake Sort"""
    cur_size = len(arr)
    while cur_size > 1:
        maxidx = arr.index(max(arr[:cur_size]))
        if maxidx != cur_size - 1:
            arr[:maxidx + 1] = arr[:maxidx + 1][::-1]
            arr[:cur_size] = arr[:cur_size][::-1]
        cur_size -= 1


# endregion

# region Binary Insertion Sort

def binary_insertion_sort(arr):
    """Binary Insertion Sort"""
    # import bisect

    length = len(arr)
    for idx in range(1, length):
        keyval = arr[idx]
        subidx = idx - 1
        # keyval이 삽입될 위치를 이진 탐색으로 검색
        location = _binary_search(arr, keyval, 0, subidx)
        # bisect 내장 모듈을 사용할 수도 있음
        # parameter hi in bisect.bisect() is len(array) not index
        # location = bisect.bisect(arr, keyval, 0, subidx + 1)
        while subidx >= location:
            arr[subidx + 1] = arr[subidx]
            subidx -= 1
        arr[subidx + 1] = keyval


def _binary_search(arr, keyval, lowidx, highidx):
    """이진 탐색"""
    if highidx <= lowidx:
        return lowidx + 1 if keyval > arr[lowidx] else lowidx
    mididx = (lowidx + highidx) // 2
    if keyval == arr[mididx]:
        return mididx + 1
    if keyval > arr[mididx]:
        return _binary_search(arr, keyval, mididx + 1, highidx)
    return _binary_search(arr, keyval, lowidx, mididx - 1)


# endregion

# region Bogo Sort

def bogo_sort(arr):
    """Bogo Sort

    = Permutation Sort, Slow Sort, Shotgun Sort, or Monkey Sort

    """
    # --- permutation 이용 ---
    # import itertools
    # answer = sorted(arr)
    # fools = itertools.permutations(arr, len(arr))
    # for fool in fools:
    #     if list(fool) == answer:
    #         arr[:] = fool[:]
    #         break

    # --- 랜덤 셔플 이용 ---
    import random

    answer = sorted(arr)
    while answer != arr:
        random.shuffle(arr)


# endregion

# region Bozo Sort

def bozo_sort(arr):
    """Bozo Sort"""
    import random

    length = len(arr)
    answer = sorted(arr)
    while answer != arr:
        idx1 = random.randint(0, length - 1)
        idx2 = idx1
        while idx1 == idx2:
            idx2 = random.randint(0, length - 1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


# endregion

# region Gnome Sort

def gnome_sort(arr):
    """Gnome Sort

    = Stupid Sort
    """
    length = len(arr)
    idx = 0
    while idx < length:
        if idx == 0:
            idx += 1
        if arr[idx] >= arr[idx - 1]:
            idx += 1
        else:
            arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
            idx -= 1


# endregion

# region Sleep Sort

def sleep_sort(arr):
    """Sleep Sort

    정렬 결과가 보장되지 않음

    정렬 케이스의 크기가 커질수록, 알고리즘 내 process sleep 기간이 짧아질수록
    정확도가 낮아질 가능성이 높음
    """

    import asyncio
    output = []

    async def additem_in_sorted_order(item):
        # sleep 크기에 따라 정렬의 정확도가 변경될 수 있음
        delta = 0.001
        await asyncio.sleep(item * delta)
        output.append(item)

    asyncio.run(asyncio.wait(map(additem_in_sorted_order, arr)))

    arr[:] = output[:]


# endregion

# region Brick Sort (Odd-Even Sort)

def brick_sort(arr):
    """Brick Sort (Odd-Even Sort)"""
    length = len(arr)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for idx in range(1, length - 1, 2):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                is_sorted = False
        for idx in range(0, length - 1, 2):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                is_sorted = False


# endregion

# region Stooge Sort

def stooge_sort(arr):
    """Stooge Sort"""
    _stooge_sort(arr, 0, len(arr) - 1)


def _stooge_sort(arr, lidx, ridx):
    if lidx >= ridx:
        return
    if arr[lidx] > arr[ridx]:
        arr[lidx], arr[ridx] = arr[ridx], arr[lidx]
    if ridx - lidx + 1 > 2:
        onethird = (ridx - lidx + 1) // 3
        _stooge_sort(arr, lidx, ridx - onethird)
        _stooge_sort(arr, lidx + onethird, ridx)
        _stooge_sort(arr, lidx, ridx - onethird)


# endregion

# region Bead Sort (Gravity Sort)

def bead_sort(arr):
    """Bead Sort (Gravity Sort)

    Args:
        arr: 양의 정수를 요소로 가져야합니다.
    """
    output = []
    interarr = [0] * max(arr)
    for item in arr:
        for idx in range(item):
            interarr[idx] += 1
    for _ in arr:
        output.append(sum(1 for e in interarr if e > 0))
        interarr = [e - 1 for e in interarr]
    arr[:] = output[:][::-1]


# endregion

# region Binary Tree Sort

class _NodeBTS:
    def __init__(self, val):
        self.left_child = None
        self.right_child = None
        self.value = val


def _binary_insert_bts(root: _NodeBTS, node: _NodeBTS):
    if root is None:
        root = node
    else:
        if root.value > node.value:
            if root.left_child is None:
                root.left_child = node
            else:
                _binary_insert_bts(root.left_child, node)
        else:
            if root.right_child is None:
                root.right_child = node
            else:
                _binary_insert_bts(root.right_child, node)


def _binary_tree_sort(root: _NodeBTS, output):
    if not root:
        return None
    _binary_tree_sort(root.left_child, output)
    output.append(root.value)
    _binary_tree_sort(root.right_child, output)


def binary_tree_sort(arr):
    """Binary Tree Sort"""
    output = []
    root = _NodeBTS(arr[0])
    for val in arr[1:]:
        _binary_insert_bts(root, _NodeBTS(val))
    _binary_tree_sort(root, output)
    arr[:] = output[:]


# endregion

# region Introspective Sort

def _heap_sort_introsort(arr):
    """Heap Sort"""
    length = len(arr)
    for idx in range(length, -1, -1):
        _heapify_introsort(arr, idx, length)
    # 크기 순 정렬
    for idx in range(length - 1, 0, -1):
        arr[idx], arr[0] = arr[0], arr[idx]
        _heapify_introsort(arr, 0, idx)


def _heapify_introsort(arr, idx, heapsize):
    largest_idx = idx
    lidx = 2 * idx + 1
    ridx = 2 * idx + 2
    if lidx < heapsize and arr[lidx] > arr[largest_idx]:
        largest_idx = lidx
    if ridx < heapsize and arr[ridx] > arr[largest_idx]:
        largest_idx = ridx
    # 힙의 정렬이 필요할 경우
    if largest_idx != idx:
        arr[largest_idx], arr[idx] = arr[idx], arr[largest_idx]
        _heapify(arr, largest_idx, heapsize)


def _insertion_sort_introsort(arr, lidx, ridx):
    for idx in range(lidx + 1, ridx + 1):
        keyval = arr[idx]
        subidx = idx - 1
        while subidx >= lidx and arr[subidx] > keyval:
            arr[subidx + 1] = arr[subidx]
            subidx -= 1
        arr[subidx + 1] = keyval


def _partition_introsort(arr, startidx, endidx):
    pivot = arr[endidx]
    pivotidx = startidx - 1
    for idx in range(startidx, endidx):
        if arr[idx] <= pivot:
            pivotidx += 1
            arr[pivotidx], arr[idx] = arr[idx], arr[pivotidx]
    arr[pivotidx + 1], arr[endidx] = arr[endidx], arr[pivotidx + 1]
    return pivotidx + 1


def _median_of_three(arr, idx_a, idx_b, idx_c):
    three = [(idx_a, arr[idx_a]), (idx_b, arr[idx_b]), (idx_c, arr[idx_c])]
    three.sort(key=lambda e: e[1])
    return three[2][0]


def _intro_util(arr, startidx, endidx, depthlimit):
    size = endidx - startidx

    if size < 16:
        _insertion_sort_introsort(arr, startidx, endidx)
        return

    if depthlimit == 0:
        _heap_sort_introsort(arr)
        return

    pivotidx = _median_of_three(arr, startidx, startidx + size // 2, endidx)
    arr[pivotidx], arr[endidx] = arr[endidx], arr[pivotidx]

    partitionidx = _partition_introsort(arr, startidx, endidx)
    _intro_util(arr, startidx, partitionidx - 1, depthlimit - 1)
    _intro_util(arr, partitionidx + 1, endidx, depthlimit - 1)


def introspective_sort(arr):
    """Introspective Sort"""
    import math
    length = len(arr)
    depthlimit = 2 * math.log2(length - 1)
    _intro_util(arr, 0, length - 1, depthlimit)


# endregion

# region Patience Sort

def patience_sort(arr):
    """Patience Sort"""
    import heapq

    piles = []
    for val in arr:
        for pile in piles:
            if val > pile[-1]:
                pile.append(val)
                break
        else:
            piles.append([val])
    arr[:] = tuple(heapq.merge(*piles))[:]  # 정렬 머징


# endregion

# region Smooth Sort

def _leonardheap(arr, length, idx):
    curidx = idx
    lidx = 2 * idx + 1
    ridx = 2 * idx + 2

    if lidx < length and arr[lidx] > arr[curidx]:
        curidx = lidx
    if ridx < length and arr[ridx] > arr[curidx]:
        curidx = ridx

    if curidx != idx:
        arr[idx], arr[curidx] = arr[curidx], arr[idx]
        _leonardheap(arr, length, curidx)


def smooth_sort(arr):
    """Smooth Sort"""
    length = len(arr)
    for idx in range(length // 2 - 1, -1, -1):
        _leonardheap(arr, length, idx)

    for idx in range(length - 1, -1, -1):
        arr[0], arr[idx] = arr[idx], arr[0]
        _leonardheap(arr, idx, 0)


# endregion

# region Tournament Sort

def tournament_sort(arr):
    """Tournament Sort"""

    length = len(arr)

    for idx in range(length // 2, -1, -1):
        _swap_binary_tree_ts(arr, length, idx)

    for idx in range(length - 1, -1, -1):
        if arr[0] > arr[idx]:
            arr[0], arr[idx] = arr[idx], arr[0]
            _swap_binary_tree_ts(arr, idx, 0)


def _swap_binary_tree_ts(arr, length, rootidx):
    minidx = rootidx
    lchildidx = 2 * rootidx
    rchildidx = 2 * rootidx + 1

    if lchildidx < length and arr[lchildidx] > arr[minidx]:
        minidx = lchildidx
    if rchildidx < length and arr[rchildidx] > arr[minidx]:
        minidx = rchildidx

    if minidx != rootidx:
        arr[rootidx], arr[minidx] = arr[minidx], arr[rootidx]
        _swap_binary_tree_ts(arr, length, minidx)


# endregion

# region Spread Sort

def spread_sort(arr):
    """Spread Sort"""

    output = []
    length = len(arr)
    max_val = max(arr)
    buckets = [[] for _ in range(length)]
    for idx in range(length):
        bucketidx = int(arr[idx] * length / (max_val + 1))
        buckets[bucketidx].append(arr[idx])
    for idx in range(length):
        _quick_sort_ss(buckets[idx], 0, len(buckets[idx]) - 1)
        output.extend(buckets[idx])
    arr[:] = output[:]


def _quick_sort_ss(arr, startidx, endidx):
    if startidx < endidx:
        partitionidx = _partition_array_ss(arr, startidx, endidx)
        _quick_sort_ss(arr, startidx, partitionidx - 1)
        _quick_sort_ss(arr, partitionidx + 1, endidx)


def _partition_array_ss(arr, startidx, endidx):
    pivot = arr[endidx]
    pivotidx = startidx - 1
    for idx in range(startidx, endidx):
        if arr[idx] <= pivot:
            pivotidx += 1
            arr[idx], arr[pivotidx] = arr[pivotidx], arr[idx]
    arr[pivotidx + 1], arr[endidx] = arr[endidx], arr[pivotidx + 1]
    return pivotidx + 1


# endregion


if __name__ == "__main__":
    pass
