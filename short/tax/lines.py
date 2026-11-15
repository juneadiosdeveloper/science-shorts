# Category: Tax (GROWTH PLAN idea #2). Idea source (STANDING RULE #1, idea only): popular "₹12 lakh tax-free / marginal relief" explainers after Budget 2025-26.
# Rules (new regime, tax year 2026-27, resident individual; Budget 2026 left them unchanged): slabs 0-4L nil, 4-8L 5%, 8-12L 10%, 12-16L 15%...;
# rebate keeps total income up to ₹12,00,000 tax-free (rebate up to ₹60,000); standard deduction ₹75,000 for salaried; marginal relief caps tax at
# (income - ₹12,00,000) up to ~₹12,70,588 total income; 4% cess on tax after relief.
# Numbers (Python): salary ₹12,75,000 → taxable ₹12,00,000 → tax ₹0. Salary ₹13,00,000 → taxable ₹12,25,000 → slab tax ₹63,750, capped at ₹25,000
# + 4% cess = ₹26,000 → in hand ₹12,74,000 (₹1,000 less than ₹12,75,000). Relief zone ends at salary ~₹13,45,588.
LINES = [
 (1,"P","बारह लाख पचहत्तर हज़ार की सैलरी पर टैक्स ज़ीरो... और तेरह लाख पर छब्बीस हज़ार?",[("₹12.75 LAKH = TAX ₹0","teal"),("₹13 LAKH = TAX ₹26,000?","red")],"s01"),
 (2,"G","मेरा इन्क्रीमेंट हुआ! पच्चीस हज़ार ज़्यादा!",[("INCREMENT +₹25,000","gold")],"s02"),
 (3,"P","नए रिजीम में बारह लाख तक की इनकम पर टैक्स ज़ीरो।",[("₹12 LAKH TAK TAX ₹0","teal")],"s03"),
 (4,"P","और सैलरी वालों को पचहत्तर हज़ार की छूट अलग से।",[("+ ₹75,000 STANDARD DEDUCTION","white"),("= ₹12.75 LAKH SALARY TAX-FREE","teal")],"s04"),
 (5,"P","पर चिंटू की इनकम बारह लाख से पच्चीस हज़ार ऊपर गई... तो टैक्स पच्चीस हज़ार, सेस मिलाकर छब्बीस हज़ार!",[("TAXABLE ₹12.25 LAKH","white"),("TAX ₹26,000","red")],"s05"),
 (6,"G","मतलब इन्क्रीमेंट के बाद... मेरे हाथ में हज़ार रुपये कम?!",[("HAATH MEIN ₹1,000 KAM!","red")],"s06"),
 (7,"P","ऐसे टैक्स के झटकों से बचना है? फॉलो करो!",[("FOLLOW KARO","gold")],"s07"),
 (8,"P","ये है मार्जिनल रिलीफ: सैलरी तेरह लाख पैंतालीस हज़ार तक हो, तो बारह लाख पचहत्तर के ऊपर की पूरी कमाई टैक्स में जा सकती है।",[("MARGINAL RELIEF ZONE","gold"),("₹12.75L SE ₹13.45L","white")],"s08"),
 (9,"P","आपकी सैलरी इस ज़ोन में है? हाँ या ना, कमेंट करो...",[("AAP IS ZONE MEIN?","gold"),("HAAN / NAA","white")],"s09"),
 (10,"P","और ये उस दोस्त को भेजो जिसका इन्क्रीमेंट आने वाला है।",[("BHEJO US DOST KO","gold"),("JISKA INCREMENT AANE WALA HAI","white")],"s10"),
]
