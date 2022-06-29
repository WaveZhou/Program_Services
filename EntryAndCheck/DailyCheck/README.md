# DailyCheck

每日产品持仓、风控


### 数据来源


- 银行流水：数据库 `jiuming_journal.银行标准流水`
- 交易流水：陈田田发送版
    - 股票
    - 期货
    - 收益互换
- 在途申赎流水：数据库 `jiuming_ta_new.在途申赎流水表`


#### 数据时间点


- 8:00 前一天托管估值表、港股收益互换对账单、券商对账单
- 14:00 前一天美股收益互换对账单
- 15:00 当天交易流水、银行流水、在途申赎


### 操作时间点

- 当天收盘后：根据当天流水获得基于当天信息的持仓变动
- 第二天下午两点之后：根据托管估值表、港股收益互换对账单、券商对账单、美股收益互换对账单计算和核对净值


### 汇率标签


- wind获取：
    - 港股通汇率：HKDCNYSET.HKS
- 对账单读取：
    - 港股收益互换汇率：HKDCNYSET.SWAP
    - 美股收益互换汇率：USDCNYSET.SWAP


### 收益互换数据获取


|科目|对账单数据|
|---|---|
|名义本金|累计支取预付金净额（结算货币）|
|已付利息|应付已付利率收益金额和预付金返息金额加总的近似值(交易货币)|
|累计应付利息|累计利率收益金额和预付金返息金额的加总近似值(交易货币)|
|标的成本|初始保障金额加总的近似值(交易货币)|
|结转预付金|结转预付金余额（交易货币）|


工作流程

持仓明细表及其相关表的更新：
早上：
1.读取托管估值表，核对净值、份额、净资产
读取其中税费数据，更新
和小何对净值
核对好的净值数据更新到最新的《持仓明细表》“历史净值”
相应的净资产数据更新到《管理费》表”净资产”
更新好的久2、久1、久8、全球1、稳健1净值更新到《管理费》表“应收管理费返还”

2.读取港股收益互换对账单，核对

3.读取券商对账单账户余额（主要的产品、账户以及昨天有交易的）到《资金股份-独立明细》“余额核对”
差额更新入《资金股份-独立明细》“余额变动明细”，汇总后更新入数据库表《1余额变动明细》
有货基的账户，久铭300指数、久铭500指数、稳健6号、浦睿1号、稳健23号，核对货基红股数目，差额更新入《资金股份-独立明细》“持仓变动明细”

下午2点
4.读取美股收益互换对账单，核对
5.最新的净值数据更新到《管理费》表”净资产”，并新增1条记录
6.更新《资金股份-独立明细》“汇率”中港股通、海外基金使用的汇率

收盘后：
6.复制前一日《持仓明细表》，
“历史净值”复制前日净值
 “资产规模表”A1更新日期
“现金余额加利息汇总”复制累计计息到前日计息

7. 《资金股份-独立宏》
交易流水、银行转账流水、在途申赎流水、处理成统一格式，更新入数据库
运行数据库函数《1收益互换汇总》
导出数据库《1每日余额汇总》、《1每日持仓汇总》、《每日SWAP余额汇总》，更新到《持仓明细表》“持仓余额明细”、“收益互换明细”
申购赎回、期货买卖要手工处理；

注意点：
1.最低佣金
2.港股通
3.EB卖出有利息
4.申购赎回确认
5.收益互换
6.灵活性