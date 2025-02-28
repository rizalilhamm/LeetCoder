package main

func maxAscendingSum(nums []int) int {
    curr := nums[0]
    res := curr

    for idx := 1; idx < len(nums); idx++ {
        if nums[idx-1] < nums[idx] {
            curr += nums[idx]
        } else {
            curr = nums[idx]
        }
        
        if res < curr {
            res = curr
        }
    }
    return res

}