# stylesheets used by the document class

from reportlab.lib.styles import ParagraphStyle

# stylesheet for pattern instructions
patternStyle = ParagraphStyle(
                        "pattern text",
                        alignment = 0,
                        allowOrphans = 0,
                        allowWidows = 1,
                        embeddedHyphenation = 0,
                        endDots = None,
                        firstLineIndent = 0,
                        fontName = "IMFell",
                        fontSize = 15,
                        justifyBreaks = 0,
                        justifyLastLine = 0,
                        leading = 12, #space between lines
                        leftIndent = 0,
                        linkUnderLine = 0,
                        rightIndent = 0,
                        spaceAfter = 0,
                        spaceBefore = 0,
                        spaceShrinkage = 0.05,
                        splitLongWords = 1,
                        strikeGap = 1,
                        textTransform = None,
                        underlineGap = 1,
                        wordWrap = None,
)

# stylesheet for pattern instructions
titleStyle = ParagraphStyle(
                        "title text",
                        alignment = 0,
                        allowOrphans = 0,
                        allowWidows = 1,
                        embeddedHyphenation = 0,
                        endDots = None,
                        firstLineIndent = 0,
                        fontName = "IMFell",
                        fontSize = 20,
                        justifyBreaks = 0,
                        justifyLastLine = 0,
                        leading = 15, #space between lines
                        leftIndent = 0,
                        linkUnderLine = 0,
                        rightIndent = 0,
                        spaceAfter = 0,
                        spaceBefore = 0,
                        spaceShrinkage = 0.05,
                        splitLongWords = 1,
                        strikeGap = 1,
                        textTransform = None,
                        underlineGap = 1,
                        wordWrap = None,
)

# stylesheet for pattern instructions
introStyle = ParagraphStyle(
                        "intro text",
                        alignment = 0,
                        allowOrphans = 0,
                        allowWidows = 1,
                        embeddedHyphenation = 0,
                        endDots = None,
                        firstLineIndent = 0,
                        fontName = "IMFell",
                        fontSize = 16,
                        justifyBreaks = 0,
                        justifyLastLine = 0,
                        leading = 18, #space between lines
                        leftIndent = 0,
                        linkUnderLine = 0,
                        rightIndent = 0,
                        spaceAfter = 0,
                        spaceBefore = 0,
                        spaceShrinkage = 0.05,
                        splitLongWords = 1,
                        strikeGap = 1,
                        textTransform = None,
                        underlineGap = 1,
                        wordWrap = None,
)