# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        dummy = head = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next

        for x in sorted(nodes):
            head.next = ListNode(x)
            head = head.next

        return dummy.next

class Solution2:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      heap = []
      for i, node in enumerate(lists):
          if node:
              heapq.heappush(heap, (node.val, i, node))

      dummy = ListNode()
      head = dummy

      while heap:
          val, i, node = heapq.heappop(heap)
          head.next = node
          head = node
          node = node.next
          if node:
              heapq.heappush(heap, (node.val, i, node))

      return dummy.next

class Solution3:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mlist = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mlist.append(self.merge(l1, l2))
            lists = mlist


        return lists[0]

    def merge(self, list1, list2):
        dummy = ListNode()
        head = dummy
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next

            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        if list1:
            head.next = list1

        if list2:
            head.next = list2

        return dummy.next
