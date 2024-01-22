# graph-generator

Generating images from adjacency tables with graphviz

- Edit edges.txt 
- Run main.py

### Example

![example.png](example.png)

```
1 2 flow=1,cost=0
1 2 flow=inf,cost=100w
2 3 flow=1,cost=0
2 3 flow=inf,cost=100w
3 4 flow=1,cost=0
3 4 flow=inf,cost=100w
1 5 flow=1,cost=0
1 5 flow=inf,cost=100w
5 6 flow=1,cost=0
5 6 flow=inf,cost=100w
6 4 flow=1,cost=0
6 4 flow=inf,cost=100w
1 7 flow=1,cost=0
1 7 flow=inf,cost=100w
7 4 flow=1,cost=0
7 4 flow=inf,cost=100w
1' 2' flow=1,cost=0
1' 2' flow=inf,cost=100w
2' 3' flow=1,cost=0
2' 3' flow=inf,cost=100w
3' 4' flow=1,cost=0
3' 4' flow=inf,cost=100w
1' 5' flow=1,cost=0
1' 5' flow=inf,cost=100w
5' 6' flow=1,cost=0
5' 6' flow=inf,cost=100w
6' 4' flow=1,cost=0
6' 4' flow=inf,cost=100w
1' 7' flow=1,cost=0
1' 7' flow=inf,cost=100w
7' 4' flow=1,cost=0
7' 4' flow=inf,cost=100w
1'' 2'' flow=1,cost=0
1'' 2'' flow=inf,cost=100w
2'' 3'' flow=1,cost=0
2'' 3'' flow=inf,cost=100w
3'' 4'' flow=1,cost=0
3'' 4'' flow=inf,cost=100w
1'' 5'' flow=1,cost=0
1'' 5'' flow=inf,cost=100w
5'' 6'' flow=1,cost=0
5'' 6'' flow=inf,cost=100w
6'' 4'' flow=1,cost=0
6'' 4'' flow=inf,cost=100w
1'' 7'' flow=1,cost=0
1'' 7'' flow=inf,cost=100w
7'' 4'' flow=1,cost=0
7'' 4'' flow=inf,cost=100w
s 1
s 1'
s 1''
4 t
4' t
4'' t
```