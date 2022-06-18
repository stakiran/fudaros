
# 1

## skippee.md

```
// コメントも許す
// # だと markdown エディタ側で見出し行として扱われることがあってうざいのでなし
// // だけでいい

7 一週間後でいいや
3 3日後にいくやつ
30 一月くらいあとにいくやつ
/20 今月の20日
7/20 今年の7/20
2023/4/1 2021/04/01に
```

## timeline.md

```
yyyy/mm/dd (dow) task
yyyy/mm/dd (dow) task
yyyy/mm/dd (dow) task
```

## today.md

```
task
task
task
```

## UI
- KISS 的にする
- 呼び出し元は何でもいいけど、🐰は ahk ベースで考える

## アルゴリズム 処理 実装

```scb
timeline 側の重複は無視する
 `7 task1` した後、やっぱり `6 task1` とした場合、7日後にセットされた方は古いが、無視する
 自分で timeline.md 見て何とかしろ

dryrun
 timeline_dryrun.md つくればいいか
 常にまるごと上書き
 format
  2022/06/25 (Sat) 一週間後でいいや from 「7 一週間後でいいや」
  後ろに`from 「...」`つける、くらいでいいだろ
```


## テスト
skippee to timeline
timeline to today with 今日の日付

