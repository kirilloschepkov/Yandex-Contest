# [I. Робот](https://contest.yandex.ru/contest/27794/problems/I/ "Ссылка на сайт с задачей")
| Ограничение времени | Ограничение памяти |
| -|-|
| 4 секунда | 64Mb |

Студенты одного из вузов спроектировали робота для частичной автоматизации процесса сборки авиационного двигателя.

В процессе сборки двигателя могут встречаться операции 26 типов, которые обозначаются строчными буквами латинского алфавита. Процесс сборки состоит из N операций.

Предполагается использовать робота один раз для выполнения части подряд идущих операций из процесса сборки.

Память робота состоит из K ячеек, каждая из которых содержит одну операцию. Операции выполняются последовательно, начиная с первой, в том порядке, в котором они расположены в памяти. Выполнив последнюю из них, робот продолжает работу с первой. Робота можно остановить после любой операции. Использование робота экономически целесообразно, если он выполнит хотя бы K + 1 операцию.

Требуется написать программу, которая по заданному процессу сборки определит количество экономически целесообразных способов использования робота.

## Формат ввода

В первой строке входного файла записано число K > 0 — количество операций, которые можно записать в память робота.

Вторая строка состоит из N > K строчных латинских букв, обозначающих операции — процесс сборки двигателя. Операции одного и того же типа обозначаются одной и той же буквой. N ≤ 200000

## Формат вывода

Выходной файл должен содержать единственное целое число — количество экономически целесообразных способов использования робота.

## Примеры

| Ввод | Вывод |
| -|-|
| 2</br>zabacabab | 5 |
| 2</br>abc | 0 |