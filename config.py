account = {
	"Username":"xxx",
	"Password":"xxx"
}
license = "xxx"
tradeset = {
	"BaseTrade":"0.00001",
	"C1":"0", 							#5-95
	"C2":"0", 							#5-95
	"NumberOfTrade":"0", 				#Max limit 200, How much you want trading in one time
	"ResetOnWin":"0", 					# 0=OFF 1=ON, If ON Change "MultiplyOnWin" to 0
	"ResetOnLose":"0", 					# 0=OFF 1=ON, If ON Change "MultiplyOnLose" to 0
	"MultiplyOnWin":"0", 				## 0 to OFF || 0.5 = 50%, 1.0 = 100% (double), 2.0 = 200% (triple)
	"MultiplyOnLose":"0", 			## 0 to OFF || 0.5 = 50%, 1.0 = 100% (double), 2.0 = 200% (triple)
	"MaxBaseTrade":"0",					# 0 to OFF
	"ResetOnLoseMaxTrade":"0", 			# 0 to OFF 
	"StopOnLoseMaxTrade":"0",			# 0 to OFF
	"StopIfBalance":"0", 				# 0 to OFF
	"StopMinBalance":"", 				# *blank* to OFF
	"ClientSeed":"999999",				#max 32 digits
	"RecoveryMultiplier":"0",			# 1=Default. Must More than 0. Multiply your BaseTrade If Lose
	"RecoveryIncrease":"0"	 			# 0 to OFF. Increase your BaseTrade If Lose
}

tools = {
	"AddDelayTrade":"0",				#Delay Per Trade
	"AddDelayTradeWin":"0",				#Delay Per Trade Win
	"AddDelayTradeLose":"0"				#Delay Per Trade Lose
}
