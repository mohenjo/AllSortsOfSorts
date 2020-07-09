"""정렬 알고리즘 유닛테스트"""

import random
import unittest

import sorts


class TestBase(unittest.TestCase):
    def setUp(self):
        min_num = 1  # 테스트 요소의 최소값
        max_num = 1_024  # 테스트 요소의 최대값
        test_arr_len = max_num - min_num + 1  # 테스트 리스트의 길이 (2**k 값)
        self.testcase = [random.randint(min_num, max_num) for _ in range(test_arr_len)]
        self.sortedcase = sorted(self.testcase)

    def test_selection_sort(self):
        sorts.selection_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_bubble_sort(self):
        sorts.bubble_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_quick_sort(self):
        sorts.quick_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_insertion_sort(self):
        sorts.insertion_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_merge_sort(self):
        sorts.merge_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_heap_sort(self):
        sorts.heap_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_counting_sort(self):
        sorts.counting_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_radix_sort(self):
        sorts.radix_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_bucket_sort(self):
        sorts.bucket_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_shell_sort(self):
        sorts.shell_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_tim_sort(self):
        sorts.tim_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_comb_sort(self):
        sorts.comb_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_pigeonhole_sort(self):
        sorts.pigeonhole_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_cycle_sort(self):
        sorts.cycle_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_cocktail_sort(self):
        sorts.cocktail_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_strand_sort(self):
        sorts.strand_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_bitonic_sort(self):
        sorts.bitonic_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_pancake_sort(self):
        sorts.pancake_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_binary_insertion_sort(self):
        sorts.binary_insertion_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    # Bogo Sort는 정렬이 될 때까지 순열을 계속 섞어 비교하는 방식이므로,
    # 길이가 긴 시퀀스에 대해서는 매우 많은 시간이 소요됨
    # 따라서, 이 케이스에 대해서는 매우 짧은 길이의 테스트를 진행함
    def test_bogo_sort(self):
        self.testcase = [5, 3, 4, 1, 2, 7, 6]
        self.sortedcase = sorted(self.testcase)
        sorts.bogo_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    # Bozo Sort는 정렬이 될 때까지 순열 항목을 교환하여 비교하는 방식이므로,
    # 길이가 긴 시퀀스에 대해서는 매우 많은 시간이 소요됨
    # 따라서, 이 케이스에 대해서는 매우 짧은 길이의 테스트를 진행함
    def test_bozo_sort(self):
        self.testcase = [5, 3, 4, 1, 2, 7, 6]
        self.sortedcase = sorted(self.testcase)
        sorts.bozo_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_gnome_sort(self):
        sorts.gnome_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    # Sleep Sort는 정렬의 정확도를 보장하지 않음
    # 정렬 케이스의 크기가 커질수록, 알고리즘 내 process sleep 기간이 짧아질수록
    # 정확도는 낮아질 가능성이 높음
    # 이 케이스에 대해서는 매우 짧은 길이의 테스트를 진행함
    def test_sleep_sort(self):
        self.testcase = [5, 3, 4, 1, 2, 7, 6, 10, 8, 9]
        self.sortedcase = sorted(self.testcase)
        sorts.sleep_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_brick_sort(self):
        sorts.brick_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    # Stooge Sort는 비효율적 정렬 알고리즘임
    # 따라서, 이 케이스에 대해서는 매우 짧은 길이의 테스트를 진행함
    def test_stooge_sort(self):
        self.testcase = [5, 3, 4, 1, 2, 7, 6, 10, 8, 9]
        self.sortedcase = sorted(self.testcase)
        sorts.stooge_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_bead_sort(self):
        sorts.bead_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_binary_tree_sort(self):
        sorts.binary_tree_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_introspective_sort(self):
        sorts.introspective_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_patience_sort(self):
        sorts.patience_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_smooth_sort(self):
        sorts.smooth_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_tournament_sort(self):
        sorts.tournament_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)

    def test_spread_sort(self):
        sorts.spread_sort(self.testcase)
        self.assertEqual(self.testcase, self.sortedcase)



if __name__ == "__main__":
    unittest.main()
