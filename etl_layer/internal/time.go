package internal

import (
	"strings"
	"time"
)

type MyTime struct {
	time.Time
}

func (mt *MyTime) UnmarshalJSON(b []byte) (err error) {
	s := string(b)

	s = strings.Trim(s, "\"")
	// Try to parse with timezone offset
	t, err := time.Parse(time.RFC3339, s)
	if err != nil {
		// If that fails, try to parse without timezone offset
		t, err = time.Parse("2006-01-02T15:04:05", s)
	}

	mt.Time = t
	return
}