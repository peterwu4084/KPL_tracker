import numpy as np
import pandas as pd

team_assault = pd.read_csv('team_assault.csv', index_col=0)
team_resource = pd.read_csv('team_resource.csv', index_col=0)
team = pd.merge(team_assault, team_resource)

team.drop(columns=['名次', '场均经济', '场均主宰', '场均暴君', '场均主宰', 
                   '场均暴君', '场均野怪击杀量', '总推塔数', '总被推塔数'], inplace=True)
team['一血率'] = team['一血率'].apply(lambda s: float(s[:-1]))
team['主宰控制率'] = team['主宰控制率'].apply(lambda s: float(s[:-1]))
team['暴君控制率'] = team['暴君控制率'].apply(lambda s: float(s[:-1]))

team['控龙'] = team['主宰控制率'] + team['暴君控制率']
team['终结'] = team['负场场均时长']/team['胜场场均时长']
team['KDA'] = (team['场均击杀'] + team['场均助攻']) / team['场均死亡']

team.drop(columns=['胜场场均时长', '负场场均时长', '主宰控制率', '暴君控制率',
                  '场均击杀', '场均助攻', '场均死亡',], inplace=True)
team.rename(columns={'分钟经济': '发育', '一血率': '一血', '场均推塔数': '推塔'}, inplace=True)
power_list = team.columns[1:]
team[power_list] = team[power_list].apply(lambda x: 5 * (x - np.min(x)) / (np.max(x) - np.min(x)) + 5)
team.to_csv('Data/team.csv')

player_kda = pd.read_csv('player_kda.csv', index_col=0)
player_power = pd.read_csv('player_power.csv', index_col=0)
player_power = player_power.sort_values(by='名次')
player_power.index = range(len(player_power))
player = pd.merge(player_kda, player_power)

player = player[['选手', 'KDA', '参团率', '分均输出', '分均承伤', '分均经济']]
player['参团率'] = player['参团率'].apply(lambda s: float(s[:-1]))
power_list = player.columns[1:]
player[power_list] = player[power_list].apply(lambda x: 10 * x / np.max(x))

player.rename(columns={'选手': 'ID',
                       '参团率': '参团',
                       '分均输出': '输出',
                       '分均承伤': '承伤',
                       '分均经济': '发育'},
             inplace=True)
player.to_csv('Data/player.csv')
