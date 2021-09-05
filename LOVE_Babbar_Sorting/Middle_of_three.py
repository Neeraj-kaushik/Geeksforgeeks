def middle_of_three(A, B, C):
    if (A >= B and A <= C) or (A <= B and A >= C):
        return A
    elif (B >= A and B <= C) or (B <= A and B >= C):
        return B
    elif (C >= A and C <= B) or (C <= A and C >= B):
        return C


A = int(input())
B = int(input())
C = int(input())
print(middle_of_three(A, B, C))
