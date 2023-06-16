#While to repeat numbers

num = 1
# while num <= 10:
#     print(num)
#     num += 1

#While to repeat numbers with break

# while num <= 10:
#     print(num)
#     if num == 5:
#         break
#     num += 1

#While to repeat numbers with continue

# while num <= 10:
#     print(num)
#     if num == 5:
#         continue
#     num += 1

#While adding numbers

num = int(input("Enter a number: "))
res = 0
cnt = 1
while cnt <= num:
    res += cnt
    cnt += 1
    print("Result: ", res)