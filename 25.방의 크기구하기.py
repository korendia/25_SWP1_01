from collections import deque

from statsmodels.graphics.tukeyplot import results

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(start_x,start_y,grid,visited,h,w):
    queue=deque()
    queue.append((start_x,start_y))
    visited[start_x][start_y]=True
    room_size=1

    while queue:
        x,y=queue.popleft()
        for dir in range(4):
            nx,ny=x+dx[dir],y+dy[dir]
            if 0<=nx<h and 0<=ny<w:
                if not visited[nx][ny] and grid[nx][ny]=='.':
                    visited[nx][ny]=True
                    queue.append((nx,ny))
                    room_size+=1
    return room_size

def solve_case(grid,h,w):
    visited=[[False]*w for i in range(h)]
    room_size=[]

    for i in range(h):
        for j in range(w):
            if grid[i][j]=='.'and not visited[i][j]:
                size=bfs(i,j,grid,visited,h,w)
                room_size.append(size)
    room_size.sort(reverse=True)
    return room_size

result=[]

if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        w,h=map(int,input().split())
        grid=[list(input().strip())for j in range(h)]
        sizes=solve_case(grid,h,w)
        result.append(sizes)

    for sizes in result:
        print(len(sizes))
        print(" ".join(map(str,sizes)))