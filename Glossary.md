# Glossary

## General Machine Learning and AI Terms

*Backtest* - A method for verifying an AI model by testing against existing historical data

*False negative* - A signal incorrectly interpreted as a negative (E.G. underlying data points to a BUY but algorithm misinterprets as NO PURCHASE)

*False positive* - A signal incorrectly interpreted as a positive (E.G. underlying data points to NO PURCHASE but algorithm misinterprets as BUY)

*Overfit* - The process of training an AI model which is tuned to its training data as opposed to the full real data space

*True negative* - A signal correctly intepreted as false (E.G. underlaying data points to NO PURCHASE and algorithm produces NO PURCHASE)

*True positive* - A signal correctly interpreted as true (E.G. underlying data points to BUY and algorithm produces BUY)

## Financial Terms

*Alpha* - Return over the market as a whole. An alpha of 1% means the investments return on the period was 1% greater than the market for the same period.

*Econometrics* - Application of statistical methods to financial data. Such as in Arbitrage Pricing Theory which seeks to relate macroeconomic risk factors to the pricing of financial assets

*Factor Investing* - The process of investing based on attributes associated with higher returns

*Financial Information eXchange (FIX)* - Real time securities trading protocol

*Sharpe Ratio* - Divides a portfolio's excess returns by a volatility measure to assess risk-adjusted performance. Mathematically indicates that excess returns over time may be volatility and risk as opposed to skill.

## People

### Finance

*Discretionary Portfolio Managers (PMs)* - Consume raw news and analyses then use intuition and judgement to make investment decisions. Work in silos to ensure firm diversification.

*Systematic Portfolio Managers (SPMs)* - Follow a particular theory or rationale to make investment decisions

### Quant Chain

*Data Curators* - collect, clean, index, store, adjust, and deliver data. Experts in market microstructure and data protocols such as FIX. (Chapter one is devoted to a summary of this vast field)

*Feature Analysts* - Use information theory, signal extraction/processing, visualization, labeling, weighting, classifiers, and feature importance techniques to transform raw data into informative signals. These signals can then be employed by strategists. (Chapters 2-9 and 17-19 are devoted to this aspect of the field)

*Strategists* - Financial market and economy data scientists who anaylze available feature signals in order to create a strategy experiment for a theory. (Developing strategies from available features is covered in chapters 10 and 16)

*Backtesters* - Data scientists who employ empirical and experimental techniques to validate a particular strategy against a variety of scenarios including historal data producing meta analysis for evaluation. Backtesters try to ensure that a strategy isn't overfit to the available data. These results are not communicated broadly in order to ensure future experiments remain untainted (Chapters 11 - 16 cover the backtester phase of strategy development)

*Deployment Team* - Integrates strategy code with production. These folk specialize in algorithms, and mathematical programming to ensure outgoing strategy is identical to incoming strategy while delivering in a time table which ensures strategy remains relevant. Some tooling include process schedulers, automation servers (E.G. Jenkins), voctorization, multithreading, multiprocessing, GPUs, distributed computing (E.G. Hadoop), high-performance computing (E.G. Slurm), and parallel computing techniques. (Deployment techniques are covered in chapters 20-22)
