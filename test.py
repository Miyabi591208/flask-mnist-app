# Counterのインポート
from collections import Counter
# Counterに文字列を格納、文字の出現頻度を数え上げる
d = Counter("A Counter is a dict subclass for counting hashable objects.")

# 最も多い5要素を並べる
print(d.most_common(6))