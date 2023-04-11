from typing import List, Optional
import mergesort

# Problem 1: Given an array of integers, find the
#            nth smallest element in the array.


def P1(arr, n):
    return mergesort.mergeSort(arr)[n-1]

# Problem 2: Given an array of integers, return the
#            array sorted in non-decreasing order.


def P2(arr):
    return mergesort.mergeSort(arr)

# Problem 3: Given two sorted arrays, merge them
#            into a single sorted array.


def P3(arr1, arr2):
    return mergesort.mergeArray(arr1, arr2, [])

# Problem 4: Merge k Sorted Lists (LeetCode Hard)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeLL(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val <= l2.val:
        l1.next = mergeLL(l1.next, l2)
        return l1
    else:
        l2.next = mergeLL(l1, l2.next)
        return l2


def sortLL(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid, slow.next = slow.next, None
    left, right = sortLL(head), sortLL(mid)
    return mergeLL(left, right)


def P4(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    while len(lists) > 1:
        new_lists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged_list = mergeLL(l1, l2)
            new_lists.append(merged_list)
        lists = new_lists
    return lists[0]
