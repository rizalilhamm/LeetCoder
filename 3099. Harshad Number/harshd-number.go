package main

func sumOfTheDigitsOfHarshadNumber(x int) int {
    total := 0
    temp := x

    for temp != 0 {
        total += temp % 10
        temp /= 10
    }

    if x % total == 0 {
        return total
    }
    return -1
}