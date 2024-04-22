# 'PatternData' class hierarchy
# Keeps track of pattern metadata for use in the pdf pattern

class PatternData:
    def __init__(self,
                rowGauge=None,
                colGauge=None,
                patternTitle=None,
                patternSubtitle=None,
                yarnWeight=None,
                yarnType=None,
                needleSize_mm=None,
                needleSize_US=None,
                skillLevel=None,
                patternIntro=None,
                patternSizing=None,
                patternNeedles=None,
                patternYarn=None,
                patternGauge=None,
                patternNotions=None,
                patternAbbrev=None,
                patternSizeChart=None):

        self.rowGauge = 7 if rowGauge is None else rowGauge
        self.colGauge = 7 if colGauge is None else colGauge
        self.patternTitle = "Pattern Name Here" if patternTitle is None else patternTitle
        self.patternSubtitle = "Pattern Subtitle Here" if patternSubtitle is None else patternSubtitle
        self.yarnWeight = "worsted" if yarnWeight is None else yarnWeight
        self.yarnType = "Cascade 220" if yarnType is None else yarnType
        self.needleSize_mm = 0 if needleSize_mm is None else needleSize_mm
        self.needleSize_US = 0 if needleSize_US is None else needleSize_US
        self.skillLevel = "beginner" if skillLevel is None else skillLevel
        self.patternIntro = ["Intro", "Text", "Here"] if patternIntro is None else patternIntro
        self.patternSizing = ["sizing", "Text", "Here"] if patternSizing is None else patternSizing
        self.patternNeedles = ["US XX, X.Xmm"] if patternNeedles is None else patternNeedles
        self.patternYarn = [f"(200,300,400,500) meters of {self.yarnType} which requires (1,1,1,2) balls"] if patternYarn is None else patternYarn
        self.patternGauge = [f"{rowGauge} row, {colGauge} columns in a 10cm x 10cm swatch"] if patternGauge is None else patternGauge
        self.patternNotions = ["stitch marker, tapestry needle"] if patternNotions is None else patternNotions
        self.patternAbbrev = {"k2tog":"knit two together",
                              "p2tog":"purl two together",
                              "ssk":"slip-slip-knit",} if patternAbbrev is None else patternAbbrev
        self.patternSizeChart = [["", "Infant", "Child", "Adult S", "Adult L"],
                                 ["Size Number", "0", "1", "2", "3"],
                                 ["Length (cm)", "5", "10", "15", "20"],
                                 ["Height (cm)", "10", "20", "30", "40"]] if patternSizeChart is None else patternSizeChart