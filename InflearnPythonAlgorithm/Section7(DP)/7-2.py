# 네트워크 선 자르기(Top-Down)

def dfs(len):
    if dy[len] > 0:
        # 메모이제이션
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = dfs(len - 1) + dfs(len - 2)
        return dy[len]

if __name__=="__main__":
    n = int(input())
    dy = [0] * (n + 1)
    print(dfs(n))