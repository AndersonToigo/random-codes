package main

type Number interface {
	int | float64
}

func Soma[T Number](m map[string]T) T {
	var soma T
	for _, v := range m {
		soma += v
	}
	return soma
}

func main() {
	m := map[string]int{"a": 1, "b": 2}
	m1 := map[string]float64{"a": 1.1, "b": 2.2}
	println(Soma(m))
	println(Soma(m1))
	println(1.1 + 2.2)
}

