package main

import (
	"fmt"
	"math/rand"
	"time"
)

var Complexity = map[int]string{
    1: "Only letters (lowercase)",
    2: "Only letters (uppercase)",
    3: "Only letters (lowercase and uppercase)",
    4: "Only numbers",
    5: "Only letters and numbers",
    6: "Only letters, numbers and special characters",
}

// Função para gerar uma string aleatória de comprimento especificado
func generateRandomString(length int) string {
	uppercaseLetters := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lowercaseLetters := "abcdefghijklmnopqrstuvwxyz"
	numbers := "0123456789"
	specialCharacters := "!@#$%&*()_+-=[]|,./?><"

	characters := uppercaseLetters + lowercaseLetters + numbers + specialCharacters

	rand.Seed(time.Now().UnixNano())
	randomString := make([]byte, length)

	for i := 0; i < length; i++ {
		randomString[i] = characters[rand.Intn(len(characters))]
	}

	return string(randomString)
}

func main() {
	fmt.Println("Password generator")
	fmt.Println("------------------")
	fmt.Println("")
	fmt.Println("Inform the number of characters: ")
	number_of_characters := 0
	fmt.Scanln(&number_of_characters)

	randomString := generateRandomString(number_of_characters)

	fmt.Println(randomString)
}