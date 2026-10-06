class Solution(object):
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        bucket_list = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket_list[count].append(num)
        result = []
        for bucket in reversed(bucket_list):
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result

        