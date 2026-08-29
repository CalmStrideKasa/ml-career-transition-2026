# 週1（9/1〜9/7相当）：基盤構築

## 概要
Python環境構築、Gitワークフロー、クラス設計・テスト・カバレッジ計測の基礎を固めた週。

## 成果物

| ファイル | 内容 |
|---|---|
| `bank_account.py` | `BankAccount`クラス（コンストラクタ、deposit、withdraw、`__repr__`、型ヒント、Google形式docstring） |
| `demo_bank_account.py` | `BankAccount`クラスの動作確認用デモスクリプト |
| `test_bank_account.py` | pytestによるテストコード（7テスト、カバレッジ100%達成） |

## 実行方法

```bash
cd week1
pytest --cov
```

## 学んだこと
- 型ヒント・docstring（Args/Returns/Raises）を備えたクラス設計
- pytestでのテスト作成とカバレッジ計測
- ブランチ運用・PR・GitHub Actions（CI）でのテスト自動実行
