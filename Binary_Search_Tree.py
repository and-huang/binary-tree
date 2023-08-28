class Binary_Search_Tree:


  class __BST_Node:


    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None


  def __init__(self):
    self.__root = None
    self.height = 0


  def __balance(self, t):
    if t is None:
      return None
    balanceValue = self.__recursive_height_check(t.right) - self.__recursive_height_check(t.left)
    if balanceValue > 1:
      if self.__recursive_height_check(t.right.right) - self.__recursive_height_check(t.right.left) < 0:
        t.right = self.__rotate_right(t.right)
      t = self.__rotate_left(t)
    elif balanceValue < -1:
      if self.__recursive_height_check(t.left.right) - self.__recursive_height_check(t.left.left) > 0:
        t.left = self.__rotate_left(t.left)
      t = self.__rotate_right(t)
    return t



  def __rotate_left(self, t):
    newParent = t.right
    t.right = newParent.left
    newParent.left = t
    return newParent
  


  def __rotate_right(self, t):
    newParent = t.left
    t.left = newParent.right
    newParent.right = t
    return newParent


  def insert_element(self, value):
    if self.__root == None:
      self.__root = Binary_Search_Tree.__BST_Node(value)
      self.height = 1
    else:
      self.__root = self.__recursive_Insertion(value, self.__root)
    self.height = self.__recursive_height_check(self.__root)


 
  def __recursive_Insertion(self, value, currentNode):
    if currentNode is None:
        return Binary_Search_Tree.__BST_Node(value)
    if currentNode.value < value:
        currentNode.right = self.__recursive_Insertion(value, currentNode.right)
    elif currentNode.value > value:
        currentNode.left = self.__recursive_Insertion(value, currentNode.left)
    else:
        raise ValueError
    return self.__balance(currentNode)


  def __recursive_Removal(self, value, currentNode):
    if currentNode == None:
        raise ValueError
    if value < currentNode.value:
        currentNode.left = self.__recursive_Removal(value, currentNode.left)
    elif value > currentNode.value:
        currentNode.right = self.__recursive_Removal(value, currentNode.right)
    else:
        if currentNode.left is None:
            return currentNode.right
        elif currentNode.right is None:
            return currentNode.left
        else:
            replacementVal = self.__find_min(currentNode.right)
            currentNode.value = replacementVal.value
            currentNode.right = self.__recursive_Removal(replacementVal.value, currentNode.right)
    return self.__balance(currentNode)


  def __recursive_height_check(self, currentNode):
    if currentNode is None:
      return 0
    else:
      return int(max(self.__recursive_height_check(currentNode.left), self.__recursive_height_check(currentNode.right)) + 1)



  def __find_min(self, node):
      while node.left is not None:
          node = node.left
      return node



  def remove_element(self, value):
    if self.__root == None:
      raise ValueError
    else:
      self.__root = self.__recursive_Removal(value, self.__root)
    self.height = self.__recursive_height_check(self.__root)


  def __recursive_in_order(self, currentNode):
    if currentNode is None:
      return ""
    else:
      left_sub = self.__recursive_in_order(currentNode.left)
      current_nodeString = str(currentNode.value)
      right_sub = self.__recursive_in_order(currentNode.right)
      if left_sub != "" and right_sub != "":
        return left_sub + ", " + current_nodeString + ", " + right_sub
      elif left_sub != "":
        return left_sub + ", " + current_nodeString
      elif right_sub != "":
        return current_nodeString + ", " + right_sub
      else:
        return current_nodeString



  def in_order(self):
    if self.__root == None:
      return "[ ]"
    return "[ " + self.__recursive_in_order(self.__root) + " ]"


  def __recursive_pre_order(self, currentNode):
    if currentNode is None:
      return ""
    else:
      left_sub = self.__recursive_pre_order(currentNode.left)
      current_nodeString = str(currentNode.value)
      right_sub = self.__recursive_pre_order(currentNode.right)
      if left_sub != "" and right_sub != "":
        return current_nodeString + ", " + left_sub + ", " + right_sub
      elif left_sub != "":
        return current_nodeString + ", " + left_sub
      elif right_sub != "":
        return current_nodeString + ", " + right_sub
      else:
        return current_nodeString


  def pre_order(self):
    if self.__root == None:
      return "[ ]"
    return "[ " + self.__recursive_pre_order(self.__root) + " ]"


  def __recursive_post_order(self, currentNode):
    if currentNode is None:
      return ""
    else:
      left_sub = self.__recursive_post_order(currentNode.left)
      current_nodeString = str(currentNode.value)
      right_sub = self.__recursive_post_order(currentNode.right)
      if left_sub != "" and right_sub != "":
        return left_sub + ", " + right_sub + ", " + current_nodeString
      elif left_sub != "":
        return left_sub + ", " + current_nodeString
      elif right_sub != "":
        return right_sub + ", " + current_nodeString
      else:
        return current_nodeString



  def post_order(self):
    if self.__root == None:
      return "[ ]"
    return "[ " + self.__recursive_post_order(self.__root) + " ]"


  def __recursive_to_list(self, currentNode, in_order_list):
    if currentNode is None:
      return
    self.__recursive_to_list(currentNode.left, in_order_list)
    in_order_list.append(currentNode.value)
    self.__recursive_to_list(currentNode.right, in_order_list)



  def to_list(self):
    in_order_list = []
    self.__recursive_to_list(self.__root, in_order_list)
    return in_order_list



  def get_height(self):
    return self.height


  def get_root(self):
    return self.__root


  def __str__(self):
    return self.in_order()


if __name__ == '__main__':
  pass