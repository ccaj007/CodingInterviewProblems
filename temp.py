def climbStairs(n: int) -> int:
    if n == 0:
        return 0
    if n == 1: 
        return 1
    
    return climbStairs(n-1) + climbStairs(n-2)



n = 5
print(climbStairs(n))


b: int = 10
c: int = '44'

b: int = 'jkdsjafkl'

z: int = 'fjdklasd'
