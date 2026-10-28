# Idea source (STANDING RULE #1): warikoo "Home Loan Mistakes That Cost You LAKHS" (~1.2M views). Our own story, mistakes and numbers.
# Numbers (Python, reducing-balance EMI, monthly rate r/12; examples only):
#  ₹50L @8.5%: 20 yr EMI ₹43,391, interest ₹54.14L; 30 yr EMI ₹38,446 (₹4,945 less), interest ₹88.40L (+₹34.3L)
#  rate 8.5% -> 9.5% after 12 months, EMI kept ₹43,391: total ~297 months (~24.7 yr), interest ₹78.75L (+₹24.6L)
#  same rise but EMI raised to ₹46,498, tenure kept 20 yr: interest ₹61.22L -> saves ~₹17.5L vs tenure extension
#  ₹50,000 insurance premium added to the loan @8.5%, 20 yr: repaid ₹1,04,139
LINES = [
 (1,"P","चिंटू ने पचास लाख का होम लोन लिया... और तीन महंगी गलतियाँ कीं!",[("HOME LOAN KI 3 GALTIYAN","white"),("₹34 LAKH TAK NUKSAAN!","red")],"s01"),
 (2,"G","मुझे EMI कम चाहिए! तीस साल का लोन दे दो!",[("GALTI #1","gold"),("30 SAAL KA LOAN","white")],"s02"),
 (3,"P","EMI सिर्फ़ पाँच हज़ार कम हुई... लेकिन ब्याज, चौंतीस लाख ज़्यादा!",[("EMI −₹4,945","teal"),("BYAAJ +₹34 LAKH","red")],"s03"),
 (4,"P","दूसरी गलती: रेट एक परसेंट बढ़ा, और बैंक ने चुपचाप लोन के साल बढ़ा दिए।",[("GALTI #2","gold"),("RATE +1% = SAAL BADHE","white")],"s04"),
 (5,"G","क्या?! बीस साल का लोन, पच्चीस साल का?!",[("20 SAAL → ~25 SAAL","red")],"s05"),
 (6,"P","हाँ, और ब्याज लगभग पच्चीस लाख और! अगर EMI बढ़वाता, तो सत्रह लाख बचते।",[("BYAAJ +₹24.6 LAKH","red"),("EMI BADHAO: ~₹17.5 LAKH BACHAT","teal")],"s06"),
 (7,"P","तीसरी गलती: पचास हज़ार का इंश्योरेंस भी लोन में जोड़ दिया। अब उस पर भी ब्याज! कुल, एक लाख चार हज़ार।",[("GALTI #3","gold"),("₹50,000 → ₹1.04 LAKH","red")],"s07"),
 (8,"P","आपने इनमें से कौन सी गलती की है? कमेंट में नंबर लिखो!",[("AAPKI GALTI: 1, 2 YA 3?","gold")],"s08"),
]
