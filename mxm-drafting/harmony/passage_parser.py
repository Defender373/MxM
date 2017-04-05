from harmony.passage import Passage
from harmony.note import Note


class PassageParser:
	"""
	Parse a passage from a .mxm file
	"""

	def __init__(self, f):
		self.f = f
		self.timesigs = {}
		self.tempi = {}
		self.title = ""
		self.composer = ""
		self.period = ""
		self.parts = {}

	def __enter__(self):
		# ttysetattr etc goes here before opening and returning the file object
		self.fd = open(self.f, "r")
		self.fd.readline()
		self.fd.readline()
		self.title = self.fd.readline().rstrip().lstrip()
		self.fd.readline()
		self.composer = self.fd.readline().rstrip().lstrip()
		self.fd.readline()
		self.period = self.fd.readline().rstrip().lstrip()
		self.fd.readline() #"> Time Signatures"
		#GET TIME SIG HERE
		line = self.fd.readline().lstrip()
		while line[0] != ">":
			line = self.fd.readline().lstrip()

		#GET TEMPOs HERE
		line = self.fd.readline().lstrip()
		while line[0] != ">":
			line = self.fd.readline().lstrip()
		return self.fd

	def __exit__(self, type, value, traceback):
		self.fd.close()

	def read(self):
		line = self.fd.readline().lstrip().rstrip()
		if line[0:6] == "- Part":
			self.fd.readline().rstrip().lstrip()
			assert self.fd.readline().rstrip().lstrip() == "> Notes"
			line = self.fd.readline().lstrip().rstrip()
		return line

	def create_passage(self):
		passage = Passage()
		line = self.read()
		while line != None:
			nst = float(line.split()[0])/float(line.split()[2])
			nend = float(line.split()[3])/float(line.split()[5])
			passage.add_notes(Note(line.split()[6]%12, nst, nend - nst))
			line = self.read()


