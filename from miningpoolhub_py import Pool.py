from miningpoolhub_py import Pool

pool_instance = Pool('ethereum')
pool_instance.get_all_user_balances()
pool_instance.get_auto_switching_and_profits_statistics()
pool_instance.get_mining_profit_and_statistics()