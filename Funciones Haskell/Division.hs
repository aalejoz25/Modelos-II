division :: Integer -> Integer -> Integer
division m n
 |n>m=0
 |n>=n = 1 + (division (m-n) n)