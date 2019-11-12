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
 
var n, count int
var matrix [1001][1001]int
 
func main() {
  // STDOUT MUST BE FLUSHED MANUALLY!!!
  defer writer.Flush()
  
  scanf("%d %d\n", &n)
  for i := 1; i <= n; i++ {
    var a, b int
    scanf("%d %d\n", &a, &b)
    matrix[a][b] = 1
  }
  
  for i := 1; i <= 1000; i++ {
    for j := 1; j <= 1000; j++ {
      if matrix[i][j] == 1 {
        count++
        dfs_adaptada(i, j)
        break
      }
    }
  }
  printf(strconv.Itoa(count - 1))
}
 
func dfs_adaptada(x, y int) () {
  if matrix[x][y] == 1 {
    matrix[x][y] = 2
    for i := 1; i <= 1000; i++ {
      if matrix[i][y] == 1 {
        dfs_adaptada(i, y)
      }
    }
    for j := 1; j <= 1000; j++ {
      if matrix[x][j] == 1 {
        dfs_adaptada(x, j)
      }
    }
  }
}
