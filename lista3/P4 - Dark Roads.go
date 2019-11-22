package main
 
import (
  "fmt"
  "bufio"
  "os"
  "strconv"
  "sort"
)
 
// Took from here: https://www.codementor.io/tucnak/using-golang-for-competitive-programming-h8lhvxzt3
var reader *bufio.Reader = bufio.NewReaderSize(os.Stdin, 10000000)
var writer *bufio.Writer = bufio.NewWriterSize(os.Stdout,10000000)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanf(f string, a ...interface{}) { fmt.Fscanf(reader, f, a...) }

type con struct {
	x int
	y int
  z int
}

func main() {
  // STDOUT MUST BE FLUSHED MANUALLY!!!
  defer writer.Flush()
  var m, n int
  scanf("%d %d\n", &m, &n)
  cons := make([]*con, n)
  var x, y, z, max int
  for i := 0; i < n; i++ {
    scanf("%d %d ", &x, &y)
    if x == 0 && y == 0 {
      break
    }
    scanf("%d\n", &z)
    cons[i] = &con{x, y, z}
    max += z
  }
  sort.SliceStable(cons, func(i, j int) bool { return cons[i].z < cons[j].z })
  kruskal := make([]int, m+1)
  for i := 1; i <= m; i++ {
  }
  var shortestPath int
  for i := 1; i <= m; i++ {
    shortestPath += kruskal[i]
  }
  printf(strconv.Itoa(max - shortestPath))
}
