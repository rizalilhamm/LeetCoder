package main

func isPowerOfThree2(n int) bool {
    if n <= 0 {
        return false
    }
    for n > 1 {
        if n % 3 != 0 {
            return false
        }
        n /= 3
    }

    return n == 1
}

/*
Example 45
45 / 3 = 15
15 / 3 = 5

result := False, karena 5 tidak bisa dihasilkan dari melakukan pangkat ke angka 3
*/ 