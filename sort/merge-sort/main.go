package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)

var steps int = 0

func readNums(infile *os.File) ([]int, error) {
	nums := make([]int, 0, 1000)
	i := 0

	scanner := bufio.NewScanner(infile)
	defer infile.Close()

	for scanner.Scan() {
		k, err := strconv.Atoi(scanner.Text())
		if err != nil {
			return nil, err
		}
		nums = append(nums, k)
		i += 1
	}
	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return nums, nil
}

func mergeSort(nums *[]int) *[]int {
	if len(*nums) <= 1 {
		return nums
	}

	l := len(*nums) / 2
	list1 := (*nums)[:l]
	list2 := (*nums)[l:]

	return merge(mergeSort(&list1), mergeSort(&list2))
}

func merge(list1 *[]int, list2 *[]int) *[]int {
	len1, len2 := len(*list1), len(*list2)
	result := make([]int, len1 + len2)
	n1, n2 := (*list1)[0], (*list2)[0]
	i, l1i, l2i := 0, 0, 0

	for {
		steps += 1
		if n1 < n2 {
			result[i] = n1
			i += 1
			l1i += 1
			if l1i == len1 {
				break
			}
			n1 = (*list1)[l1i]
		} else {
			result[i] = n2
			i += 1
			l2i += 1
			if l2i == len2 {
				break
			}
			n2 = (*list2)[l2i]
		}
	}

	for l1i < len1 {
		steps += 1
		result[i] = (*list1)[l1i]
		i += 1
		l1i += 1
	}
	for l2i < len2 {
		steps += 1
		result[i] = (*list2)[l2i]
		i += 1
		l2i += 1
	}
	return &result
}

func main() {
	nums, err := readNums(os.Stdin)
	if err != nil {
		log.Fatalf("Failed to read nums: %v", err)
	}

	sorted := mergeSort(&nums)
	for i := range *sorted {
		fmt.Println((*sorted)[i])
	}
	l := len(nums)
	fmt.Fprintln(os.Stderr, "Length: ", l)
	fmt.Fprintln(os.Stderr, "n log(n): ", float64(l) * math.Log2(float64(l)))
	fmt.Fprintln(os.Stderr, "Steps: ", steps)
}
