"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length


  def add_to_head(self, value):
    self.length += 1
    new_head = ListNode(value)
    if self.head is None:
      self.head = new_head
      self.tail = new_head
    else:
      self.head.insert_before(value)
      self.head = self.head.prev

  def remove_from_head(self):
    if self.head is None:
      return None

    self.length -= 1
    head = self.head
    if self.head.next is None:
      self.head = None
      self.tail = None
    else:
      self.head.delete()
      self.head = self.head.next
    return head.value

  def add_to_tail(self, value):
    self.length += 1
    new_tail = ListNode(value)
    if self.tail is None:
      self.head = new_tail
      self.tail = new_tail
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next

  def remove_from_tail(self):
    if self.tail is None:
      return Noone

    self.length -= 1
    tail = self.tail
    if self.tail.prev is None:
      self.head = None
      self.tail = None
    else:
      self.tail.delete()
      self.tail = self.tail.prev
    return tail.value


  def move_to_front(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
      return

    if node is self.tail:
      self.tail = node.prev
    self.head.insert_before(node.value)
    node.delete()
    self.head = self.head.prev
    return self

  def move_to_end(self, node):
    if self.tail is None:
      self.head = node
      self.tail = node
      return

    if node is self.head:
      self.head = node.next
    self.tail.insert_after(node.value)
    node.delete()
    self.tail = self.tail.next
    return self

  def delete(self, node):
    if self.length == 0:
      return None
    if node is self.head:
      self.remove_from_head()
    elif node is self.tail:
      self.remove_from_tail()
    else:
      node.delete()
      self.length -= 1

  def get_max(self):
    n = self.head
    if n is None:
      return None

    maximum = float('-inf')
    while n is not None:
      if n.value > maximum:
        maximum = n.value
      n = n.next
    return maximum
