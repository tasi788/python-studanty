def  heapSort(nums):  #將陣列 nums[0] ~ nums[n-1] 共n個元素作排序
  buildHeap(nums) 		#先將陣列nums[] 整理成heap
  n = len(nums)
  while n > 0:
    nums[n-1],nums[0] = nums[0],nums[n-1]	# Swap nums[0],nums[n-1]
    n -= 1
    siftDown(nums, n, 0)  #將nums[0]往下調整以符合heap性質
def buildHeap(nums):
  n = len(nums)
  for k in range(n//2-1, -1, -1):
 		siftDown(nums, n, k)
def siftDown(nums, n, k):
  up = nums[k]
  while k < n//2:       #nums[k]不是樹葉
    bs = 2*k + 1        # nums[bs]為nums[k]之左兒子
    if bs+1<n and nums[bs+1]>nums[bs]:
      bs += 1  #若右兒子存在且較大
    if up >= nums[bs]:
      break    #大於大兒子
    nums[k] = nums[bs]        #大兒子上來
    k = bs
  nums[k] = up

nums = list(map(int, input().split()))
heapSort(nums)
print(nums)