### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
    # Using only 1 '=' sets a variable equal to a value, 2 must be used for comparison
      return True
    else
    # A ':' is required here as with the initial if statement
      return False
   

  dif highest_card(self, card1 card2):
  # 'dif' needs to be 'def'
  # A ',' is missing between 'card1' and 'card2'
  # All code below here should be indented from the first line
  if card1.value > card2.value:
    return card
    # 'card' wasn't passed in and doesn't reference anything, should be 'card1'
  else:
    return card2
  


def cards_total(self, cards):
  total
  # 'total' currently does nothing and should be assigned a value, such as '=0'
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # This return statement should be outside of the for loop, currently it will end after the first loop
    # The return statement will be an error as it is currently trying to add a string and an integer
  
```
