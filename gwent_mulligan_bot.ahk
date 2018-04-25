CoordMode, Mouse, Client
SetKeyDelay, 300

EnterPracticeMode() {
	Sleep, 15000
	if WinExist("ahk_exe Gwent.exe")
		WinActivate
	MouseMove, 0, 0
	Send, {Enter 2}
	Sleep, 20000
	Send, {Enter}
	Sleep, 5000
	Send, {Down}{Wheeldown}
	Sleep, 1000
	Send, {Enter}
	Sleep, 2000
}

SampleMulligan() {
	Send, {Enter}
	Sleep, 17000
	MouseMove, 1, 1
	Sleep, 500
	Send, {LWin down}{PrintScreen}{LWin up}
	Loop, 2 {
		Send, {Right}{Enter}
		Sleep, 500
	}
	Send, {Right}{Enter}{Right}
	Sleep, 1000
	Send, {Left 30}
	Sleep, 10000
	Send, {Enter 2}
	Sleep, 2000
	MouseMove 0, 0
	Sleep, 500
	Send, {LWin down}{PrintScreen}{LWin up}{Right}{Enter 10}{Esc}
	Sleep, 1000
	Send, {Enter}
	Sleep, 4000
	Send, {Esc}
	Sleep, 1000
	Send, {Esc} ; This key isn't supposed to do anything. It fires - and whiffs - during a loading screen when the script is in sync. The key's purpose is to guarantee re-syncing if the script has de-synced.
	Sleep, 14000
}

ExitGame() {
	if WinActive("ahk_exe Gwent.exe") {
		Send, {Esc}
		Sleep, 1000
		Send, {Esc}
		Sleep, 1000
		Send, {Enter}
		Sleep, 20000
	}
	if WinExist("ahk_exe Gwent.exe") {
		WinKill
		Sleep, 20000
	}
	MouseMove 1, 1
}

InputBox, n, Number of batches, 
	(
	The bot runs for 50 samplings before restarting Gwent.

Enter the number of such 50 sample batches you want.

E.g. '12' runs the bot 12 times -> 12x50 = 600 samplings.
	)
Loop, %n% {
	Run, Gwent.exe, C:\Program Files (x86)\GOG Galaxy\Games\Gwent
	EnterPracticeMode()
	Loop, 50 {
		if WinActive("ahk_exe Gwent.exe")
			SampleMulligan()
		else
			break
	}
	ExitGame()
}
