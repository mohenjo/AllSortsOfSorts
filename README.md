# All Sorts of Sorts | 정렬 알고리즘 코드 구현

다양한 정렬 알고리즘에 대한 파이썬 코드 구현

> + 다양한 정렬 알고리즘 문서로부터 최적의 파이썬 코드 구현을 참조, 수정 및 업데이트
> + 정렬 알고리즘에 대한 유닛테스트
> + 정렬 알고리즘의 성능 비교(실행시간) 



## Description

### Module Usage

```{python}
import sorts
```

### Desciption on Filess

+ `sorts.py`
    + 정렬 알고리즘을 포함하고 있는 모듈입니다.
    + 모든 알고리즘은 in-place 방식으로 구현되었습니다.
    + 다른 정렬 알고리즘의 참조가 필요한 경우 `# region <algorithm_name>` ... `# endregion` 내에 필요한 코드를 모두 포함하였습니다.
    + 알고리즘 구현에 필요한 built-in 모듈은 해당 함수 내에서 `import`했습니다.
+ `test_sorts.py`
    + `sorts.py`에 대한 유닛테스트 파일입니다.
    + (일부 알고리즘의 제한에 의해) 정수 리스트에 대한 유닛테스트를 실행합니다.
+ `sorts_perftest.py`
    + 정렬 알고리즘의 성능 측정을 위한 파일입니다.
    + 다양한 테스트 케이스에 대해 성능을 측정합니다.
    + 측정 결과는  `.txt` 파일에도 저장됩니다.

### Sorting Algorithms

- Selection Sort
- Bubble Sort
- Quick Sort
- Insertion Sort
- Merge Sort
- Heap Sort
- Counting Sort
- Radix Sort
- Bucket Sort
- Shell Sort
- Tim Sort
- Comb Sort
- Pigeonhole Sort
- Cycle Sort
- Cocktail Sort (Bidirectional Bubble Sort)
- Strand Sort
- Bitonic Sort
- Pancake Sort
- Binary Insertion Sort
- Bogo Sort
- Bozo Sort
- Gnome Sort
- Sleep Sort
- Brick Sort (Odd-Even Sort)
- Stooge Sort
- Bead Sort (Gravity Sort)
- Binary Tree Sort
- Introspective Sort
- Patience Sort
- Smooth Sort
- Tournament Sort
- Spread Sort

### Test Cases for Performance

정수 리스트에 대해서:

1. 랜덤 리스트 (요소 중복 가능)
2. 랜덤 리스트
3. 순차 증가 리스트 (오름차순 정렬)
4. 순차 감소 리스트 (내림차순 정렬)
5. 2단계 순차 증가 리스트 (예: `[1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10, 12]`)
6. 2단계 순차 감소 리스트 (예: `[12, 10, 8, 6, 4, 2, 11, 9, 7, 5, 3, 1]`)
7. 대체로 정렬된 리스트 (요소의 10%가 랜덤 분포)
8. 특정 값이 돌출된 리스트 

*테스트 케이스에 따라 동일 알고리즘의 성능이 크게 차이날 수 있습니다.*

*비효율 정렬 방식은 코드 구현만 제공합니다.*



## Test Environments & Dependencies

### Test Environment

+ Python 3.7.5 (64-bit)
+ PyCharm Community Edition
+ Microsoft Windows 10 (x64)

### Dependencies / 3rd-party package(s)

+ None



## License

+ MIT License