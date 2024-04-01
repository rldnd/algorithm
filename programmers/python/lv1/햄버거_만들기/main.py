def solution(ingredient):
    count = 0
    hamburger = list()
    
    for value in ingredient:
        hamburger.append(value)
        if len(hamburger) >= 4 and hamburger[len(hamburger)-4:len(hamburger)] == [1,2,3,1]:
            count += 1
            hamburger.pop()
            hamburger.pop()
            hamburger.pop()
            hamburger.pop()
            
    return count