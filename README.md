This repository contains Python code that I have learnt on Data Structures & Algorithms.

Resource: https://jovian.com/learn/data-structures-and-algorithms-in-python?action=locked

## Question - Brute Force/Binary Search/Generic Binary Search
> Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

<img src="https://i.imgur.com/mazym6s.png" width="480">

## Question - Generic Binary Search (Ascending Order) (Start & End Index of a given number)
> Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.

#### Example 1:
#### Input: nums = [5,7,7,8,8,10], target = 8
#### Output: [3,4]

<br>

#### Example 2:
#### Input: nums = [5,7,7,8,8,10], target = 6
#### Output: [-1,-1]

<br>

#### Example 3:
#### Input: nums = [], target = 0
#### Output: [-1,-1]

<br>

## Question - Assignment 1a (Number of times an increasing order sorted array is rotated to the right)
> You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
<br><br> Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
<br><br> Your function should have the worst-case complexity of O(log N), where N is the length of the list.
<br><br> __You can assume that all the numbers in the list are unique.__
<br><br> We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].
<br><br> "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

#### Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

<br>

## Question - Assignment 1b (Number of times an increasing order sorted array is rotated to the right)
> You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
<br><br> Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
<br><br> __The numbers in the list can be repeated.__
<br><br> We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].
<br><br> "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

#### Example: The list [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4] was obtained by rotating the sorted list [0, 0, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 9, 9, 9] 6 times. (Notice the list has repeated numbers.)

<br>

## Question - Assignment 1c (Searching in a Rotated List)
> You are given list of numbers, obtained by rotating a sorted list an unknown number of times. You are also given a target number. Write a function to find the position of the target number within the rotated list. __You can assume that all the numbers in the list are unique.__

#### Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], the target number 2 occurs at position 5.

<br>
