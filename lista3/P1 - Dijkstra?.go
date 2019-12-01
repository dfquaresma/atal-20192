# DESISTI DE FAZER EM GO 
# ABAIXO O RASCUNHO...

package main
 
import (
  "fmt"
  "bufio"
  "os"
  "math"
)
 
// Took from here: https://www.codementor.io/tucnak/using-golang-for-competitive-programming-h8lhvxzt3
var reader *bufio.Reader = bufio.NewReaderSize(os.Stdin, 10000000)
var writer *bufio.Writer = bufio.NewWriterSize(os.Stdout,10000000)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanf(f string, a ...interface{}) { fmt.Fscanf(reader, f, a...) }

type node struct {
  id             int
  index          int
  distanceToRoot int
  predecessor    int
}

var nodes []*node
var adjacencyMatrix [100][100]int
func main() {
  // STDOUT MUST BE FLUSHED MANUALLY!!!
  defer writer.Flush()
  var n, m int
  scanf("%d %d\n", &n, &m)
  var x, y, z int
  for i := 0; i < m; i++ {
    scanf("%d %d %d\n", &x, &y, &z)
    updateMatrix(x, y, z)
  }
  nodes := make([]*node, n + 1)
  nodes[1] = &node{1, 1, 0, 0}
  for i := 2; i <= n; i++ {
    nodes[i] = &node{i, i, math.MaxInt64, -1}
  }
  for i := 1; i < n; i++ {
    fmt.Printf("%d\n%v", i, nodes)
    u := extractMin()
    for j := 1; j <= n; j++ {
      if nodes[j] != nil && adjacencyMatrix[u.id][j] != 0 {
        relax(u.id, j)
      }
    }
    nodes[u.id] = nil
  }
}

// TODO
func extractMin(n int) *node {
  return nil
}

func relax(uid, vid int) {
  u, v := nodes[uid], nodes[vid]
  distanceThroughU := u.distanceToRoot + adjacencyMatrix[u.id][v.id]
  if v.distanceToRoot > distanceThroughU {
    v.distanceToRoot = distanceThroughU
    v.predecessor = u.id
  }
}

func min(a, b int) int {
    if a <= b { return a }
    return b
}

func updateMatrix(x, y, z int) {
    if adjacencyMatrix[x][y] != 0 {
      z = min(z, adjacencyMatrix[x][y])
    }
    adjacencyMatrix[x][y] = z
    adjacencyMatrix[y][x] = z
}
