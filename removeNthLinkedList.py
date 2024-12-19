pointer1 = head
pointer2 = head

for i in range(n):
    pointer1 = pointer1.next

if not pointer1:
    return head.next

while pointer1.next:
    pointer1 = pointer1.next
    pointer2 = pointer2.next

pointer2.next = pointer2.next.next
return head