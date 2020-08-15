account = {
	"Username":"xxx",
	"Password":"xxx"
}
license = "xxx"
tradeset = {
	"BaseTrade":"0.00001",
	"C1":"55", 							#5-95
	"C2":"65", 							#5-95
	"NumberOfTrade":"0", 				#max limit 200 					#ON/OFF
	"MultiplyOnWin":"0", 				## 0 untuk OFF || 0.5 = 50%, 1.0 = 100% (double), 2.0 = 200% (triple)
	"MultiplyOnLose":"0", 				## 0 untuk OFF || 0.5 = 50%, 1.0 = 100% (double), 2.0 = 200% (triple)
	"MaxBaseTrade":"0",					# 0 untuk OFF
	"ResetOnLoseMaxTrade":"OFF", 		# ON/OFF
	"StopOnLoseMaxTrade":"OFF",			# ON/OFF
	"TargetProfit":"0",				#0 untuk OFF
	"ClientSeed":"0",				#max 32 digits
	"RecoveryMultiplier":"0",			# 1 untuk OFF
	"RecoveryIncrease":"0"	 			# 0 untuk OFF. Increase your BaseTrade If Lose
}

tools = {
	"AddDelayTrade":"0",				#Delay Per Trade
	"AddDelayTradeWin":"0",				#Delay Per Trade Win
	"AddDelayTradeLose":"0"				#Delay Per Trade Lose
}
