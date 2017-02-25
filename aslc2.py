import string

#
# Per-line counting functions
#
def countLines(ln):      return 1
def countBlankLines(ln): return 0 if ln.strip() else 1
def countWords(ln):      return len(ln.split())

def charCounter(validChars):
    vc = set(validChars)
    def counter(ln):
        return sum(1 for ch in ln if ch in vc)
    return counter
countSentences = charCounter('.!?')
countLetters   = charCounter(string.ascii_letters)
countPunct     = charCounter(string.punctuation)

#
# do counting
#
class FileStats(object):
    def __init__(self, countFns, labels=None):
        super(FileStats,self).__init__()
        self.fns    = countFns
        self.labels = labels if labels else [fn.__name__ for fn in countFns]
        self.reset()

    def reset(self):
        self.counts = [0]*len(self.fns)

    def doFile(self, fname):
        try:
            with open(fname) as inf:
                for line in inf:
                    for i,fn in enumerate(self.fns):
                        self.counts[i] += fn(line)
        except IOError:
            print('Could not open file {0} for reading'.format(fname))

    def __str__(self):
        return '\n'.join('{0:20} {1:>6}'.format(label, count) for label,count in zip(self.labels, self.counts))

fs = FileStats(
    (countLines, countBlankLines, countSentences, countWords, countLetters, countPunct, (len(ln.split())/countSentences)),
    ("Lines",    "Blank Lines",   "Sentences",    "Words",    "Letters",    "Punctuation",    "Average Sentence Length:")
)
fs.doFile('aslcSample2.txt')
print(fs)
