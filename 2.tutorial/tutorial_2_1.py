# 第2章 Python数理最適化チュートリアル¶
# 2.1 連立一次方程式をPythonの数理最適化ライブラリで解く

import pulp

problem = pulp.LpProblem('SLE', pulp.LpMaximize)

x = pulp.LpVariable('x', cat='Continuous')
y = pulp.LpVariable('y', cat='Continuous')

problem += 120 * x + 150 * y == 1400
problem += x + y == 10

status = problem.solve()

print('Status:', pulp.LpStatus[status])
print('x=', x.value(), 'y=', y.value())
