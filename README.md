# To Run This Repository
Use python main.py
The main file contains all unit tests and multithreading. <br> <br>
Example Output: <br>
```
python main.py
['asqwr1234@1', 'aF145#', '2w3E*', '2We3345']
no match: asqwr1234@1
no match: 2w3E*
no match: 2We3345
['which is better python 2 or python 3']
{'2': 1, '3': 1, 'better': 1, 'is': 1, 'or': 1, 'python': 2, 'which': 1}
enqueue: 1
rear: 1
enqueue: 2
rear: 2
enqueue: 3
rear: 3
enqueue: 4
rear: 4
enqueue: 5
rear: 5
Start
1 -> 1
2 -> 2
3 -> 3
4 -> 4
5 -> 5
End
enqueue: 15
rear: 5
Start
1 -> 1
2 -> 2
3 -> 3
4 -> 4
5 -> 15
End
dequeue: 1
front 2
dequeue: 2
front 3
Start
1 -> None
2 -> None
3 -> 3
4 -> 4
5 -> 15
End
enqueue: 25
rear: 1
Start
1 -> 25
2 -> None
3 -> 3
4 -> 4
5 -> 15
End
enqueue: 35
rear: 2
Start
1 -> 25
2 -> 35
3 -> 3
4 -> 4
5 -> 15
End
enqueue: 45
rear: 2
Start
1 -> 25
2 -> 45
3 -> 3
4 -> 4
5 -> 15
End
dequeue: 3
front 4
Start
1 -> 25
2 -> 45
3 -> None
4 -> 4
5 -> 15
End
done
enqueue: 1
rear: 1
enqueue: 2
rear: 2
enqueue: 3
rear: 3
enqueue: 4
rear: 4
enqueue: 5
rear: 5
dequeue: 1
front 2
.enqueue: 1
rear: 1
enqueue: 2
rear: 2
enqueue: 3
rear: 3
enqueue: 4
rear: 4
dequeue: 1
front 2
.enqueue: 1
rear: 1
enqueue: 2
rear: 2
enqueue: 3
rear: 3
enqueue: 4
rear: 4
enqueue: 5
rear: 5
.enqueue: 1
rear: 1
enqueue: 2
rear: 2
enqueue: 3
rear: 3
enqueue: 4
rear: 4
enqueue: 5
rear: 5
enqueue: 15
rear: 5
.['asqwr1234@1', 'aF145#', '2w3E*', '2We3345']
no match: asqwr1234@1
no match: 2w3E*
no match: 2We3345
.['which is better python 2 or python 3']
{'2': 1, '3': 1, 'better': 1, 'is': 1, 'or': 1, 'python': 2, 'which': 1}
.
----------------------------------------------------------------------
Ran 6 tests in 0.006s

OK
```
