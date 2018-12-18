import matplotlib.pyplot as plt

def interpolar(media):
  v = list(media.values())

  for i in v:
    flag = max(v[v.index(i):], key=float)
    if i < flag:
      v[i] = flag
  
  return v

def plot(media):
  y = interpolar(media)
  x = media.keys()

  print(x)
  print(y)
  plt.plot(x, y, 'g')
  plt.axis( [0, 100, 0, 100])

  plt.title('Média de precisão por revocação')

  plt.xlabel('Revocação')
  plt.ylabel('Precisão')
  plt.show()