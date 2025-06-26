# numpy を import
import numpy as np
# math　をインポート
import math

# 係数行列と右辺ベクトルを定義
# 以下の値はサンプル（資料の最初のほうに出てきた値）
A = np.array([[1,2,3], [2,1,1], [1,3,1]])
b = np.array([14,7,15])
# 係数行列の大きさを取得
n = A.shape[0]

# 拡大行列 G = [A, b] を作る
G = np.hstack((A, b.reshape(n, 1)))
G = G.astype(float)


# 前進代入
ExistAns = True
for k in range(0, n - 1):
    print("k = ", k, ", pivot = " , G[k, k])
    count = 0
    for l in range(k, n):
      if(G[l, k] != 0): count += 1
    if(count == 0):
      print("一意解は存在しない")
      ExistAns = False
      break
    #### 部分ピボッティングをここに実装する
    max = abs(G[k, k])
    for l in range(k , n):
        if(abs(G[l, k]) > max):
          for m in range(0, n + 1):
            G[k, m], G[l, m] = G[l, m], G[k, m]

    #### ピボッティングした後に前進消去を行う
    if(G[k, k] == 0):
      continue
    else:
      for i in range(k + 1, n):
        a = G[i, k] / G[k, k]
        for j in range(k, n + 1):
          G[i, j] -= a * G[k, j]
          if(math.isclose(G[i, j], 0, abs_tol = 1e-10)):
            G[i, j] = 0


# 解を格納する行列を宣言
x = np.zeros(n)

#### 後退代入を行う
if(G[n - 1, n - 1] == 0):
  print("一意解は存在しない")
  ExistAns = False
else:
  x[n - 1] = G[n - 1, n] / G[n - 1, n - 1]
  for i in range(n - 2, -1, -1):
    sum = 0
    for j in range(i + 1, n):
      sum += G[i, j] * x[j]
    x[i] = (G[i, n] - sum) / G[i, i]

# 解を出力
if(ExistAns):
  print(x)

