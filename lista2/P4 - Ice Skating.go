package main

import (
  "fmt"
  "bufio"
  "os"
)

// Took from here: https://www.codementor.io/tucnak/using-golang-for-competitive-programming-h8lhvxzt3
var reader *bufio.Reader = bufio.NewReaderSize(os.Stdin, 10000000)
var writer *bufio.Writer = bufio.NewWriterSize(os.Stdout,10000000)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanf(f string, a ...interface{}) { fmt.Fscanf(reader, f, a...) }

func main() {
  // STDOUT MUST BE FLUSHED MANUALLY!!!
  defer writer.Flush()

  var n int
  scanf("%d\n", &n)
  var xcount [1001]int
  var ycount [1001]int
  var matrix [1001][1001]int
  for i := 1; i <= n; i++ {
    var x, y int
    scanf("%d %d\n", &x, &y)
    matrix[x][y] = 1
    xcount[x]++;
    ycount[y]++;
  }
  count := 0
  for i := 1; i <= 1000; i++ {
    for j := 1; i <= 1000; i++ {
      if matrix[i][j] == 1 && xcount[i] == 1 && ycount[j] == 1 {
        count++
      }
    }
  }
  fmt.Println(count)
}
