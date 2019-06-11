from doubly_linked_list import DoublyLinkedList

class TextBuffer:
  def __init__(self, init=None):
    self.contents = DoublyLinkedList()
    if init:
      for char in init:
        self.contents.add_to_tail(char)

  def __str__(self):
    s = ""
    current = self.contents.head
    while current:
      s += current.value
      current = current.next
    return s

  def append(self, str_to_add):
    for char in str_to_add:
      self.contents.add_to_tail(char)

  def prepend(self, str_to_add):
    for char in str_to_add[::-1]:
      self.contents.add_to_head(char)

  def delete_front(self, chars_to_remove):
    for _ in range(chars_to_remove):
      self.contents.remove_from_head()

  def delete_back(self, chars_to_remove):
    for _ in range(chars_to_remove):
      self.contents.remove_from_tail()

  def join(self, other_buffer):
    # connect tail of this buffer to head of other buffer
    self.contents.tail.next = other_buffer.contents.head
    # set other buffers heads previous to be self.tail
    other_buffer.contents.head.prev = self.contents.tail
    # update other buffer's head to be first buffer's head
    other_buffer.contents.head = self.contents.head
    # update this buffer's tail to be other's tail
    self.contents.tail = other_buffer.contents.tail

text = TextBuffer("Super")
print(text)

text.append("califragilisticexpealidocious")
print(text)

text.delete_back(8)
print(text)

text.prepend("hey")
print(text)

text.delete_front(5)
print(text)
