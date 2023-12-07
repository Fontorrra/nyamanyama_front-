# s=0
# d=open("f.txt")#.read()
# # print(d)
# for i in d:
#     # print(i)
#     s+=int(i)
# print(s)


# c=input().split()
# a=[]
# s=0
# k=-1
# i=0
# u=0
# while i <len(c):
#     print(c)
#     if c[i]=="+":
#         # if s==0:
#             s=int(c[i-1])+int(c[i-2])
#             c[i]=str(s)
#             c.pop(i-1)
#             c.pop(i-2)
#             i-=2
#         # else:
#         #     s+=int(c[i-1])
#         #     c[i]=str(s)
#         #     i-=1
#     elif c[i]=="*":
#         # if s==0:
#             s=int(c[i-1])*int(c[i-2])
#             c[i]=str(s)
#             c.pop(i-1)
#             c.pop(i-2)
#             i-=2
#         # else:
#         #     s*=int(c[i-1])
#         #     c[i]=str(s)
#         #     i-=1
#     elif c[i]=="-":
#         # if s==0:
#             s=int(c[i-2])-int(c[i-1])
#             c[i]=str(s)
#             c.pop(i-1)
#             c.pop(i-2)
#             i-=2
#         # else:
#         #     s-=int(c[i-1])
#         #     c[i]=str(s)
#         #     i-=1
#     else:
#         i+=1
# print(s)




# u=input()
# o=[]
# y=[]
# while len(u)>0:
    
#     y+=[u]
#     u=input()
# for u in y:
#     #o+=[u]
#     if u=="+":
#         print(o[0])
#         o.pop(0)
#     elif len(o)>4:
#         pass
#     else:
#         o+=[u]
## print(o)

# u=input().split()
# s=0
# i=0
# c=0
# while u[i]=="1" and i<len(u)-1:
#     s+=1
#     u+=["0"]
#     i+=1
#     print(u)
# for i in u:
#     if i=="1":
#         c+=1
#     else:
#         c-=1
# if c<0:
#         c=0
# s+=c
# print(s)

# a1=input().split()
# b1=input().split()
# a=[]
# b=[]
# l=-1
# f=0
# for i in a1:
#     a+=[int(i)]
# for i in b1:
#     l+=1
#     b+=[int(i)]
# i=0
# while i<(len(b)-1):
#     if b[i]==1 and b[i+1]==0:
#         if a[i]>a[i+1] :
#             b.pop(i+1)
#             a.pop(i+1)
#             i-=1
#         elif a[i]<a[i+1]:
#             b.pop(i)
#             a.pop(i)
#             i-=1
#     else:        
#         i+=1
# print(len(b))

# class ListNode:
#      def __init__(self, x):
#          self.val = x
#          self.next = None
# class Solution:
#     o=""  
#     def getDecimalValue(self, head: ListNode) -> int: 
#         o=""
#         while(ListNode!=None):
#             #o=""
#        	    #o+=str(ListNode(self))
#             print(self,ListNode(self))



# n=[1,1,1,1,1]
# n=[2,3,1,1,4]
# n=n=[9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5]
# def jump(self, n: List[int]) -> int:
#         f=0
#         o=[]
#         l=len(n)
#         c=m=0
#         i=k=0
#         while i<len(n)-1:

#             a=n[i]
#             if i+n[i]>=l-1:
#                 k+=1
#                 return k
#                 break
#             ma=i+a
#             for u in range(1,a+1):
#                 p=i+u
#                 if n[p]+p>=m :#and p+n[p]>ma:
#                     m=n[p]+p
#                     c=u
#             # print(c)
            
#             m=0
#             i+=c
#             k+=1
#             # print(i,n[i],k)
#             if i+n[i]>=l-1:
#                 k+=1
#                 return k
#                 break
#         return k
# N = 5
# f = lambda x: all(x % i != 0 for i in range(int(x**0.5)+1) [2:])
# a = filter(f, range(4000)[2:]) [:N]
# print(f)


# o=[2]*4+[3]*3+[0]*5
# for i in range(1,6):
#     for u in range((4*i)%10,(4*i)%10+2):
#         o[u]+=(i%2)*2
# for i in range(1,13):
#     for u in range((3*i)%15,(3*i)%15+2):
#         o[u]+=i+1
#     for u in range(i,i+2):
#         o[u]=sum(o[i:i+2])+sum(o[i+1:i+3])
print(sum(o))
# print(sum(o[4:6]))
# print(sum(o[4:8]))
# print(sum(o[6:9]))