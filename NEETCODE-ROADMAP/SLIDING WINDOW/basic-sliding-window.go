// You can edit this code!
// Click here and start typing.
package main

func main() {
	data := []int{1, 2, 3, 4, 5, 6, 7, 7}

	totalSum := 0
	for idx := 0; idx < 3; idx++ {
		totalSum += data[idx]
	}

	idx := 3
	fIdx := 0

	for idx < len(data) {
		totalSum = (totalSum + data[idx]) - data[fIdx]
		fIdx += 1
		idx += 1
	}

}
