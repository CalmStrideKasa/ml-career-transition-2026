\# Career Transition: Fluid Dynamics → Surrogate Modeling \& Physics-Informed ML



\## プロジェクトの目的

流体力学/CFDのバックグラウンドを活かし、サロゲートモデル × Physics-Informed Machine Learning

の専門家としてフルリモート・年収アップの転職を実現するための学習記録リポジトリです。

2026年9月〜2027年8月の12ヶ月で、Python/ML基礎からポートフォリオ構築、転職活動までを実行します。



\## 進捗ダッシュボード



| 月 | フェーズ | ステータス |

|---|---|---|

| 9月 | Python/ML基礎固め① | 進行中 |

| 10月 | Python/ML基礎固め② | 未着手 |

| 11月 | ML応用①PINNs | 未着手 |

| 12月 | ML応用②融合 | 未着手 |

| 1月 | ポートフォリオ着手 | 未着手 |

| 2月 | ポートフォリオ完成 | 未着手 |

| 3月 | 発信・実績化① | 未着手 |

| 4月 | MLOps基礎 | 未着手 |

| 5月 | 発信・実績化② | 未着手 |

| 6月 | 転職準備① | 未着手 |

| 7月 | 転職活動本番① | 未着手 |

| 8月 | 転職活動本番② | 未着手 |



\## セットアップ



```bash

python -m venv ml\_journey

ml\_journey\\Scripts\\activate

pip install -r requirements.txt

```



または Docker を使う場合:



```bash

docker build -t ml\_journey .

docker run -it ml\_journey python

```



\## テストの実行



```bash

pytest --cov=bank\_account --cov-report=term-missing

```

