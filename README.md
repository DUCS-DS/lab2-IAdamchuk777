[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17817173)
# Sp25Lab2
Lab 2 for Spring 25 Data Structures

### Runtime complexity

Referring to the algorithm you implemented in the function **monotonic** in the
file **edit_me.py** and assuming that the input list has length **N**,

* the big-O worst-case complexity is O(N), and
* the big-O best-case complexity is O(1) if the list is 1(one).

Referring to the code block below,
* the big-O worst-case complexity of the function **search** is log N.
  ```python
  def search(lst, key):

      assert monotonic(lst), "The list is not sorted"

      low = 0
      mid = len(lst) // 2
      high = len(lst) - 1

      while (high >= low):
          mid = (high + low) // 2
          if (lst[mid] < key):
              low = mid + 1
          elif (lst[mid] > key):
              high = mid - 1
          else:
              return mid

      return -1
  ```

Notes:
* Recall that, in Python, an **assert** statement has this form:
  ```python
  assert Boolean_expression, string
  ```
* Upon execution of an **assert** statement, **Boolean_expression** is evaluated; if it
  evaluates to **False**, execution is halted and error-message **string** is displayed.
  If **Boolean_expression** evaluates to **True**, then execution of the program continues.

#### Critique

I would not use the function **search** in real life because it inefficiently depend on an assert statement to verify that the list is sorted, adding an O(N) overhead that undermines the advantages of binary search. Also, the function only works with lists sorted in ascending order—if the list is in a different order, the search will move in the wrong direction, making it ineffective.
#Ivan Adamchuk