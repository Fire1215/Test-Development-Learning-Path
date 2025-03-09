name="青埂峰"
stock_price=1.8821
stock_code='003032'
stock_price_daily_growth_rate=1.5
growth_days=7
stock_price1=stock_price_daily_growth_rate**growth_days*stock_price
+stock_price
message="""公司名称：%s, 股票代码：%s, 股票价格为：%.2f, 经专业人士统计, 
          该股每日增长率为：%.2f, 经%d天后, 该公司股票价格为: %.2f
          """ % (name, stock_code, stock_price, stock_price_daily_growth_rate, 
                 growth_days, stock_price1) # 三引号注释可直接换行
print(message)
# print(f"公司名称：{name}, 股票代码：{stock_code}, 股票价格为：{stock_price}, 
# 经专业人士统计, 该股增长率为：{stock_price_daily_growth_rate}, 经{growth_days}天后, 
# 该公司股票价格为: {stock_price1}")
