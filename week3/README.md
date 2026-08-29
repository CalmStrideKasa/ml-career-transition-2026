# 週3（9/15〜9/21相当）：scikit-learn実装力 ＋ 非線形材料工学①

## 概要
scikit-learnで5手法の回帰モデルを実装・比較し、あわせて非線形材料工学①（弾塑性構成則）の理論とコード化を行った週。

## 使用データ
Kaggle「California Housing Prices」（`camnugent/california-housing-prices`）。
`sklearn.datasets.fetch_california_housing()`がfigshare側の403 Forbiddenエラーで取得できなかったため、Kaggle経由でCSVを直接取得する方式に切り替えた（`week3/data/housing.csv`）。

## モデル比較表

| モデル | RMSE | R² | 備考 |
|---|---|---|---|
| Ridge(alpha=0.1) | 70,031 | 0.6257 | |
| Ridge(alpha=1) | 70,028 | 0.6258 | |
| Ridge(alpha=10) | 70,004 | 0.6260 | |
| Lasso(alpha=0.1) | 70,031 | 0.6257 | max_iter=10000でも収束せず（ConvergenceWarning） |
| Lasso(alpha=1) | 70,031 | 0.6257 | |
| Lasso(alpha=10) | 70,026 | ― | |
| RandomForest(n=100) | 検証誤差 約49,260（learning_curve、最大データ量時） | ― | 過学習気味。訓練誤差との隙間が最後まで縮まらない |
| XGBoost(n=1) | 92,978 | 0.340 | |
| XGBoost(n=10) | 55,533 | 0.765 | |
| XGBoost(n=100) | **47,499** | **0.828** | 5手法中最良。学習曲線の隙間は縮小傾向 |
| LightGBM | ― | ― | Windows環境で`OSError: access violation`が発生。バージョン確認・再インストールでも解消せず、保留 |

## 学習曲線

- `randomforest_learning_curve.png`：訓練誤差と検証誤差の隙間が最後まで縮まらず、過学習気味
- `xgboost_learning_curve.png`：データ件数を増やすほど訓練誤差・検証誤差が近づく、より健全な傾向

## 成果物（コード）

| ファイル | 内容 |
|---|---|
| `day1_csv_preprocessing.py` | CSV読み込み、欠損値処理（`total_bedrooms`を平均値で補完）、カテゴリ変数のOne-Hot Encoding（`ocean_proximity`） |
| `day1_linear_regression.py` | 線形回帰ベースライン |
| `day1_elastoplastic.py` | 非線形材料工学①：`compute_stress_elastoplastic`関数 |
| `day2_ridge_lasso.py` | Ridge/Lasso（alpha=[0.1, 1, 10]）、StandardScalerによる標準化 |
| `day3_randomforest.py` | RandomForestRegressor、学習曲線 |
| `day4_xgboost_lgbm.py` | XGBoost/LightGBM実装（LightGBMは環境問題で保留） |

## 非線形材料工学①：弾塑性構成則

`compute_stress_elastoplastic(strain, E, sigma_y, H=0.0)`を実装。弾性域・塑性域の境界（ε=ε_yは弾性側に含める）、引張・圧縮の対称性を考慮した設計。

検証済みの値（手計算と一致）：
- 弾性域：E=200GPa, σ_y=250MPa, ε=0.0008 → σ=160MPa
- 塑性域：E=200GPa, σ_y=250MPa, H=10GPa, ε=0.003 → σ=267.5MPa
- 圧縮側（対称性確認）：ε=-0.003 → σ=-267.5MPa

## つまずいた点・学んだこと

- **StandardScalerの必要性**：特徴量のスケールが大きく異なると（`total_rooms`は数千〜数万、`housing_median_age`は1〜50など）、Lassoが収束しにくくなる。標準化（平均0、分散1）で緩和される
- **XGBoostの列名制約**：`pd.get_dummies()`で生成された列名に`<`が含まれる（`ocean_proximity_<1H OCEAN`）と、XGBoostが`ValueError`を出す。列名の置換は`pd.get_dummies()`の**後**に行う必要がある
- **RandomForestとXGBoostの学習曲線の違い**：RandomForest（バギング）は木を増やしても過学習しにくいが分散の低減は頭打ちになる。XGBoost（ブースティング）は木を増やしすぎると過学習しやすいが、健全な範囲では訓練・検証誤差の隙間が縮まっていく
- **環境依存の問題は保留にして前進する判断**：`fetch_california_housing`の403、LightGBMのaccess violationは、いずれもコードのロジックではなく環境側の問題と切り分け、代替手段（Kaggle CSV、XGBoostのみで進行）で学習を止めないことを優先した
