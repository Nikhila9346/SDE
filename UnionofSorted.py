def UnionSorted(nums1, nums2):
    i = 0
    j = 0
    l = []
    while (i < len(nums1) and j < len(nums2)):
        if nums1[i] <= nums2[j]:
            if nums1[i] not in l or nums1[j]!=l[-1]:
                l.append(nums1[i])
            i += 1
        elif nums2[j] <= nums1[i]:
            if nums2[j] not in l or nums2[j] != l[-1]:
                l.append(nums2[j])
            j += 1 
    while j < len(nums2):
        if nums2[j] not in l:
            l.append(nums2[j])
            j += 1
    while i < len(nums1):
        if nums1[i] not in l:
            l.append(nums1[i])
            i += 1
    return l

nums1 =[1, 2, 3, 4, 5]
nums2 = [1, 2, 3, 6, 7]
nums2 = []
print(UnionSorted(nums1, nums2))

'''
[1, 2, 3,4, 5, 6, 7]
'''