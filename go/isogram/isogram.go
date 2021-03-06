// Package isogram checks for isograms.
package isogram

import (
	"strings"
	"unicode"

	mapset "github.com/deckarep/golang-set"
)

// IsIsogram determines if a string is an isogram.
func IsIsogram(s string) bool {
	found := make(map[rune]bool)
	for _, r := range strings.ToUpper(s) {
		if !unicode.IsLetter(r) {
			continue
		}
		if found[r] {
			return false
		}
		found[r] = true
	}
	return true
}

// IsIsogramMapset determines if a string is an isogram using a mapset.
func IsIsogramMapset(s string) bool {
	found := mapset.NewSet()
	for _, r := range strings.ToUpper(s) {
		if !unicode.IsLetter(r) {
			continue
		}
		if found.Contains(r) {
			return false
		}
		found.Add(r)
	}
	return true
}
