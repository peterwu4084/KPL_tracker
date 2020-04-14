# Introduction

* crawl data about 2020 KPL (King Pro League) from [wanplus](https://www.wanplus.com/).

* compare the abilities (self-designed) between teams and players interactive plotting.

  + Team abilities
    1. KDA: (场均击杀 + 场均助攻) / 场均死亡
    2. 发育: 分钟经济
    3. 一血: 一血率
    4. 推塔: 场均推塔数
    5. 控龙: 暴君控制率 + 主宰控制率
    6. 终结: 负场场均时长 / 胜场场均时长
  + Player abilities
    1. KDA: KDA
    2. 参团: 参团率
    3. 输出: 分均输出
    4. 承伤: 分均承伤
    5. 发育: 分均经济

  Team abilities were normalized to [5, 10] and player abilities were normalized to [0, 10].

# Prerequisites

* python3
* plotly 4.6
* numpy
* pandas
* selenium
* chromedriver
* BeautifulSoup4

# Use

1. python spider.py
2. python parse.py
3. python process.py
4. python plot.py

# Future

* To crawl detailed data about teams and players
* To crawl data about games and heroes.