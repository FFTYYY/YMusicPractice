
#统一用升号

对应表 = {
"B8":		7902.13  , 
"A#8":		7458.62  , 
"A8":		7040.00  , 
"G#8":		6644.88  , 
"G8":		6271.93  , 
"F#8":		5919.91  , 
"F8":		5587.65  , 
"E8":		5274.04  , 
"D#8":		4978.03  , 
"D8":		4698.64  , 
"C#8":		4434.92  , 
"C8":		4186.01  , 
"B7":		3951.07  , 
"A#7":		3729.31  , 
"A7":		3520.00  , 
"G#7":		3322.44  , 
"G7":		3135.96  , 
"F#7":		2959.96  , 
"F7":		2793.83  , 
"E7":		2637.02  , 
"D#7":		2489.02  , 
"D7":		2349.32  , 
"C#7":		2217.46  , 
"C7":		2093.00  , 
"B6":		1975.53  , 
"A#6":		1864.66  , 
"A6":		1760.00  , 
"G#6":		1661.22  , 
"G6":		1567.98  , 
"F#6":		1479.98  , 
"F6":		1396.91  , 
"E6":		1318.51  , 
"D#6":		1244.51  , 
"D6":		1174.66  , 
"C#6":		1108.73  , 
"C6":		1046.50  , 
"B5":		987.767  , 
"A#5":		932.328  , 
"A5":		880.000  , 
"G#5":		830.609  , 
"G5":		783.991  , 
"F#5":		739.989  , 
"F5":		698.456  , 
"E5":		659.255  , 
"D#5":		622.254  , 
"D5":		587.330  , 
"C#5":		554.365  , 
"C5":		523.251  , 
"B4":		493.883  , 
"A#4":		466.164  , 
"A4":		440.000  , 
"G#4":		415.305  , 
"G4":		391.995  , 
"F#4":		369.994  , 
"F4":		349.228  , 
"E4":		329.628  , 
"D#4":		311.127  , 
"D4":		293.665  , 
"C#4":		277.183  , 
"C4":		261.626  , 
"B3":		246.942  , 
"A#3":		233.082  , 
"A3":		220.000  , 
"G#3":		207.652  , 
"G3":		195.998  , 
"F#3":		184.997  , 
"F3":		174.614  , 
"E3":		164.814  , 
"D#3":		155.563  , 
"D3":		146.832  , 
"C#3":		138.591  , 
"C3":		130.813  , 
"B2":		123.471  , 
"A#2":		116.541  , 
"A2":		110.000  , 
"G#2":		103.826  , 
"G2":		97.9989  , 
"F#2":		92.4986  , 
"F2":		87.3071  , 
"E2":		82.4069  , 
"D#2":		77.7817  , 
"D2":		73.4162  , 
"C#2":		69.2957  , 
"C2":		65.4064  , 
"B1":		61.7354  , 
"A#1":		58.2705  , 
"A1":		55.0000  , 
"G#1":		51.9131  , 
"G1":		48.9994  , 
"F#1":		46.2493  , 
"F1":		43.6535  , 
"E1":		41.2034  , 
"D#1":		38.8909  , 
"D1":		36.7081  , 
"C#1":		34.6478  , 
"C1":		32.7032  , 
"B0":		30.8677  , 
"A#0":		29.1352  , 
"A0":		27.5000  , 
"G#0":		25.9565  , 
"G0":		24.4997  , 
"F#0":		23.1247  , 
"F0":		21.8268  , 
"E0":		20.6017  , 
"D#0":		19.4454  , 
"D0":		18.3540  , 
"C#0":		17.3239  , 
"C0":		16.3516  , 
}

记号列表 = list(对应表)
记号列表.reverse() #从最低音开始数

n = len(记号列表)

def 获得记号编号(s):
	return 记号列表.index(s)

def 获得记号区间(s1 , s2):
	l = 获得记号编号(s1)
	r = 获得记号编号(s2)
	return 记号列表[l : r+1]

def 去除黑键(l):
	'''输入一个唱名列表，去除其中所有黑键'''
	return [x for x in l if "#" not in x]

def 从记号获得频率(s):
	return 对应表[s]

def 获得最接近记号(f):
	mrk = None
	dif = -1
	for s in 记号列表:
		if dif < 0 or abs(从记号获得频率(s) - f) < dif:
			dif = abs(从记号获得频率(s) - f)
			mrk = s
	return mrk , dif
