# 2.The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem

group_size = int(input())
room_list = list(map(int,input().split()))
room_set = (sum(set(room_list))*group_size - sum(room_list))//(group_size -1)
print(room_set)
