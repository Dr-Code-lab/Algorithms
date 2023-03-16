class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeKSortedLists():
    from typing import List, Optional

    def __init__(self, content = [66,26,46]):
        self.content = content
        print('>>', '\n', 'CONTENT : ',content)

    # Definition for singly-linked list.


    def sort_merge(self, total_listnode, listnode):
        if total_listnode is None:
            return listnode
        elif listnode is None:
            return total_listnode
        if total_listnode.val <= listnode.val:
            result = total_listnode
            result.next = self.sort_merge(total_listnode.next, listnode)
        else:
            result = listnode
            result.next = self.sort_merge(total_listnode, listnode.next)
        return result

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        total_listnode = None
        lists_will_append = None 
        if lists:
            for index, item in enumerate(lists):
                if item and not total_listnode:
                    total_listnode = item
                    lists_will_append = lists[index + 1:len(lists):]
        if lists_will_append:
            for listnode in lists_will_append:
                total_listnode = self.sort_merge(total_listnode, listnode)
        return total_listnode
            


    
    def main(self):
        print('\033[92m',self.mergeKLists(self.content), '\033[0m\n........')

# TEST :
if __name__ == '__main__':

    text = (
            [[1,4,5],[1,3,4],[2,6]]     # Need to make linked lists
            )
             
    for item in text:
        MergeKSortedLists(item).main()
