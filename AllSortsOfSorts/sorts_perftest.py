"""정렬 알고리즘 성능 측정"""

import timeit
import os
import random

import sorts


def main():
    """정렬 알고리즘의 실행시간을 측정하고 결과를 출력합니다."""

    # region 테스트 기본값

    # 테스트 요소의 최소값
    min_value = 1  # 양의 정수여야 함
    # 테스트 요소의 최대값
    max_value = 1024
    # 테스트 리스트의 길이
    array_length = max_value - min_value + 1  # (2**k 값이 되어야 함)

    # endregion 테스트 기본값

    # region 테스트 케이스 설정

    # 테스트 케이스
    testcases = []

    description = "랜덤 리스트 (요소 중복)"
    case_rnd_ovlp = [random.randint(min_value, max_value) for _ in range(array_length)]
    testcases.append((case_rnd_ovlp, description))

    description = "랜덤 리스트"
    case_rnd = list(range(min_value, max_value + 1))
    random.shuffle(case_rnd)
    testcases.append((case_rnd, description))

    description = "순차 증가 리스트 (정렬됨)"
    case_inc = list(range(min_value, max_value + 1))
    testcases.append((case_inc, description))

    description = "순차 감소 리스트 (역정렬됨)"
    case_dec = list(range(max_value, min_value - 1, -1))
    testcases.append((case_dec, description))

    description = "2단계 순차 증가 리스트"  # 예. [1, 3, 5, 7, 2, 4, 6, 8]
    case_2inc = [e for e in range(min_value, max_value + 1) if e % 2 == 0] + \
                [o for o in range(min_value, max_value + 1) if o % 2 == 1]
    testcases.append((case_2inc, description))

    description = "2단계 순차 감소 리스트"  # 예. [7, 5, 3, 1, 8, 6, 4, 2]
    case_2dec = [e for e in range(max_value, min_value - 1, -1) if e % 2 == 0] + \
                [o for o in range(max_value, min_value - 1, -1) if o % 2 == 1]
    testcases.append((case_2dec, description))

    description = "대체로 정렬된 리스트"  # 정렬 리스트 내 10% 개의 요소를 임의 배치
    case_near_sort = list(range(min_value, max_value + 1))
    shuffle_times = round(array_length * 0.05)  # 5% 선택: 짝 -> 10%
    for _ in range(shuffle_times):
        idx1 = random.randint(0, array_length - 1)
        idx2 = idx1
        while idx2 == idx1:
            idx2 = random.randint(0, array_length - 1)
        case_near_sort[idx1], case_near_sort[idx2] = \
            case_near_sort[idx2], case_near_sort[idx1]
    testcases.append((case_near_sort, description))

    description = "특정 값이 돌출된 랜덤 리스트"
    case_weired = list(range(min_value, max_value + 1))
    random.shuffle(case_weired)
    idx = random.randint(0, array_length - 1)
    case_weired[idx] = max_value ** 2
    testcases.append((case_weired, description))

    # endregion

    # region 테스트 메소드 설정

    testmethods = [
        (sorts.selection_sort, "Selection Sort"),
        (sorts.bubble_sort, "Bubble Sort"),
        (sorts.quick_sort, "Quick Sort"),
        (sorts.insertion_sort, "Insertion Sort"),
        (sorts.merge_sort, "Merge Sort"),
        (sorts.heap_sort, "Heap Sort"),
        (sorts.counting_sort, "Counting Sort"),
        (sorts.radix_sort, "Radix Sort"),
        (sorts.bucket_sort, "Bucket Sort"),
        (sorts.shell_sort, "Shell Sort"),
        (sorts.tim_sort, "Tim Sort"),
        (sorts.comb_sort, "Comb Sort"),
        (sorts.pigeonhole_sort, "Pigeonhole Sort"),
        (sorts.cycle_sort, "Cycle Sort"),
        (sorts.cocktail_sort, "Cocktail Sort"),
        (sorts.strand_sort, "Strand Sort"),
        (sorts.bitonic_sort, "Bitonic Sort"),
        (sorts.pancake_sort, "Pancake Sort"),
        (sorts.binary_insertion_sort, "Binary Insertion Sort"),
        # (sorts.bogo_sort, "Bogo Sort"),  # 비효율적 정렬 알고리즘
        # (sorts.bozo_sort, "Bozo Sort"),  # 비효율적 정렬 알고리즘
        (sorts.gnome_sort, "Gnome Sort"),
        # (sorts.sleep_sort, "Sleep Sort"),  # 정렬의 정확도가 보장되지 않음
        (sorts.brick_sort, "Brick Sort"),
        # (sorts.stooge_sort, "Stooge Sort"),  # 비효율적 정렬 알고리즘
        (sorts.bead_sort, "Bead Sort"),  # 요소의 편차가 클 경우 매우 느림
        (sorts.binary_tree_sort, "Binary Tree Sort"),
        (sorts.introspective_sort, "Introspective Sort"),
        (sorts.patience_sort, "Patience Sort"),
        (sorts.smooth_sort, "Smooth Sort"),
        (sorts.tournament_sort, "Tournament Sort"),
        (sorts.spread_sort, "Spread Sort")
    ]

    # endregion

    # region 성능 측정

    # --- 성능 측정 ---

    # 실행 시간 성능이 저장되는 리스트
    # 각 요소는 [함수설명, case 1 수행시간, case 2 수행시간, ...]의 리스트임
    performance_table = []

    num_total_works = len(testmethods) * len(testcases)  # 전체 작업 수
    curwork_count = 0  # 현재 진행 작업
    for (fn, fn_desc) in testmethods:
        method_result = [fn_desc]
        for (tc_idx, (tc, _)) in enumerate(testcases):
            # 진행 상태 출력
            curwork_count += 1
            prgbar = progress_bar(curwork_count, num_total_works)
            print(f"성능 측정 중입니다: {prgbar}", end="\r")

            # 실행 시간 측정
            unsortedcase = tc[:]
            sortedcase = sorted(unsortedcase)
            st_time = timeit.default_timer()
            fn(unsortedcase)
            en_time = timeit.default_timer()
            delta_ms = int((en_time - st_time) * 1000)  # ms
            if unsortedcase != sortedcase:
                raise AssertionError(f"{fn.__name__} - Sort failed.")

            method_result.append(delta_ms)
        performance_table.append(method_result)
    print("\n")

    # endregion

    # region 출력

    # --- 출력을 위해 performance_table 재구성 ---
    # 각 요소는 [함수설명, case 1 수행시간, case 2 수행시간, ..., 평균, 표준편차]의 리스트
    repr_table = []  # result_table의 문자열 구성

    # 헤드라인 구성
    headline = ["Cases"]
    for i in range(len(testcases)):
        headline.append(f"Case {i + 1:>2}")
    headline.append("Average")  # 전체 케이스에 대한 평균 컬럼
    headline.append("Std.Dev.")  # 전체 케이스에 대한 표준편차 컬럼
    repr_table.append(headline)
    # 테이블 바디
    for (col_1st, *vals) in performance_table:  # 메소드명, *실행시간
        eachline = [col_1st]
        for idx, val in enumerate(vals):
            valstr = f"{val:,}" if val >= 1 else "<1"
            eachline.append(f"{valstr} ms")
        # 전체 케이스에 대한 평균 실행 시간 추가
        avgtime = round(sum(vals) / len(vals), 1)
        avgstr = f"{avgtime:,}" if avgtime >= 1 else "<1"
        eachline.append(f"{avgstr} ms")
        # 전체 케이스에 대한 표준편차
        stddev = round((sum((v - avgtime) ** 2 for v in vals) / len(vals)) ** 0.5, 1)
        stddevstr = f"{stddev:,}" if stddev >= 1 else "<1"
        eachline.append(f"{stddevstr} ms")

        repr_table.append(eachline)

    max_methoname_span = 0  # 메소드명의 최대 길이
    max_value_span = 0  # 실행 시간 표현의 최대 길이
    for (col_1st, *col_others) in repr_table:
        if len(col_1st) > max_methoname_span:
            max_methoname_span = len(col_1st)
        max_cur_line_value_span = max(len(col) for col in col_others)
        if max_cur_line_value_span > max_value_span:
            max_value_span = max_cur_line_value_span

    # --- 출력 ---
    sio = list()  # 출력 결과 저장
    # 테스트 케이스 설명 테이블
    sio.append("[테스트 케이스]")
    prefix = "   - "
    for (idx, (_, desc)) in enumerate(testcases):
        sio.append(f"{prefix}Case {idx + 1:>2}: {desc}")
    sio.append("")

    # 실행 시간 테이블
    sio.append("[실행 시간]")
    for (col_1st, *col_others) in repr_table:
        tmpstr = f"{prefix}{col_1st:>{max_methoname_span}}: "
        for val in col_others:
            tmpstr += f"{val:>{max_value_span}}  "
        sio.append(tmpstr)

    # 화면 출력
    for line in sio:
        print(line)

    # 현재 디렉토리에 로그
    filepath = os.path.splitext(__file__)[0] + ".txt"
    with open(filepath, "w", encoding="UTF8") as f:
        for line in sio:
            f.write(f"{line}\n")

    # endregion 출력


def progress_bar(current_work, total_work):
    """진행 상태를 나타내는 문자열을 반환합니다.
    
    Args:
        current_work: 현재의 작업 단게를 나타내는 정수
        total_work: 총 작업의 개수
    """

    length = 50  # 프로그레스 바의 길이
    done = round(current_work / total_work * length)
    progress_str = [
        "[",
        done * "█",
        (length - done) * "-",
        "]",
        f" {round(current_work / total_work * 100)}%",
    ]
    return "".join(progress_str)


if __name__ == "__main__":
    main()