"""
> Passage
  - Title
      PASSAGE TITLE
  - Composer
      COMPOSER NAME
  - Period
      PERIOD
  > Time Signatures
      1               3 / 4
      10              1 / 4
      13              4 / 4
      14              1 / 4
      126             4 / 4

  > Tempi
      1    / 1        100
      21   / 2        100
      14   / 1        100

  > Parts
    - Part
      - Instrument
        Violin
      > Notes
          1    / 1        8    / 7        72
          8    / 7        3    / 2        74
          3    / 2        2    / 1        67
          2    / 1        2    / 1        67
          15   / 7        5    / 2        79
          5    / 2        3    / 1        78
          3    / 1        3    / 1        78
          22   / 7        7    / 2        74
          7    / 2        4    / 1        69
          4    / 1        29   / 7        72
          29   / 7        13   / 3        66
          13   / 3        9    / 2        64
          9    / 2        5    / 1        66
          5    / 1        36   / 7        74
          36   / 7        11   / 2        72
          16   / 3        11   / 2        71
          11   / 2        6    / 1        69
          6    / 1        43   / 7        67
          43   / 7        13   / 2        79
          19   / 3        13   / 2        78
          13   / 2        7    / 1        76
          7    / 1        50   / 7        74
          50   / 7        15   / 2        73
          22   / 3        15   / 2        78
          15   / 2        8    / 1        79
          8    / 1        49   / 6        78
          57   / 7        25   / 3        79
          25   / 3        17   / 2        67
          17   / 2        9    / 1        66
          9    / 1        64   / 7        76
          64   / 7        19   / 2        81
          19   / 2        10   / 1        78
          10   / 1        71   / 7        69
          71   / 7        21   / 2        73
          21   / 2        23   / 2        74
          23   / 2        25   / 2        69
          25   / 2        27   / 2        62
          27   / 2        14   / 1        71
          14   / 1        15   / 1        74
          15   / 1        46   / 3        67
          61   / 4        16   / 1        66
          16   / 1        17   / 1        67
          17   / 1        18   / 1        79
          18   / 1        19   / 1        78
          19   / 1        77   / 4        76
          77   / 4        20   / 1        78
          20   / 1        21   / 1        74
          21   / 1        85   / 4        69
          85   / 4        22   / 1        71
          22   / 1        23   / 1        72
          23   / 1        93   / 4        66
          93   / 4        24   / 1        64
          24   / 1        25   / 1        66
          25   / 1        26   / 1        74
          26   / 1        79   / 3        72
          105  / 4        27   / 1        71
          27   / 1        82   / 3        69
          109  / 4        28   / 1        71
          28   / 1        29   / 1        67
          29   / 1        88   / 3        79
          117  / 4        30   / 1        78
          30   / 1        91   / 3        76
          121  / 4        31   / 1        78
          31   / 1        125  / 4        79
          125  / 4        32   / 1        74
          32   / 1        97   / 3        73
          129  / 4        33   / 1        78
          33   / 1        133  / 4        79
          133  / 4        34   / 1        71
          34   / 1        103  / 3        69
          137  / 4        35   / 1        78
          35   / 1        141  / 4        79
          141  / 4        36   / 1        67
          36   / 1        145  / 4        66
          145  / 4        37   / 1        69
          37   / 1        149  / 4        73
          149  / 4        38   / 1        76
          38   / 1        39   / 1        81
          39   / 1        157  / 4        78
          157  / 4        40   / 1        74
          40   / 1        41   / 1        69
          41   / 1        42   / 1        73
          42   / 1        43   / 1        74
          43   / 1        44   / 1        69
          44   / 1        45   / 1        62
          45   / 1        181  / 4        78
          181  / 4        46   / 1        79
          46   / 1        47   / 1        81
          47   / 1        189  / 4        78
          189  / 4        48   / 1        74
          48   / 1        49   / 1        72
          49   / 1        50   / 1        78
          50   / 1        151  / 3        71
          201  / 4        51   / 1        74
          51   / 1        205  / 4        79
          205  / 4        52   / 1        81
          52   / 1        53   / 1        83
          53   / 1        213  / 4        79
          213  / 4        54   / 1        75
          54   / 1        55   / 1        76
          55   / 1        221  / 4        72
          221  / 4        56   / 1        76
          56   / 1        225  / 4        69
          225  / 4        57   / 1        79
          57   / 1        172  / 3        78
          229  / 4        58   / 1        76
          58   / 1        233  / 4        71
          233  / 4        59   / 1        76
          59   / 1        237  / 4        75
          237  / 4        60   / 1        73
          60   / 1        61   / 1        71
          61   / 1        184  / 3        78
          245  / 4        62   / 1        71
          62   / 1        249  / 4        79
          249  / 4        63   / 1        76
          63   / 1        190  / 3        75
          253  / 4        64   / 1        76
          64   / 1        193  / 3        78
          257  / 4        65   / 1        71
          65   / 1        196  / 3        79
          261  / 4        66   / 1        71
          66   / 1        265  / 4        81
          265  / 4        67   / 1        78
          67   / 1        202  / 3        76
          269  / 4        68   / 1        78
          68   / 1        205  / 3        79
          273  / 4        69   / 1        71
          69   / 1        208  / 3        81
          277  / 4        70   / 1        69
          70   / 1        281  / 4        67
          281  / 4        71   / 1        83
          71   / 1        285  / 4        78
          285  / 4        72   / 1        79
          72   / 1        73   / 1        71
          73   / 1        220  / 3        76
          293  / 4        74   / 1        75
          74   / 1        75   / 1        76
          75   / 1        76   / 1        71
          76   / 1        77   / 1        64
          77   / 1        309  / 4        76
          309  / 4        78   / 1        78
          78   / 1        79   / 1        79
          79   / 1        238  / 3        73
          317  / 4        80   / 1        71
          80   / 1        81   / 1        73
          81   / 1        82   / 1        69
          82   / 1        247  / 3        62
          329  / 4        83   / 1        69
          83   / 1        333  / 4        79
          333  / 4        84   / 1        76
          84   / 1        85   / 1        78
          85   / 1        341  / 4        74
          341  / 4        86   / 1        72
          86   / 1        345  / 4        71
          345  / 4        87   / 1        74
          87   / 1        349  / 4        79
          349  / 4        88   / 1        71
          88   / 1        353  / 4        69
          353  / 4        89   / 1        84
          89   / 1        357  / 4        83
          357  / 4        90   / 1        79
          90   / 1        361  / 4        81
          361  / 4        91   / 1        79
          91   / 1        365  / 4        78
          365  / 4        92   / 1        76
          92   / 1        93   / 1        74
          93   / 1        373  / 4        78
          373  / 4        94   / 1        79
          94   / 1        283  / 3        81
          377  / 4        95   / 1        78
          95   / 1        381  / 4        74
          381  / 4        96   / 1        76
          96   / 1        289  / 3        78
          385  / 4        97   / 1        74
          97   / 1        389  / 4        69
          389  / 4        98   / 1        71
          98   / 1        295  / 3        72
          393  / 4        99   / 1        69
          99   / 1        397  / 4        66
          397  / 4        100  / 1        67
          100  / 1        301  / 3        69
          401  / 4        101  / 1        66
          101  / 1        405  / 4        62
          405  / 4        102  / 1        72
          102  / 1        307  / 3        71
          409  / 4        103  / 1        67
          103  / 1        413  / 4        62
          413  / 4        104  / 1        74
          104  / 1        313  / 3        71
          417  / 4        105  / 1        67
          105  / 1        421  / 4        62
          421  / 4        106  / 1        79
          106  / 1        319  / 3        74
          425  / 4        107  / 1        71
          107  / 1        322  / 3        72
          429  / 4        108  / 1        69
          108  / 1        325  / 3        71
          433  / 4        109  / 1        67
          109  / 1        437  / 4        62
          437  / 4        110  / 1        71
          110  / 1        331  / 3        69
          441  / 4        111  / 1        71
          111  / 1        445  / 4        72
          445  / 4        112  / 1        67
          112  / 1        337  / 3        66
          449  / 4        113  / 1        71
          113  / 1        453  / 4        72
          453  / 4        114  / 1        64
          114  / 1        343  / 3        62
          457  / 4        115  / 1        71
          115  / 1        461  / 4        72
          461  / 4        116  / 1        60
          116  / 1        465  / 4        59
          465  / 4        117  / 1        62
          117  / 1        469  / 4        66
          469  / 4        118  / 1        69
          118  / 1        119  / 1        74
          119  / 1        477  / 4        71
          477  / 4        120  / 1        67
          120  / 1        121  / 1        62
          121  / 1        122  / 1        66
          122  / 1        125  / 1        67
          126  / 1        505  / 4        74
          505  / 4        253  / 2        67
          253  / 2        253  / 2        67
          127  / 1        509  / 4        78
          509  / 4        255  / 2        76
          255  / 2        128  / 1        74
          128  / 1        513  / 4        72
          513  / 4        257  / 2        66
          257  / 2        257  / 2        66
          129  / 1        1549 / 12       72
          1678 / 13       388  / 3        71
          517  / 4        259  / 2        69
          259  / 2        130  / 1        67
          130  / 1        1561 / 12       76
          1691 / 13       391  / 3        78
          521  / 4        261  / 2        79
          261  / 2        131  / 1        73
          131  / 1        1573 / 12       69
          1704 / 13       394  / 3        78
          525  / 4        263  / 2        79
          263  / 2        132  / 1        66
          132  / 1        529  / 4        81
          529  / 4        265  / 2        78
          265  / 2        133  / 1        69
          133  / 1        533  / 4        74
          533  / 4        267  / 2        69
          267  / 2        134  / 1        62
          134  / 1        537  / 4        81
          537  / 4        269  / 2        78
          269  / 2        135  / 1        72
          135  / 1        1621 / 12       71
          1756 / 13       406  / 3        74
          541  / 4        271  / 2        79
          271  / 2        136  / 1        83
          136  / 1        545  / 4        76
          545  / 4        273  / 2        72
          273  / 2        137  / 1        69
          137  / 1        1782 / 13       71
          1782 / 13       549  / 4        76
          549  / 4        275  / 2        75
          275  / 2        138  / 1        71
          138  / 1        1795 / 13       79
          1795 / 13       415  / 3        76
          553  / 4        277  / 2        75
          277  / 2        139  / 1        78
          139  / 1        1808 / 13       81
          1808 / 13       418  / 3        78
          557  / 4        279  / 2        76
          279  / 2        140  / 1        79
          140  / 1        1821 / 13       67
          1821 / 13       561  / 4        83
          561  / 4        281  / 2        78
          281  / 2        141  / 1        71
          141  / 1        141  / 1        76
          565  / 4        283  / 2        71
          283  / 2        142  / 1        64
          142  / 1        569  / 4        79
          569  / 4        285  / 2        73
          285  / 2        285  / 2        73
          143  / 1        1717 / 12       62
          1860 / 13       430  / 3        69
          573  / 4        287  / 2        79
          287  / 2        144  / 1        78
          144  / 1        1873 / 13       71
          1873 / 13       577  / 4        74
          577  / 4        289  / 2        79
          289  / 2        145  / 1        69
          145  / 1        1886 / 13       81
          1886 / 13       581  / 4        79
          581  / 4        291  / 2        78
          291  / 2        146  / 1        74
          146  / 1        1753 / 12       81
          1899 / 13       439  / 3        78
          585  / 4        293  / 2        74
          293  / 2        147  / 1        78
          147  / 1        1765 / 12       72
          1912 / 13       442  / 3        69
          589  / 4        295  / 2        66
          295  / 2        148  / 1        69
          148  / 1        1777 / 12       71
          1925 / 13       445  / 3        67
          593  / 4        297  / 2        62
          297  / 2        149  / 1        71
          149  / 1        1789 / 12       74
          1938 / 13       597  / 4        71
          597  / 4        299  / 2        72
          299  / 2        150  / 1        71
          150  / 1        1801 / 12       69
          1951 / 13       451  / 3        71
          601  / 4        301  / 2        72
          301  / 2        151  / 1        66
          151  / 1        1813 / 12       62
          1964 / 13       454  / 3        71
          605  / 4        303  / 2        72
          303  / 2        152  / 1        59
          152  / 1        609  / 4        74
          609  / 4        305  / 2        71
          305  / 2        153  / 1        62
          153  / 1        154  / 1        67
"""
