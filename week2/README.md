# 週2（9/8〜9/14相当）：数理×実務データ

## 概要
NumPy/Pandasでの実務データ処理、勾配降下法・損失関数のスクラッチ実装、可視化を行った週。

## 成果物

| ファイル | 内容 |
|---|---|
| `broadcast_demo.py` | NumPyのブロードキャストの仕組みを確認するデモ |
| `sensor_dataframe.py` | センサーデータ生成・Pandasでのデータフレーム操作 |
| `senser_standardization.py` | センサーデータの標準化処理 |
| `sensor_profile_report.html` | ydata-profilingによるデータプロファイリングレポート |
| `sensor_visualization.py` | ヒストグラム・散布図の可視化コード |
| `temperature_histogram.png` / `temp_vs_pressure_scatter.png` | 静的可視化（matplotlib） |
| `temperature_histogram_interactive.html` / `temp_vs_pressure_scatter_interactive.html` | インタラクティブ可視化（plotly） |
| `gradient_descent_comparison.py` | 勾配降下法3手法（Batch/SGD/Mini-batch）のスクラッチ実装・比較 |
| `sgd_per_step_loss.png` / `loss_curve_comparison.png` | 勾配降下法の収束比較プロット |
| `loss_comparison.py` / `loss_function_shapes.png` | MSE/MAE/Huber損失の比較 |
| `week2_summary.ipynb` | 週2成果物の統合Notebook（Restart & Run All確認済み） |

## 学んだこと
- NumPyのブロードキャストの仕組み
- Pandasでのgroupby集計・欠損値処理（ffill/bfill/mean fill）・条件フィルタ
- 勾配降下法3手法の違い（epoch単位/step単位での収束の見え方の違い）
- MSE/MAE/Huber損失の外れ値への頑健性の違い
- PDE分類（楕円・放物・双曲）の判別式と、時間微分の階数と物理的性質（拡散/波動）の関係
