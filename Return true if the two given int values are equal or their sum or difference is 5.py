def test_number5(x, y):  
    if x == 5 or y == 5 or abs(x-y) == 5 or (x+y) == 5:  
        return True  
    else:  
        return False  
  
print(test_number5(7, 2))  
print(test_number5(3, 2))  
print(test_number5(2, 2))