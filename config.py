account = {
	"Username":"kumaru1",
	"Password":"aqmar2012"
}
license = "STB-0FBGA-C4ANL-H8F8F-DVC"
tradeset = {
	"BaseTrade":"0.00001",
	"C1":"50", 							#5-95
	"C2":"65", 							#5-95
	"NumberOfTrade":"5", 				#max limit 200
	"ResetOnWin":"1", 					# 0=OFF 1=ON, If ON Change "IncreaseOnWinPercent" to 0
	"ResetOnLose":"0", 					# 0=OFF 1=ON, If ON Change "IncreaseOnLosePercent" to 0
	"MultiplyOnWin":"0", 				## 0 to OFF || 0.5 = 50%, 1.0 = 100% (double), 2.0 = 200% (triple)
	"MultiplyOnLose":"2.0", 			## 0 to OFF || 0.5 = 50%, 1.0 = 100% (double), 2.0 = 200% (triple)
	"MaxBaseTrade":"0",					# 0 to OFF
	"ResetOnLoseMaxTrade":"0", 			# 0 to OFF 
	"StopOnLoseMaxTrade":"0",			# 0 to OFF
	"StopIfBalance":"0", 				# 0 to OFF
	"StopMinBalance":"0", 				# *blank* to OFF
	"ClientSeed":"412312",				#max 32 digits
	"RecoveryMultiplier":"1.5",			# 1=Default. Must More than 0. Multiply your BaseTrade If Lose
	"RecoveryIncrease":"0"	 			# 0 to OFF. Increase your BaseTrade If Lose
}

tools = {
	"AddDelayTrade":"0",				#Delay Per Trade
	"AddDelayTradeWin":"0",				#Delay Per Trade Win
	"AddDelayTradeLose":"0"				#Delay Per Trade Lose
}
