package main
 
import (
  "fmt"
  "bufio"
  "os"
  "strconv"
)
 
// Took from here: https://www.codementor.io/tucnak/using-golang-for-competitive-programming-h8lhvxzt3
var reader *bufio.Reader = bufio.NewReaderSize(os.Stdin, 10000000)
var writer *bufio.Writer = bufio.NewWriterSize(os.Stdout,10000000)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanf(f string, a ...interface{}) { fmt.Fscanf(reader, f, a...) }
 
var n, m int
var matrix [4001][4001]int
var warriors [4001]int

func main() {
  // STDOUT MUST BE FLUSHED MANUALLY!!!
  defer writer.Flush()
  
  scanf("%d %d\n", &n, &m)
  for i := 1; i <= m; i++ {
    var a, b int
    scanf("%d %d\n", &a, &b)
    matrix[a][b] = 1
    matrix[b][a] = 1
    warriors[a]++
    warriors[b]++
  }
  min := -1
  for i := 1; i <= n;  i++ {
    for j := 1; j <= n; j++ {
      if matrix[i][j] == 1 {
        for k := 1; k <= n; k++ {
          if matrix[j][k] == 1 && matrix[i][k] == 1 {
            sum := warriors[i] + warriors[j] + warriors[k]
            sum -= 6 // remove as contagens dos warriors escolhidos
            if sum < min || min == -1 {
              min = sum
            }
          }
        }
      }
    }
  }
  printf(strconv.Itoa(min))
}
