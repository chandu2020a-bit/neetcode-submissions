class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tot = sorted(nums1 + nums2 )
        if len(tot)%2 == 0 :
            left = 0 
            right= len(tot)-1
            mid = (left+right)//2 
            return (tot[mid]+tot[mid+1])/2 
        else:
            left = 0 
            right= len(tot)-1
            mid = (left+right)//2
            return float(tot[mid])
        