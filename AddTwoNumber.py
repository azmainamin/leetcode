class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        """
                p1
        l1 =   [2, 4,3]
                p2
        l2 =   [5,6,4]
        
        Output: [7,0,8]
        """
        
        # 2 pointers each pointing to the start of the linked list 
        # initialize carry to false/0
        # if both pointers are not null, sum them up (check to see there is a carry or not) and see if there is a carry for the next number
        # move both pointers
        # if 1 of the pointer is null, we have reached the end of number. Add carry (if it exists) and then the rest of the number (are there more carries)
        
        pointer_1 = l1
        pointer_2 = l2
        
        carry = False
        
        resultHead = ListNode()
        # initialize resultList
        resultTail = resultHead
        
        while pointer_1 is not None or pointer_2 is not None:
            sum = 0
            if pointer_1 is None:
                sum += pointer_2.val
                pointer_2 = pointer_2.next
            
            elif pointer_2 is None:
                sum += pointer_1.val
                pointer_1 = pointer_1.next
            
            else:
                sum += pointer_1.val + pointer_2.val
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next
            
            # if we have carry from previous digit, add to sum
            
            if carry:
                sum += 1
            
            # check if we need to carry to next digit
            if sum >= 10:
                carry = True
                result = sum % 10
            else:
                carry = False
                result = sum
                
                
            currNode = ListNode(result)
            resultTail.next = currNode
            resultTail = resultTail.next
            
        
        # check for last carry
        if carry:
            carryNode = ListNode(1)
            resultList.next = carryNode
            
        return resultHead.next