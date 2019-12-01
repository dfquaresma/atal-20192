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

var father []int
var rank   []int
var cons   []*con
func main() {
  // STDOUT MUST BE FLUSHED MANUALLY!!!
  defer writer.Flush()
  var m, n int
  for {
    scanf("%d %d\n", &m, &n)
    if m == 0 && n == 0 { break }
    
    cons  = make([]*con, n)
    var x, y, z, max int
    for i := 0; i < n; i++ {
      scanf("%d %d ", &x, &y)
      if x == 0 && y == 0 {
        break
      }
      scanf("%d\n", &z)
      cons[i]  = &con{x, y, z}
      max += z
    }
    initFatherAndRank(m+1)
    minimumCoverTreeSum := kruskal(m, n)
    printf(strconv.Itoa(max - minimumCoverTreeSum))
  }
}

func kruskal(m, n int) int {
  sort.SliceStable(cons, func(i, j int) bool { return cons[i].z < cons[j].z })
  minimumCoverTreeSum := 0
  for _, c := range cons {
    if find(c.x) != find(c.y) {
      union(c.x, c.y)
      minimumCoverTreeSum += c.z
    }
  }
  return minimumCoverTreeSum
}

func find(nodeIndex int) int {
    if (father[nodeIndex] == nodeIndex) {
      return nodeIndex
    }
    father[nodeIndex] = find(father[nodeIndex])
    return father[nodeIndex]
}

func union(nodeAIndex, nodeBIndex int) {
    nodeAIndex = find(nodeAIndex);
    nodeBIndex = find(nodeBIndex);
    if rank[nodeAIndex] < rank[nodeBIndex] {
      tmp := nodeAIndex
      nodeAIndex = nodeBIndex
      nodeBIndex = tmp
    }
    rank[nodeAIndex]  += rank[nodeBIndex];
    father[nodeBIndex] = father[nodeAIndex];
}

func initFatherAndRank(size int) {
  father = make([]int, size)
  rank   = make([]int, size)
  for i := 1; i < size; i++ {
    father[i] = i;
    rank[i] = 1;
  } 
}
