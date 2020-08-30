account = {
	"Username":"xxx",
	"Password":"xxx"
}
license = "xxx"
tradeset = {
	"BaseTrade":"0.0001",
	"C1":"25", 					#5-95
	"C2":"35", 					#5-95
	"TradeCount":"35", 				#max limit 200
	"MultiplyOnWin":"0", 				## 0 untuk OFF 
	"MultiplyOnLose":"0.5", 			## 0 untuk OFF 
	"MaxBaseTrade":{
		"Toogle":"OFF",				#ON/OFF
		"Max":"0.001",
		"ResetOnLoseMaxTrade":"OFF", 		# ON/OFF
		"StopOnLoseMaxTrade":"OFF"},		# ON/OFF
	"ClientSeed":"999999",				#max 32 digits
}

tools = {
	"AddDelayTrade":"0",				#Delay Per Trade
	"AddDelayTradeWin":"0",				#Delay Per Trade Win
	"AddDelayTradeLose":"0",			#Delay Per Trade Lose
	"RecoveryMultiplier":"1.5",			# 1 untuk OFF. BaseTrade Lose Terakhir di Kali RecoveryMultiplier
	"RecoveryIncrease":"0",	 			# 0 untuk OFF. BaseTrade Lose Terakhir di Tambah RecoveryIncrease
	"TargetProfit":"20",				#0 untuk OFF
	"StopLoseBalance":"20", 			#0 untuk OFF
	"ForceTC1AfterLose":"ON",			#ON/OFF
	"ChangeTCAfterLose":{
		"Toogle":"ON",
		"ChangeTo":"5"} 			
}
